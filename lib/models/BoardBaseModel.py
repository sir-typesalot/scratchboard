from .BoardModel import BoardModel
from .BaseModel import BaseModel

class BoardBaseModel(BaseModel):
    DATACLASS = None
    BASE_TABLE = None

    def __init__(self, board_hash):
        board = BoardModel().get({'hash': board_hash})
        self.board_id = board.id if board else None
        super().__init__()

    def get(self, search_term: dict={}, fetchone=False):
        # Use board_id as default
        search_term['board_id'] = self.board_id
        results = []

        data = self.db.read(self.BASE_TABLE, search_term)
        for row in data:
            results.append(self.convert_to_class(row))

        if not results:
            # Return this since it would be an empty list anyways
            return results
        return results if not fetchone else results[0]

    def convert_to_class(self, data_dict):
        if not data_dict:
            return None
        else:
            dataclass = self.sanitize(data_dict, self.DATACLASS.headers())
            return self.DATACLASS(**dataclass)
