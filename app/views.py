from flask import render_template
import requests
import json
from requests.auth import HTTPBasicAuth
from app import app



@app.route('/')
@app.route('/index')
def index():

    json_data = open(app.config['PATH'],'r')
    data = json.load(json_data)
    json_data.close()

    tests = requests.get("http://localhost:5000/chrono_test/api/tests/benchmark_ChBody",
        auth = HTTPBasicAuth(data["username"], data["pw"]))

    title = 'Testing Infrastructure for Chrono'
    user = app.config['HELLO']

    if(tests.status_code == 200):
        return render_template('index.html',
            title = title,
            user = user,
            tests = tests.json())
    else:
        return render_template('index.html',
            title = title,
            user = "ERROR " + str(tests.status_code))


