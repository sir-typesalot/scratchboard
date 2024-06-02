import pytest
from lib.models.BoardTagModel import BoardTagModel
from .data_populator import populate_tables

@pytest.mark.parametrize("board_id, name, expected", [
    (1, 'TestingTag', 1)
])
def test_create_new(db, board_id, name, expected):
    populate_tables(['boards'])
    exists = BoardTagModel().create_new(board_id, name, None)
    assert exists is expected

def test_create_new_error(db):
    populate_tables(['boards', 'board_tags'])
    with pytest.raises(NameError):
        BoardTagModel().create_new(1, 'TestTag', 'Test the description')
