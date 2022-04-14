import os
from flask import Flask, request
from mysql.connector import connection

app = Flask(__name__)




DB_USER = os.getenv('DB_USER', default=None)
DB_PASSWORD = os.getenv('DB_PASSWORD', default=None)
DB_HOST = os.getenv('DB_HOST', default=None)
DB_PORT = int(os.getenv('DB_PORT', default=None))
DB_AUTOCOMMIT = eval(os.getenv('DB_AUTOCOMMIT', default=False))
DB_DATABASE = os.getenv('DB_DATABASE', default="test")

def getData(connect, tableName):
  querry = "select * from %s" %(tableName)
  connect.start_transaction(isolation_level="SERIALIZABLE")
  connect.connect()
  cursor = connect.cursor()
  cursor.execute(querry)
  if cursor.with_rows:
    for i in cursor:
      data = cursor.fetchall()
  connect.commit()
  connect.close()
  return data

def getConnectorObject():
    return connection.MySQLConnection(user=DB_USER,
                          password=DB_PASSWORD,
                          database=DB_DATABASE,
                          port=DB_PORT,
                          host=DB_HOST,
                          autocommit=DB_AUTOCOMMIT)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/movies')
def get_movies():
    cnx = getConnectorObject()

    return {
        "movies": getData(cnx, "Movie")
        }

@app.route('/cinemas')
def get_cinemas():
    return {
        "cinemas": ['Goteborg','stockholm']
    }


@app.route('/method')
def request_method():
    cnx = getConnectorObject()

    cnx.start_transaction()
    return request.method

