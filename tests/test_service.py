from roam_research_to_sqlite import service
from . import fixtures


def test_transform_page():
    page = fixtures.PAGE_ONE.copy()

    service.transform_page(page)

    assert page == {
        "uid": fixtures.PAGE_ONE["uid"],
        "title": fixtures.PAGE_ONE["title"],
        "create_time": fixtures.PAGE_ONE["create-time"],
        "edit_time": fixtures.PAGE_ONE["edit-time"],
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

    block['children'] = [block_child_one, block_child_two]

    flatten_blocks = service.flatten_block_hierarchy(
        children=[block],
        page_uid=page_uid,
    )

    assert len(flatten_blocks) == 3
    assert block in flatten_blocks
    assert block_child_one in flatten_blocks
    assert block_child_two in flatten_blocks
