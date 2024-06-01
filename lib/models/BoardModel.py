from lib.DBHandler import Scribe
from lib.models.BaseModel import BaseModel
from lib.DataClasses import Board
import hashlib

class BoardModel(BaseModel):

    def __init__(self):
        super().__init__()
        self.db = Scribe()

    def create(self, seed: str, name: str, is_active: bool = True):
        # Convert seed into SHA224 hash
        hash = BoardModel.generate_hash(seed)
        # Create dataclass and convert to dict
        tag = Board(hash=hash, name=name, is_active=is_active).dict()
        try:
            # Derive columns and values from dict
            columns, values = self.split(tag)
            id = self.db.insert('boards', columns, values)
            return id
        except:
            # TODO: add logging at some point
            print("Unable to create board")

    def exists(self, hash: str):
        data = self.get({'hash': hash})
        return True if data else False

    def get(self, search_term: dict):
        board = self.db.read('boards', search_term)
        if not board:
            return None
        else:
            exercise = self.sanitize(exercise, Board.headers())
            return Board(**exercise)

    def modify(self, board: Board):
        conditions = [f"hash = '{board.hash}'"]
        self.db.update('boards', board.dict(), conditions)

    def create_new(self, seed: str, name: str):
        hash = BoardModel.generate_hash(seed)
        exists = self.exists(hash)
        if exists:
            raise NameError(f"Board hash: {hash} already exists")
        else:
            id = self.create(hash, name)
            return id

    def delete(self, hash: str):
        values = {
            'hash': hash
        }
        conditions = ["hash = %(hash)s"]
        self.db.drop('boards', values, conditions)

    @classmethod
    def generate_hash(cls, seed: str):
        buffer = bytes(seed, 'utf-8')
        return hashlib.sha256(buffer).hexdigest()