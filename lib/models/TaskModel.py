from lib.DBHandler import Scribe
from lib.models.BaseModel import BaseModel
from lib.DataClasses import Task

class TaskModel(BaseModel):

    def __init__(self):
        super().__init__()
        self.db = Scribe()

    def create(self, board_id: int, title: str, description: str = '', tag_id: int = 1):
        # Create dataclass and convert to dict
        task = Task(
            board_id=board_id,
            tag_id=tag_id,
            title=title,
            description=description
        ).dict()
        try:
            # Derive columns and values from dict
            columns, values = self.split(task)
            id = self.db.insert('board_tasks', columns, values)
            return id
        except Exception as e:
            print(e)
            # add logging at some point
            print("Unable to create task")

    def exists(self, name: str, board_id: int):
        data = self.get({'tag_name': name, 'board_id': board_id})
        return True if data else False

    def get(self, search_term: dict):
        task = self.db.read('board_tasks', search_term)
        if not task:
            return None
        else:
            task = self.sanitize(task, Task.headers())
            return Task(**task)

    def modify(self, task: Task):
        conditions = [f"task_id = '{task.task_id}'"]
        self.db.update('board_tasks', task.dict(), conditions)

    def delete(self, task_id: int):
        values = {
            'task_id': task_id
        }
        conditions = ["task_id = %(task_id)s"]
        self.db.drop('board_tasks', values, conditions)
