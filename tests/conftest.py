import pytest
from lib.db import DB
from app.config import Config

def get_db():
    Config.SCHEMA = '_test_db'
    db = DB(Config.SCHEMA).db_connect
    return db()

@pytest.fixture
def db():
    Config.SCHEMA = '_test_db'
    yield
    # Until tables are created, keep hidden
    # tables = ['boards', 'board_tags', 'board_tasks', 'task_comments']
    tables = ['boards']
    with get_db() as cursor:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        for table in tables:
            cursor.execute(f"TRUNCATE TABLE {table}")
            cursor.execute(f"ALTER TABLE {table} AUTO_INCREMENT = 1")
