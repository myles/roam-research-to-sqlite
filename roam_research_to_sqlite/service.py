import logging
from pathlib import Path
from typing import Any, Dict, List

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
                "create_time": int,
                "edit_time": int,
            },
            pk="uid",
        )
        pages_table.enable_fts(["title"], create_triggers=True)

    if blocks_table.exists() is False:
        logger.info("Building the blocks table.")
        blocks_table.create(
            columns={
                "uid": str,
                "page_uid": str,
                "parent_uid": str,
                "string": str,
                "create_time": int,
                "edit_time": int,
            },
            pk="uid",
        )
        blocks_table.enable_fts(["string"], create_triggers=True)
        blocks_table.add_foreign_key("page_uid", "pages", "uid")
        blocks_table.add_foreign_key("parent_uid", "blocks", "uid")

    blocks_table_indexes = {tuple(i.columns) for i in blocks_table.indexes}
    if ("page_uid",) not in blocks_table_indexes:
        blocks_table.create_index(["page_uid"])
    if ("parent_uid",) not in blocks_table_indexes:
        blocks_table.create_index(["parent_uid"])


def transform_page(page: Dict[str, Any]):
    """
    Transformer a Roam Research page, so it can be safely saved to the SQLite
    database.
    """
    page["create_time"] = page.pop("create-time")
    page["edit_time"] = page.pop("edit-time")

    to_remove = [
        k
        for k in page.keys()
        if k not in ("uid", "title", "create_time", "edit_time")
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

    pages_table.insert_all(pages, pk="uid", alter=True, replace=True)

    logger.info(f"Saved {pages_table.count} rows into the pages table.")


def transform_block(
    block: Dict[str, Any],
    page_uid: str,
    parent_uid: str = None,
):
    """
    Transformer a Roam Research block, so it can be safely saved to the SQLite
    database.
    """
    block["create_time"] = block.pop("create-time", None)
    block["edit_time"] = block.pop("edit-time", None)

    to_remove = [
        k
        for k in block.keys()
        if k not in ("uid", "string", "create_time", "edit_time")
    ]
    for key in to_remove:
        del block[key]

    block["page_uid"] = page_uid
    block["parent_uid"] = parent_uid


def flatten_page_block_hierarchy(
    page: Dict[str, Any],
    page_uid: str,
    parent_uid: str = None,
) -> List[Dict[str, Any]]:
    """
    Flatten a Roam Research page block hierarchy's structure.
    """
    children = []

    if "children" not in page:
        return children

    for child in page["children"]:
        child["page_uid"] = page_uid
        child["parent_uid"] = parent_uid

        if "children" in child:
            children.extend(
                flatten_page_block_hierarchy(
                    child,
                    page_uid=page_uid,
                    parent_uid=child["uid"],
                )
            )
        else:
            children.append(child)

    return children


def save_blocks(db: Database, pages: List[Dict[str, Any]]):
    """
    Save Roam Research blocks to the SQLite database.
    """
    build_database(db)
    blocks_table = get_table("blocks", db=db)

    blocks = []
    for page in pages:
        blocks.extend(flatten_page_block_hierarchy(page, page_uid=page["uid"]))

    logger.info(f"Found {len(blocks)} blocks to import.")

    for block in blocks:
        transform_block(
            block,
            page_uid=block["page_uid"],
            parent_uid=block.get("parent_id", None),
        )

    blocks_table.insert_all(blocks, pk="uid", alter=True, replace=True)

    logger.info(f"Saved {blocks_table.count} rows into the blocks table.")
