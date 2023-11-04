import MySQLdb as DB
import sys

user_name = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]


db_connect = DB.connect(
    host='localhost',
    port=3306,
    user=user_name,
    passwd=password,
    db=db_name)


if __name__ == '__main__':
    db_cursor = db_connect.cursor()

    sql_query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"

    db_cursor.execute(sql_query)

    row_sellected = db_cursor.fetchall()

    for row in row_sellected:
        print(row)

    db_connect.commit()
    db_cursor.close()
    db_connect.close()
