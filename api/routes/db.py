import sqlite3

def inputDB(param):
    con = sqlite3.connect('db/main.db')
    cur = con.cursor()

    cur.execute(f"INSERT INTO main Values({param['filename'], param['file'], param['version'], param['date']})")