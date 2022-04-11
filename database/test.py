from multiprocessing import connection
from typing_extensions import Self
import mysql.connector
import time

def connectDatabase(username='root', password='Shiv@1991', database= 'test', host= '127.0.0.1'):
    cnx = mysql.connector.connect(user=username,password=password, host=host , database= database)
    cnx.autocommit = False
    return cnx

ctx = connectDatabase()
ctx.start_transaction(isolation_level = 'SERIALIZABLE')
cursor = ctx.cursor()
query = ("select * from student where id=10")
cursor.execute(query)

time.sleep(120)
for database in cursor:
    print(database)
cursor.close()
ctx.commit()
ctx.close()