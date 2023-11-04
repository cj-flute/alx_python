import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password, db=database_name)

    cur = db.cursor()

    sql_query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    cur.execute(sql_query)

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
