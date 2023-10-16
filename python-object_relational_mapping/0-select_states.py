import MySQLdb as DB
# from flask_sqlalchemy import SQLAlchemy

db_connect = DB.connect(host='localhost', port=3306,
                        user='root', passwd='mummysdaycjflute', db='cj')

db_cursor = db_connect.cursor()

db_cursor.execute("CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;")
db_cursor.execute("USE hbtn_0e_0_usa;")
db_cursor.execute(
    """CREATE TABLE IF NOT EXISTS states(
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id)
    )"""
)

states = ("Arizona", "Califonia", "Neveda", "New york", "Texas")

for state in states:
    db_cursor.execute("INSERT INTO states (name) VALUES (%s)", [state])

db_connect.commit()
db_cursor.close()

# db_cursor.execute("INSERT INTO states ()")
