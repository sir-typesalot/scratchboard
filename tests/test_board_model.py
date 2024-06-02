import pytest
from lib.models.BoardModel import BoardModel
from .data_populator import populate_tables

@pytest.mark.parametrize("seed, name, expected", [
    ('unique seed', 'New Board', 1)
])
def test_create_new(db, seed, name, expected):
    exists = BoardModel().create_new(seed, name)
    assert exists is expected

def test_create_new_error(db):
    populate_tables(['boards'])
    with pytest.raises(NameError):
        BoardModel().create_new('test hashing', 'Test Project')

@pytest.mark.parametrize("seed, expected", [
    ('test hash', 'bb5d944c0fcda36e4912245f1b295a612107f35bf8e7ab4e2b9bbb5f')
])
def test_generate_hash(seed, expected):
    assert expected == BoardModel.generate_hash(seed)

def test_modify_board(db):
    populate_tables(['boards'])
    board = BoardModel().get({'hash': '164b2551025f1ed0261a33febdd5d75435c987de8854f2b1cda909c0'})
    board.name = 'Changed Name'
    # TODO: Take a look at this one... a little stupid
    BoardModel().modify(board)
    modified = BoardModel().get({'hash': '164b2551025f1ed0261a33febdd5d75435c987de8854f2b1cda909c0'})
    assert modified.name == 'Changed Name'
