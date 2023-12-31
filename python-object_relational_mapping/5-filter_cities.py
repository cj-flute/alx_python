import MySQLdb as DB
import sys

user_name = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]
state_name = sys.argv[4]

db_connect = DB.connect(
    host='localhost',
    port=3306,
    user=user_name,
    passwd=password,
    db=db_name)


if __name__ == '__main__':
    db_cursor = db_connect.cursor()

    sql_query = "SELECT name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = %s) ORDER BY id ASC"

    db_cursor.execute(sql_query, (state_name,))

    row_sellected = db_cursor.fetchall()

    city_name = ', '.join([row[0] for row in row_sellected])
    print(city_name)

    db_connect.commit()
    db_cursor.close()
    db_connect.close()
