from mysql.connector import connection
import os

""" DB_USER = os.getenv('DATABASE_USER', default=None)
DB_PASSWORD = os.getenv('DATABASE_PASSWORD', default=None)
DB_HOST = os.getenv('DB_HOST', default=None)
DB_PORT = os.getenv('DB_PORT', default=None)
DB_AUTOCOMMIT = os.getenv('DB_AUTOCOMMIT', default=False)
DB_DATABASE = os.getenv('DB_DATABASE', default="test") """


DB_USER = 'root'
DB_PASSWORD = 'shiv@1991'
DB_HOST = '172.17.0.3'
DB_PORT = '3306'
DB_AUTOCOMMIT = False
DB_DATABASE = 'MovieGuru'

def getConnectorObject():
    return connection.MySQLConnection(user=DB_USER,
                          password=DB_PASSWORD,
                          database=DB_DATABASE,
                          port=DB_PORT,
                          host=DB_HOST,
                          autocommit=DB_AUTOCOMMIT)

cnx = getConnectorObject()
cnx.start_transaction(isolation_level="SERIALIZABLE")
cnx.connect()
cursor = cnx.cursor()
cursor.execute("select * from Movie where MovieId=1")
for i in cursor:
  print(i)

cnx.commit()
cnx.close()
