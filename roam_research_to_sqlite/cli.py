from pathlib import Path
from zipfile import ZipFile
import click
import json
import logging
from . import service


@click.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.argument(
    "roam_export_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.option('-v', '--verbose', count=True)
@click.version_option()
def cli(db_path, roam_export_path, verbose):
    """
    Save data from Roam Research's JSON export to a SQLite database.
    """
    logging.basicConfig(level=verbose)

    db_path = Path(db_path)
    db = service.open_database(db_path)

    roam_export_path = Path(roam_export_path)
    with ZipFile(roam_export_path, 'r') as zip_file_obj:
        file_name = [name for name in zip_file_obj.namelist() if name.endswith(".json")][0]
        raw_pages = zip_file_obj.read(file_name)

    pages_one = json.loads(raw_pages)
    pages_two = json.loads(raw_pages)

    service.save_pages(db, pages_one)
    service.save_blocks(db, pages_two)
