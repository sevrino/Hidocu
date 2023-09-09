import sqlite3

con = sqlite3.connect('db/main.db')
cur = con.cursor()

cur.execute("CREATE TABLE main (filename TEXT NOT NULL, file TEXT NOT NULL, version	TEXT NOT NULL, date INTEGER NOT NULL)")

print("설정완료")