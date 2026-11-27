#!/usr/bin/python3
"""Display states matching user input using format, sorted by states.id."""
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
    query = (
        "SELECT id, name FROM states WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC".format(sys.argv[4])
    )
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
