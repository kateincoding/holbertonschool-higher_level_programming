#!/usr/bin/python3
from sys import argv
import MySQLdb;

def mysqlconnect():
    try:
        db = MySQLdb.connect(host="localhost", port = 3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    except:
        print("Can't connect to database")
        return 0
    print("Connected")
    cur = db.cursor()
    cur.close()
    db.close()

mysqlconnect()
