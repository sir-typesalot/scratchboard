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
    id: int
    name: str
    is_active: bool
    create_datetime: datetime

@dataclass
class Task(BaseClass):
    board_id: int
    task_id: int
    tag_id: int
    title: str
    description: str
    status: StatusEnum
    create_datetime: datetime
    status_datetime: datetime

@dataclass
class Tag(BaseClass):
    board_id: int
    tag_id: int
    tag_name: str
    description: str

# TODO: Will be set up for the board settings
@dataclass
class BoardConfig(BaseClass):
    user_id: int
    param_name: str
    param_value: str
    modify_datetime: datetime
