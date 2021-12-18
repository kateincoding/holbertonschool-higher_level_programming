#!/usr/bin/python3
from sys import argv
import MySQLdb;

if __name__ == '__main__':
    try:
        db = MySQLdb.connect(host="localhost", port = 3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    except:
        print("Can't connect to database")
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cur.execute(sql)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()