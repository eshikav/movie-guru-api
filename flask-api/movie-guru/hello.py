from flask import Flask, request

app = Flask(__name__)


import os

DB_USER = os.getenv('DATABASE_USER', default=None)
DB_PASSWORD = os.getenv('DATABASE_PASSWORD', default=None)
DB_HOST = os.getenv('DB_HOST', default=None)
DB_PORT = os.getenv('DB_PORT', default=None)
DB_AUTOCOMMIT = os.getenv('DB_AUTOCOMMIT', default=False)
DB_DATABASE = os.getenv('DB_DATABASE', default="test")


def getConnectorObject():
    return MySQLConection(user=DB_USER,
                          password=DB_PASSWORD,
                          database=DB_DATABASE,
                          port=DB_PORT,
                          host=DB_HOST,
                          autocommit=DB_AUTOCOMMIT)

def getMovies(cnx, table):
   query = "SELECT * from %s"
   cnx.connect()
   cnx.start_transaction(isolation_level='SERIALIZABLE')
   cursor = cnx.cursor()
   result = cursor.execute(query)
   if result.with_rows:
       result = result.fetchall()
   return result

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/movies')
def get_movies():
    return {
        "movies": ['sarkarvaripata','beemlanayak']
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

