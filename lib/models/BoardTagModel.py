from lib.DBHandler import Scribe
from lib.models.BaseModel import BaseModel
from lib.DataClasses import Tag

class BoardTagModel(BaseModel):

    def __init__(self):
        super().__init__()
        self.db = Scribe()

    def create(self, board_id: int, name: str, description: str):
        # Create dataclass and convert to dict
        tag = Tag(board_id, name, description).dict()
        try:
            # Derive columns and values from dict
            columns, values = self.split(tag)
            id = self.db.insert('board_tags', columns, values)
            return id
        except:
            # add logging at some point
            print("Unable to create tag")

    def exists(self, name: str):
        data = self.get({'name': name})
        return True if data else False

    def get(self, search_term: dict):
        tag = self.db.read('board_tags', search_term)
        if not tag:
            return None
        else:
            tag = self.sanitize(tag, Tag.headers())
            return Tag(**tag)

    def modify(self, tag: Tag):
        conditions = [f"name = '{tag.name}'"]
        self.db.update('board_tags', tag.dict(), conditions)

    def create_new(self, name: str, is_unilateral: bool, is_bodyweight: bool, details: dict):
        exists = self.exists(name)
        if exists:
            raise NameError(f"Tag {name} already exists")
        else:
            id = self.create(name, is_unilateral, is_bodyweight, details)
            return id

    def delete(self, name: str):
        values = {
            'name': name
        }
        conditions = ["name = %(name)s"]
        self.db.drop('board_tags', values, conditions)
