import datetime
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

from sqlite_utils.db import Database, Table

logger = logging.getLogger(__name__)


def open_database(db_file_path: Path) -> Database:
    """
    Open the Roam Research SQLite database.
    """
    return Database(db_file_path)


def get_table(table_name: str, db: Database) -> Table:
    """
    Returns a Table from a given db Database object.
    """
    return Table(db=db, name=table_name)


def build_database(db: Database):
    """
    Build the Roam Research SQLite database structure.
    """
    pages_table = get_table("pages", db=db)
    blocks_table = get_table("blocks", db=db)

    if pages_table.exists() is False:
        logger.info("Building the pages table.")
        pages_table.create(
            columns={
                "uid": str,
                "title": str,
                "daily_note_date": Optional[datetime.date],
                "create_time": datetime.datetime,
                "edit_time": datetime.datetime,
            },
            pk="uid",
        )
        pages_table.enable_fts(["title"], create_triggers=True)

    pages_table_indexes = {tuple(i.columns) for i in pages_table.indexes}
    if ("daily_note_date",) not in pages_table_indexes:
        blocks_table.create_index(["daily_note_date"])

    if blocks_table.exists() is False:
        logger.info("Building the blocks table.")
        blocks_table.create(
            columns={
                "uid": str,
                "page_uid": str,
                "parent_uid": str,
                "string": str,
                "create_time": datetime.datetime,
                "edit_time": datetime.datetime,
            },
            pk="uid",
            foreign_keys=(
                ("page_uid", "pages", "uid"),
                ("parent_uid", "blocks", "uid"),
            ),
        )
        blocks_table.enable_fts(["string"], create_triggers=True)

    blocks_table_indexes = {tuple(i.columns) for i in blocks_table.indexes}
    if ("page_uid",) not in blocks_table_indexes:
        blocks_table.create_index(["page_uid"])
    if ("parent_uid",) not in blocks_table_indexes:
        blocks_table.create_index(["parent_uid"])


def transform_daily_note_uid_to_date(uid: str) -> Optional[datetime.date]:
    """
    Transform a Roam Research daily note page's UID into a date object.
    """
    try:
        return datetime.datetime.strptime(uid, "%m-%d-%Y").date()
    except ValueError:
        return None


def transform_time(value: Optional[int]) -> Optional[datetime.datetime]:
    """
    Transform a Roam Research time value into a datetime object.
    """
    if value is None:
        return None

    return datetime.datetime.fromtimestamp(value / 1000)


def transform_page(page: Dict[str, Any]):
    """
    Transformer a Roam Research page, so it can be safely saved to the SQLite
    database.
    """
    page["daily_note_date"] = transform_daily_note_uid_to_date(
        page.get("uid", "")
    )
    page["create_time"] = transform_time(page.pop("create-time"))
    page["edit_time"] = transform_time(page.pop("edit-time"))

    to_remove = [
        k
        for k in page.keys()
        if k
        not in (
            "uid",
            "title",
            "daily_note_date",
            "create_time",
            "edit_time",
        )
    ]
    for key in to_remove:
        del page[key]


def save_pages(db: Database, pages: List[Dict[str, Any]]):
    """
    Save Roam Research pages to the SQLite database.
    """
    build_database(db)
    pages_table = get_table("pages", db=db)

    logger.info(f"Found {len(pages)} pages to import.")

    for page in pages:
        transform_page(page)

    pages_table.upsert_all(pages, pk="uid")

    logger.info(f"Saved {pages_table.count} rows into the pages table.")


def transform_block(
    block: Dict[str, Any],
    page_uid: str,
    parent_uid: Optional[str] = None,
):
    """
    Transformer a Roam Research block, so it can be safely saved to the SQLite
    database.
    """
    block["create_time"] = transform_time(block.pop("create-time", None))
    block["edit_time"] = transform_time(block.pop("edit-time", None))

    to_remove = [
        k
        for k in block.keys()
        if k not in ("uid", "string", "create_time", "edit_time")
    ]
    for key in to_remove:
        del block[key]

    block["page_uid"] = page_uid
    block["parent_uid"] = parent_uid


def flatten_block_hierarchy(
    children: List[Dict[str, Any]],
    page_uid: str,
    parent_uid: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Flatten a Roam Research page block hierarchy's structure.
    """
    _children: List[Dict[str, Any]] = []

    for child in children:
        child["page_uid"] = page_uid
        child["parent_uid"] = parent_uid

        _children.append(child)

        if "children" in child and len(child["children"]) > 0:
            _children.extend(
                flatten_block_hierarchy(
                    child["children"],
                    page_uid=page_uid,
                    parent_uid=child["uid"],
                )
            )

    return _children


def save_blocks(db: Database, pages: List[Dict[str, Any]]):
    """
    Save Roam Research blocks to the SQLite database.
    """
    build_database(db)
    blocks_table = get_table("blocks", db=db)

    blocks = []
    for page in pages:
        if "children" in page and len(page["children"]) > 0:
            blocks.extend(
                flatten_block_hierarchy(page["children"], page_uid=page["uid"])
            )

    logger.info(f"Found {len(blocks)} blocks to import.")

    for block in blocks:
        transform_block(
            block,
            page_uid=block["page_uid"],
            parent_uid=block.get("parent_id", None),
        )

    blocks_table.upsert_all(blocks, pk="uid")

    logger.info(f"Saved {blocks_table.count} rows into the blocks table.")
