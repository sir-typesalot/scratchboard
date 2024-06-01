from dataclasses import dataclass, asdict
from datetime import datetime
from Enums import StatusEnum
import json

# TypedDict might be an option if perf is too slow
class BaseClass:

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}

    def format_datetime(self, datetime: datetime):
        return datetime.strftime("%m/%d/%Y %H:%M")

    def to_json(self, field: dict):
        return json.dumps(field)

    @classmethod
    def headers(cls):
        return list(cls.__annotations__.keys())

@dataclass
class Board(BaseClass):
    hash: str
    # These are not needed for creating new rows in the DB since we auto increment
    # Not sure how to handle this for now, so will just set the default to 0
    id: int = 0
    name: str
    is_active: bool = True
    create_datetime: datetime

@dataclass
class Task(BaseClass):
    board_id: int = 0
    task_id: int = 0
    tag_id: int = 1
    title: str
    description: str = ''
    status: StatusEnum
    create_datetime: datetime
    status_datetime: datetime = None

@dataclass
class Tag(BaseClass):
    board_id: int = 0
    tag_id: int = 0
    tag_name: str
    description: str = ''

@dataclass
class Comment(BaseClass):
    id: int = 0
    task_id: int
    text: str
    created_datetime: datetime

# TODO: Will be set up for the board settings
@dataclass
class BoardConfig(BaseClass):
    user_id: int
    param_name: str
    param_value: str
    modify_datetime: datetime
