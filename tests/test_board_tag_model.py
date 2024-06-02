import pytest
from lib.models.TagModel import TagModel
from .data_populator import populate_tables

@pytest.mark.parametrize("board_id, name, expected", [
    (1, 'TestingTag', 1)
])
def test_create_new(db, board_id, name, expected):
    populate_tables(['boards'])
    exists = TagModel().create_new(board_id, name, None)
    assert exists is expected

def test_create_new_error(db):
    populate_tables(['boards', 'board_tags'])
    with pytest.raises(NameError):
        TagModel().create_new(1, 'TestTag', 'Test the description')
