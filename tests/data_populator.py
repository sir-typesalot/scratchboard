from .conftest import get_db

def populate_boards():
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO boards (hash, name, is_active) VALUES
            ('164b2551025f1ed0261a33febdd5d75435c987de8854f2b1cda909c0', 'Test Project', 1)
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
            (board_id, tag_id, title, description, status, status_datetime) VALUES
            (1, 1, 'Test Title', 'Something here', 'todo', '2024-06-02 19:30:26'),
            (1, 1, 'Test Title 2', 'Something more over here', 'progress', '2024-06-02 19:30:26')
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
    'board_tags': populate_tags,
    'board_tasks': populate_tasks,
    'task_comments': populate_comments
}
def populate_tables(tables: list):
    for table in tables:
        table_map[table]()
