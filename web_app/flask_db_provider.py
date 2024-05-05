
import sqlite3

class FBG_Provider():
    def __init__(self, db) -> None:
        self.__db = db
        self.__cur = db.cursor()
    
    def getMenu(self):
        sql_cmd = '''SELECT * FROM irregular_verbs'''
        try:
            self.__cur.execute(sql_cmd)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print('Error: wrong sql querry')
        return []
    
    def addPost(self, t:str, v1:str, v2:str, v3:str):
        sql_cmd = 'INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("{}", "{}", "{}", "{}")'
        try:
            self.__cur.execute(sql_cmd.format(t, v1, v2, v3))
            self.__db.commit()
            return True
        except sqlite3.Error as e:
            return False