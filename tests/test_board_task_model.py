import pytest
from lib.models.TaskModel import TaskModel
from .data_populator import populate_tables

@pytest.mark.parametrize("board_id, tag_id, name, expected", [
    (1, 1, 'Test Title', 1)
])
def test_create_new(db, board_id, tag_id, name, expected):
    populate_tables(['boards', 'board_tags'])
    exists = TaskModel().create(board_id, tag_id=tag_id, title=name, description=None)
    assert exists is expected

def test_modify_board(db):
    populate_tables(['boards', 'board_tags', 'board_tasks'])
    task = TaskModel().get({'board_id': 1, 'task_id': 1})
    task.status = 'progress'
    # TODO: Take a look at this one... a little stupid
    TaskModel().modify(task)
    task = TaskModel().get({'board_id': 1, 'task_id': 1})
    assert task.status == 'progress'
