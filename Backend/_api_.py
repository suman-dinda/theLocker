from connection import dbConnect
from authentication import signup, signin
from flask import Flask, request, redirect, url_for
import json
app = Flask(__name__)

conn = dbConnect.connection("connection","config/dbSettings.json")
dbObj = conn[1]
dbName = conn[0]
dblist = dbObj.list_database_names()

@app.route('/api/register')
def hello_world():
    if dbName in dblist:
        print(dbObj.list_database_names())
        _full_name = request.form['full_name']
        _email = request.form['email']
        _password = request.form['password']
        response = signup(_full_name,_email,_password)
        return response

@app.route('/api/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      _email = request.form['email']
      _password = request.form['password']
      response = signin(_email,_password)
      response = str(response)
      print(response)
      return app.response_class(response, content_type='application/json')
   else:
      return json.dumps("{\"response\":200, \"Message\": \"No request allowed\"}")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)