from dataclasses import dataclass, asdict
from datetime import datetime
from .Enums import StatusEnum
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
    name: str
    create_datetime: datetime = datetime.now()
    # These are not needed for creating new rows in the DB since we auto increment
    # Not sure how to handle this for now, so will just set the default to 0
    id: int = 0
    is_active: bool = True

@dataclass
class Task(BaseClass):
    title: str
    create_datetime: datetime
    description: str = ''
    status: StatusEnum = StatusEnum.TO_DO
    status_datetime: datetime = None
    board_id: int = 0
    task_id: int = 0
    tag_id: int = 1

@dataclass
class Tag(BaseClass):
    tag_name: str
    board_id: int = 0
    tag_id: int = 0
    description: str = ''

@dataclass
class Comment(BaseClass):
    task_id: int
    text: str
    created_datetime: datetime
    id: int = 0

# TODO: Will be set up for the board settings
@dataclass
class BoardConfig(BaseClass):
    user_id: int
    param_name: str
    param_value: str
    modify_datetime: datetime
