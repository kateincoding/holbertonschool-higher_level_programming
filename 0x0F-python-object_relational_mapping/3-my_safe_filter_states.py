#!/usr/bin/python3
from sys import argv
import MySQLdb;

if __name__ == '__main__':
    try:
        db = MySQLdb.connect(host="localhost", port = 3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
        state = argv[4]
    except:
        print("Can't connect to database")
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    params = (state,)
    cur.execute(sql, params)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()
