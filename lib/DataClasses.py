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
    # TODO: is_active not in use
    id: int = 0
    is_active: bool = True

@dataclass
class Task(BaseClass):
    title: str
    description: str = ''
    # TODO: currently hard coded to hade TO_DO value, need to make it responsive to current swimlane
    status: StatusEnum = StatusEnum.TO_DO.value
    status_datetime: datetime = datetime.now()
    create_datetime: datetime = datetime.now()
    board_id: int = 0
    task_id: int = 0
    tag_id: int = 1

@dataclass
class Tag(BaseClass):
    tag_name: str
    board_id: int = 0
    tag_id: int = 0
    # TODO: set up hex value to tag

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
