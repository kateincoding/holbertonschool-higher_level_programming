#!/usr/bin/python3
"""
script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    sql = """SELECT * FROM states
          WHERE name LIKE 'N%'
          ORDER BY states.id ASC"""
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        if 'N' == row[1][0]:
            print(row)
    cur.close()
    db.close()
