from lib.DBHandler import Scribe
from lib.models.BoardBaseModel import BoardBaseModel
from lib.DataClasses import Tag

class TagModel(BoardBaseModel):
    DATACLASS = Tag
    BASE_TABLE = 'board_tags'

    def create(self, name: str, description: str = ''):
        # Create dataclass and convert to dict
        tag = Tag(tag_name=name, board_id=self.board_id, description=description).dict()
        try:
            # Derive columns and values from dict
            columns, values = self.split(tag)
            id = self.db.insert('board_tags', columns, values)
            return id
        except Exception as e:
            print(e)
            # add logging at some point
            print("Unable to create tag")

    def exists(self, name: str):
        data = self.get({'tag_name': name})
        return True if data else False

    def modify(self, tag: Tag):
        conditions = [f"tag_id = '{tag.tag_id}'"]
        self.db.update('board_tags', tag.dict(), conditions)

    def create_new(self, name, description):
        exists = self.exists(name)
        if exists:
            raise NameError(f"Tag {name} for board {self.board_id} already exists")
        else:
            id = self.create(name, description)
            return id

    def delete(self, tag_id: int):
        values = {
            'tag_id': tag_id
        }
        conditions = ["tag_id = %(tag_id)s"]
        self.db.drop('board_tags', values, conditions)
