from .conftest import get_db

def populate_boards():
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO boards (hash, name, is_active) VALUES
            ('04bda9501c4b88cae4643821a47f33670e553bed1222dbf6edc24e35', 'Test Project', 1)
        """)

def populate_tags():
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO board_tags (board_id, tag_name, description) VALUES
            (1, 'TestTag', 'Test the description')
        """)

def populate_tasks():
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO board_tasks
            (board_id, tag_id, title, description) VALUES
            (1, 1, 'Test Title', 'Something here'),
            (1, 1, 'Test Title 2', 'Something more over here')
        """)

def populate_comments():
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO task_comments (task_id, text) VALUES
            (1, 'Must test how this is created'),
            (2, 'Will have to add some more text here')
        """)

table_map = {
    'boards': populate_boards,
    'tags': populate_tags,
    'exercises': populate_tasks,
    'routine_map': populate_comments
}
def populate_tables(tables: list):
    for table in tables:
        table_map[table]()
