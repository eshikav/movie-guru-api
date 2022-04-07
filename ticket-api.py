from multiprocessing import connection
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import IntegrityError
from datetime import datetime
import json
import re

app = Flask(__name__)


@app.route("/seatList")
def home():
    file = open("home.json")
    x = json.load(file)
    return json.dumps(x)

@app.route("/reservedList", methods = ['POST', 'GET', 'DELETE'])
def reserved_list():
    if request.method == "GET":
          body = request.get_json()
          connection = mysql.connector.connect(user='root', password='centos',host='192.168.0.107', database='test')
          mycursor = connection.cursor()
          querry   = ("select seats from seatlayout where movie=%s and city=%s")
          mycursor.execute(querry,(body['movie'],body['city'],))
          reservedList = []
          [reservedList.extend(i[0].split(',')) for i in mycursor]
          return {
                 "status": "success",
                 "reservedList": reservedList
                 }

    elif  request.method == "POST":
      try:
          body = request.get_json()
          connection = mysql.connector.connect(user='root', password='centos',host='192.168.0.107', database='test')
          mycursor = connection.cursor()
          querry   = ("insert into seatlayout(city, movie,emailid,mobilenumber,name,seats) values(%s,%s,%s, %s,%s,%s)")
          mycursor.execute(querry,(body['city'],body['movie'],body['emailid'],body['mobilenumber'],body['name'],','.join(body['seats'])))
          connection.commit()
          ret_val = {
                       "Status": "Success",
                       "inserted_rows": mycursor.rowcount
                   }
          return ret_val
      except (IntegrityError):
          ret_val = {
                       "Status": "Error",
                       "inserted_rows": "Mobile number already in use"
                   }
          return ret_val
      except:
          ret_val = {
                       "Status": "Error",
                       "inserted_rows": "Error inserting the data"
                   }
          return ret_val

@app.route("/admin/reservedList", methods = ['POST', 'GET'])
def adminList():
    if request.method == "GET":
          body = request.get_json()
          connection = mysql.connector.connect(user='root', password='centos',host='192.168.0.107', database='test')
          mycursor = connection.cursor()
          querry   = ("select seats from seatlayout where movie=%s and city=%s")
          mycursor.execute(querry,(body['movie'],body['city'],))
          reservedList = []
          [reservedList.extend(i[0].split(',')) for i in mycursor]
          return {
                 "status": "success",
                 "reservedList": reservedList
                 }
    elif  request.method == "POST":
      try:
          body = request.get_json()
          connection = mysql.connector.connect(user='root', password='centos',host='192.168.0.107', database='test')
          mycursor = connection.cursor()
          querry   = ("insert into seatlayout(city, movie,emailid,mobilenumber,name,seats) values(%s,%s,%s, %s,%s,%s)")
          mycursor.execute(querry,(body['city'],body['movie'],body['emailid'],body['mobilenumber'],body['name'],','.join(body['seats'])))
          connection.commit()
          ret_val = {
                       "Status": "Success",
                       "inserted_rows": mycursor.rowcount
                   }
          return ret_val
      except (IntegrityError):
          ret_val = {
                       "Status": "Error",
                       "inserted_rows": "Mobile number already in use"
                   }
          return ret_val
      except:
          ret_val = {
                       "Status": "Error",
                       "inserted_rows": "Error inserting the data"
                   }
          return ret_val

@app.route("/movieList")
def movieList():
    #x = {"movies": ['BheemlaNayak', 'Acharya']}
    location = request.get_json()
    connection = mysql.connector.connect(user='root', password='centos',host='192.168.0.107', database='test')
    mycursor = connection.cursor()
    querry   = ("select moviename from movies where city = %s")
    mycursor.execute(querry,(location['city'],))
    movieList = {"movies": [i for i in mycursor]}
    return movieList




@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route("/v1/<name>")
def hello_where(name):
    x = {
        "name": name
    }
    x = json.dumps(x)
    return x

