import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='joris123',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE edlerco")

print("Done!")
