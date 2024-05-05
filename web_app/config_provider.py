
import sqlite3 as sq

class Singltone(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def get_instance(cls):
        return cls()

    def __init__(self) -> None:
        self.nav_links = []
    
    def set_nav_link(self, name, link='#'):
        self.nav_links.append({
            'name' : name,
            'link' : link
        })
    
    def connect_to_db_1(self):
        '''
        Connects to DB
        '''
        with sq.connect("test.db") as connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS irregular_verbs (
                    verb_id INTEGER PRIMARY KEY,
                    treanslation TEXT NOT NULL,
                    verb1 TEXT NOT NULL,
                    verb2 TEXT NOT NULL,
                    verb3 TEXT NOT NULL
            )''')

    def connect_to_db(self):
        '''
        Connects to DB
        '''
        connection = sq.connect("test.db")
        cursor = connection.cursor()
        return cursor