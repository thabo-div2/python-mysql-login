import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="Grimmijow06",
    database="Hospital"
)

cursor = db.cursor()

cursor.execute("DESC login")

print(cursor.fetchall())
