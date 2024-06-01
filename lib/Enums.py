from enum import Enum

class StatusEnum(Enum):
    TO_DO = "todo"
    IN_PROGRESS = "progress"
    DONE = "done"

    @classmethod
    def has_member_key(cls, key):
        return key in cls.__members__

    @classmethod
    def get_member_key(cls, key):
        key = StatusEnum[key].value if cls.has_member_key(key) else None
        if key:
            return key
        else:
            return False
