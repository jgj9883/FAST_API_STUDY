import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)

con = sqlite3.connect("test.db", isolation_level=None) # db 생성(Auto Commit)
cur = con.cursor()

con.execute("CREATE TABLE IF NOT EXISTS user_info (id integer primary key, ide text, password text )")

def sql_insert() :
    try :
        cur.execute("INSERT INTO user_info Values( 1, 'kyubin','1234')")
    except :
        print("Insert 오류")

def sql_select(user_id):
    try :
        cur.execute("SELECT password FROM user_info where ide = '%s'" % user_id)
        value = cur.fetchall()
        if value == [] :
            return None

        return value[0][0]
    except :
        print("Select 오류")
