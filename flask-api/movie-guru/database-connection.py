from mysql.connector import connection
import os

DB_USER = os.getenv('DATABASE_USER', default=None)
DB_PASSWORD = os.getenv('DATABASE_PASSWORD', default=None)
DB_HOST = os.getenv('DB_HOST', default=None)
DB_PORT = int(os.getenv('DB_PORT', default=None))
DB_AUTOCOMMIT = eval(os.getenv('DB_AUTOCOMMIT', default=False))
DB_DATABASE = os.getenv('DB_DATABASE', default="test")

def getData(connect, tableName):
  querry = "select * from %s" %(tableName)
  connect.start_transaction(isolation_level="SERIALIZABLE")
  connect.connect()
  cursor = cnx.cursor()
  cursor.execute(querry)
  if cursor.with_rows:
    for i in cursor:
      print(i)
  cnx.commit()
  cnx.close()


def getConnectorObject():
    return connection.MySQLConnection(user=DB_USER,
                          password=DB_PASSWORD,
                          database=DB_DATABASE,
                          port=DB_PORT,
                          host=DB_HOST,
                          autocommit=DB_AUTOCOMMIT)

cnx = getConnectorObject()

getData(cnx, "Movie")