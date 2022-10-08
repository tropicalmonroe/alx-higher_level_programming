#!/usr/bin/python3
"""all states with a name with N (upper N) from database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""
    SELECT id, name
    FROM states
    WHERE name LIKE BINARY'N%'
    ORDER BY id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
