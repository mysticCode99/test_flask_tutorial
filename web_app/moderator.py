
from config_provider import Singltone

class Moderator(object):
    def __init__(self) -> None:
        self.singltone = Singltone()

    def insert_data(self, table_name, **kwargs) -> None:
        '''
        Adds data to data base
        '''
        cursor = self.singltone.connect_to_db()
        col_names = ''
        values = ''
        for var_name, value in kwargs.items():
            col_names += f'{var_name},'
            values += f'{value},'
        print(f'''
                INSERT INTO {table_name} ({col_names.strip(',')})
                VALUES ( {values.strip(',')} )
            ''')
        try:
            cursor.execute(f'''
                INSERT INTO {table_name} ({col_names.strip(',')})
                VALUES ( {values.strip(',')} )
            ''')
        except:
            pass
        cursor.close()

if __name__ == '__main__':
    print(__name__)
    Moderator()