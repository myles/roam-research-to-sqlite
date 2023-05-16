import datetime

import pytest

from roam_research_to_sqlite import service

from . import fixtures


@pytest.mark.parametrize(
    "value, expected_result",
    (
        (
            "January 1st, 2022",
            {"month": "January", "day": "1", "year": "2022"},
        ),
        (
            "January 2nd, 2022",
            {"month": "January", "day": "2", "year": "2022"},
        ),
        (
            "January 3rd, 2022",
            {"month": "January", "day": "3", "year": "2022"},
        ),
        (
            "January 4th, 2022",
            {"month": "January", "day": "4", "year": "2022"},
        ),
    ),
)
def test_re_daily_log(value, expected_result):
    result = service.RE_DAILY_LOG.match(value)

    assert result is not None
    assert result.groupdict() == expected_result


@pytest.mark.parametrize(
    "value, expected_result",
    (
        ("January 1st, 2022", datetime.date(2022, 1, 1)),
        ("January 2nd, 2022", datetime.date(2022, 1, 2)),
        ("January 3rd, 2022", datetime.date(2022, 1, 3)),
        ("January 4th, 2022", datetime.date(2022, 1, 4)),
        ("January 2022", None),
        ("Hello, World!", None),
    ),
)
def test_extract_daily_note_date(value, expected_result):
    result = service.extract_daily_note_date(value)

    assert result == expected_result


def test_transform_page():
    page = fixtures.PAGE_ONE.copy()

    service.transform_page(page)

    assert page == {
        "uid": fixtures.PAGE_ONE["uid"],
        "title": fixtures.PAGE_ONE["title"],
        "is_daily_note": False,
        "daily_note_date": None,
        "create_time": fixtures.PAGE_ONE["create-time"],
        "edit_time": fixtures.PAGE_ONE["edit-time"],
    }


def test_transform_page__daily_note():
    page = fixtures.DAILY_NOTE_PAGE.copy()

    service.transform_page(page)

    assert page == {
        "uid": fixtures.DAILY_NOTE_PAGE["uid"],
        "title": fixtures.DAILY_NOTE_PAGE["title"],
        "is_daily_note": True,
        "daily_note_date": datetime.date(2023, 5, 15),
        "create_time": fixtures.DAILY_NOTE_PAGE["create-time"],
        "edit_time": fixtures.DAILY_NOTE_PAGE["edit-time"],
    }


def test_transform_block():
    block = fixtures.BLOCK_ONE.copy()
    page_uid = "IAmAPageUID"
    parent_uid = "IAmABlockParentUID"

    service.transform_block(block, page_uid=page_uid, parent_uid=parent_uid)

    assert block == {
        "uid": fixtures.BLOCK_ONE["uid"],
        "string": fixtures.BLOCK_ONE["string"],
        "create_time": fixtures.BLOCK_ONE["create-time"],
        "edit_time": fixtures.BLOCK_ONE["edit-time"],
        "page_uid": page_uid,
        "parent_uid": parent_uid,
    }


def test_flatten_block_hierarchy():
    page_uid = "IAmAPageUID"

    block = fixtures.BLOCK_TWO.copy()

    block_child_one = fixtures.BLOCK_TWO_CHILD_ONE.copy()
    block_child_two = fixtures.BLOCK_TWO_CHILD_TWO.copy()

    block["children"] = [block_child_one, block_child_two]

    flatten_blocks = service.flatten_block_hierarchy(
        children=[block],
        page_uid=page_uid,
    )

    assert len(flatten_blocks) == 3
    assert block in flatten_blocks
    assert block_child_one in flatten_blocks
    assert block_child_two in flatten_blocks
