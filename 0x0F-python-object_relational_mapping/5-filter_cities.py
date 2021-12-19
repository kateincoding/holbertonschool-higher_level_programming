#!/usr/bin/python3
""" script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa """


from sys import argv
import MySQLdb
"""script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    state = argv[4]
    cur = db.cursor()
    sql = """SELECT cities.id, cities.name
          FROM cities LEFT JOIN states
          ON cities.state_id = states.id
          WHERE states.name = %s ORDER by id ASC"""
    params = (state,)
    cur.execute(sql, params)
    query_rows = cur.fetchall()

    for row in query_rows:
        if row != query_rows[-1]:
            print(row[1], end=", ")
        else:
            print(row[1])
    cur.close()
    db.close()
