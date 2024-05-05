
import sqlite3 as sq

def attemp_1():
    ''' It's not secure to use execute command directly'''
    connection = sq.connect("test.db")
    cursor = connection.cursor()
    cursor.execute('')
    connection.close()


def create_db():
    ''' It's not secure to use execute command directly'''
    # DB table format
    # translation v1 v2 v3
    # repeat count
    # correctness count
    # word_id for random choose

    with sq.connect("test.db") as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS irregular_verbs (
                treanslation TEXT NOT NULL,
                verb1 TEXT NOT NULL PRIMARY KEY,
                verb2 TEXT NOT NULL,
                verb3 TEXT NOT NULL
        )''')

def destroy_db():
    with sq.connect("test.db") as connection:
        cursor = connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS irregular_verbs')

def insert_data():
    verbs_insert_list = [
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "be", "was/were", "been") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "become", "became", "become") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "begin", "began", "begun") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "break", "broke", "broken") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "bring", "brought", "brought") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "build", "built", "built") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "buy", "bought", "bought") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "catch", "caught", "caught") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "choose", "chose", "chosen") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "come", "came", "come") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "cost", "cost", "cost") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "cut", "cut", "cut") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "do", "did", "done") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "draw", "drew", "drawn") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "drink", "drank", "drunk") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "eat", "ate", "eaten") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "fall", "fell", "fallen") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "find", "found", "found") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "fly", "flew", "flown") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "forget", "forgot", "forgotten") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "give", "gave", "given") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "go", "went", "gone") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "grow", "grew", "grown") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "have", "had", "had") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "hear", "heard", "heard") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "hold", "held", "held") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "keep", "kept", "kept") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "know", "knew", "known") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "leave", "left", "left") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "lose", "lost", "lost") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "make", "made", "made") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "mean", "meant", "meant") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "meet", "met", "met") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "pay", "paid", "paid") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "put", "put", "put") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "read", "read", "read") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "ride", "rode", "ridden") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "ring", "rang", "rung") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "run", "ran", "run") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "say", "said", "said") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "see", "saw", "seen") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "sell", "sold", "sold") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "send", "sent", "sent") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "set", "set", "set") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "sing", "sang", "sung") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "sink", "sank", "sunk") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "sleep", "slept", "slept") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "speak", "spoke", "spoken") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "spend", "spent", "spent") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "stand", "stood", "stood") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "steal", "stole", "stolen") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "swim", "swam", "swum") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "take", "took", "taken") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "teach", "taught", "taught") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "tell", "told", "told") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "think", "thought", "thought") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "throw", "threw", "thrown") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "understand", "understood", "understood") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "wear", "wore", "worn") ''', 
        ''' INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3) VALUES ("", "write", "wrote", "written") ''', 
    ]
    # get | got | gotten (American English) / got (British English)
    # learn | learned (American English) / learnt (British English) | learned (American English) / learnt (British English)
    # wake | woke | woken (British English) / waked (American English)

    with sq.connect("test.db") as connection:
        cursor = connection.cursor()
        for insert_cmd in  verbs_insert_list:
            cursor.execute(insert_cmd)
        # cursor.execute('''
        #     INSERT INTO irregular_verbs (treanslation, verb1, verb2, verb3)
        #     VALUES ( "զարթնել", "awake", "awoke", "awoken" )
        # ''')

def get_data():
    with sq.connect("test.db") as connection:
        cursor = connection.cursor()
        # cursor.execute('SELECT * FROM irregular_verbs')
        res = cursor.fetchall()
        print(res)

def update_data():
    with sq.connect("test.db") as connection:
        cursor = connection.cursor()
        cursor.execute('''
        UPDATE irregular_verbs SET translation = 'linel' WHERE verb1 = 'be'
        ''')
    
def delete_data():
    with sq.connect("test.db") as connection:
        cursor = connection.cursor()
        cursor.execute('''
        DELETE FROM irregular_verbs SET translation = 'linel' WHERE verb1 = 'be'
        ''')

if __name__ == '__main__':
    # create_db()
    # insert_data()
    get_data()
    pass