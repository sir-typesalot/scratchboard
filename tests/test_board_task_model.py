import pytest
from lib.models.TaskModel import TaskModel
from .data_populator import populate_tables

@pytest.mark.parametrize("board_hash, tag_id, name, expected", [
    ('164b2551025f1ed0261a33febdd5d75435c987de8854f2b1cda909c0', 1, 'Test Title', 1)
])
def test_create_new(db, board_hash, tag_id, name, expected):
    populate_tables(['boards', 'board_tags'])
    exists = TaskModel(board_hash).create(tag_id=tag_id, title=name, description=None)
    assert exists is expected

def test_modify_task(db):
    populate_tables(['boards', 'board_tags', 'board_tasks'])
    hash = '164b2551025f1ed0261a33febdd5d75435c987de8854f2b1cda909c0'
    task = TaskModel(hash).get({'task_id': 1})[0]
    task.status = 'progress'
    # TODO: Take a look at this one... a little stupid
    TaskModel(hash).modify(task)
    task = TaskModel(hash).get({'task_id': 1})[0]
    assert task.status == 'progress'
