import os
import contextlib
import mysql.connector
from dotenv import load_dotenv

class DB(object):

    def __init__(self, db='scratchboard'):
        self.db = db

    @contextlib.contextmanager
    def db_connect(self, cur_type=None):
        load_dotenv()
        if os.environ.get('ENV') == 'live':
            config = {
                "host": os.environ.get('LIVE_HOST'),
                "user": os.environ.get('LIVE_USER'),
                "passwd": os.environ.get('LIVE_PASS'),
                "database": self.db
            }
        else:
            config = {
                "host": os.environ.get('LOCAL_HOST'),
                "user": os.environ.get('LOCAL_USER'),
                "passwd": os.environ.get('LOCAL_PASS'),
                "database": self.db
            }

        cnx = mysql.connector.MySQLConnection(**config)

        if cur_type == 'dict':
            cursor = cnx.cursor(dictionary=True, buffered=True)
        else:
            cursor = cnx.cursor(buffered=True)

        try:
            yield cursor
        finally:
            cnx.commit()
            cursor.close()
            cnx.close()
