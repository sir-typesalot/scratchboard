from lib.models.BoardBaseModel import BoardBaseModel
from lib.DataClasses import Task

class TaskModel(BoardBaseModel):
    DATACLASS = Task
    BASE_TABLE = 'board_tasks'

    def create(self, title: str, description: str='', tag_id: int=1, status: str='todo'):
        # Create dataclass and convert to dict
        task = Task(
            board_id=self.board_id,
            tag_id=tag_id,
            title=title,
            description=description,
            status=status
        ).dict()
        try:
            # Derive columns and values from dict
            columns, values = self.split(task)
            print(columns)
            print(values)
            id = self.db.insert('board_tasks', columns, values)
            return id
        except Exception as e:
            print(e)
            # add logging at some point
            print("Unable to create task")

    def exists(self, name: str):
        data = self.get({'tag_name': name, 'board_id': self.board_id})
        return True if data else False

    def modify(self, task: Task):
        conditions = [f"task_id = '{task.task_id}'"]
        self.db.update('board_tasks', task.dict(), conditions)

    def delete(self, task_id: int):
        values = {
            'task_id': task_id
        }
        conditions = ["task_id = %(task_id)s"]
        self.db.drop('board_tasks', values, conditions)
