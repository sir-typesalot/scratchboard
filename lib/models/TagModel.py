from lib.DBHandler import Scribe
from lib.models.BaseModel import BaseModel
from lib.DataClasses import Tag

class TagModel(BaseModel):

    def __init__(self):
        super().__init__()
        self.db = Scribe()

    def create(self, name: str, board_id: int = 0, description: str = ''):
        # Create dataclass and convert to dict
        tag = Tag(tag_name=name, board_id=board_id, description=description).dict()
        try:
            # Derive columns and values from dict
            columns, values = self.split(tag)
            id = self.db.insert('board_tags', columns, values)
            return id
        except Exception as e:
            print(e)
            # add logging at some point
            print("Unable to create tag")

    def exists(self, name: str, board_id: int):
        data = self.get({'tag_name': name, 'board_id': board_id})
        return True if data else False

    def get(self, search_term: dict):
        tag = self.db.read('board_tags', search_term)
        if not tag:
            return None
        else:
            tag = self.sanitize(tag, Tag.headers())
            return Tag(**tag)

    def modify(self, tag: Tag):
        conditions = [f"tag_id = '{tag.tag_id}'"]
        self.db.update('board_tags', tag.dict(), conditions)

    def create_new(self, board_id, name, description):
        exists = self.exists(name, board_id)
        if exists:
            raise NameError(f"Tag {name} for board {board_id} already exists")
        else:
            id = self.create(name, board_id, description)
            return id

    def delete(self, tag_id: int):
        values = {
            'tag_id': tag_id
        }
        conditions = ["tag_id = %(tag_id)s"]
        self.db.drop('board_tags', values, conditions)
