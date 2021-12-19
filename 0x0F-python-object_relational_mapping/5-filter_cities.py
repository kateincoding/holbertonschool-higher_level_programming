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
    sql = """SELECT cities.name
          FROM cities JOIN states
          ON cities.state_id = states.id
          WHERE states.name = %s ORDER by cities.id ASC"""
    params = (state,)
    cur.execute(sql, params)
    query_rows = cur.fetchall()

    print(", ".join(row[0] for row in query_rows))
    cur.close()
    db.close()
