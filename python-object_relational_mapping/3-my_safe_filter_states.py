#!/usr/bin/python3
"""Display states matching user input safely from SQL injection."""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name FROM states WHERE name LIKE BINARY %s "
        "ORDER BY id ASC",
        (sys.argv[4],),
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
