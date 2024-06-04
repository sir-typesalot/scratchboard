import pytest
from lib.models.TagModel import TagModel
from .data_populator import populate_tables

@pytest.mark.parametrize("board_hash, name, expected", [
    ('164b2551025f1ed0261a33febdd5d75435c987de8854f2b1cda909c0', 'TestingTag', 1)
])
def test_create_new(db, board_hash, name, expected):
    populate_tables(['boards'])
    exists = TagModel(board_hash).create_new(name, None)
    assert exists is expected

def test_create_new_error(db):
    populate_tables(['boards', 'board_tags'])
    hash = '164b2551025f1ed0261a33febdd5d75435c987de8854f2b1cda909c0'
    with pytest.raises(NameError):
        TagModel(hash).create_new('TestTag', 'Test the description')
