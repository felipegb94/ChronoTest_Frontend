from flask import render_template
import requests
import json
from requests.auth import HTTPBasicAuth
from app import app

@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():

    title = 'Testing Infrastructure for Chrono'
    url = app.config['BACKEND_URL']
    tests = requests.get(url + "tests",
                         auth = HTTPBasicAuth(app.config['CURRENT_TOKEN'],""))

    # Check if token has expired or it hasn't been set to anything.
    if((app.config['CURRENT_TOKEN'] == None) or tests.status_code == 401):
        response = set_token()
        if(response.status_code == 401):
            return render_template('index.html', title = "ERROR " + str(tests.status_code) + ": Failed login")

    tests = requests.get(url + "tests",
                         auth = HTTPBasicAuth(app.config['CURRENT_TOKEN'],""))


    if(tests.status_code == 200):
        return render_template('index.html',
            title = title,
            user = "",
            tests = tests.json())
    else:
        return render_template('index.html',
            title = "ERROR " + str(tests.status_code)  + ": Failed login")


@app.route('/tests/<test_name>')
@app.route('/tests/<test_name>/')
def test(test_name):
    title = 'Testing Infrastructure for Chrono'
    url = app.config['BACKEND_URL'] + 'tests/' + test_name
    tests = requests.get(url, auth = HTTPBasicAuth(app.config['CURRENT_TOKEN'], ""))

    # Check if token has expired
    if(tests.status_code == 401):
        response = set_token()
        if(response.status_code == 401):
            return render_template('index.html', title = "ERROR " + str(tests.status_code) + ": Failed login")

    tests = requests.get(url, auth = HTTPBasicAuth(app.config['CURRENT_TOKEN'], ""))

    if(tests.status_code == 200):
        return render_template('test_all.html',
            title = title,
            user = "",
            tests = tests.json())
    else:
        return render_template('test_all.html',
            title = "ERROR " + str(tests.status_code))
    

def set_token():
    url = app.config['BACKEND_URL']
    json_data = open(app.config['PATH'],'r')
    data = json.load(json_data)
    json_data.close()
    response = requests.get(url + "token",
                            auth = HTTPBasicAuth(data["username"], data["pw"]))
    if(response.status_code == 401):
        return response
    else:
        app.config['CURRENT_TOKEN'] = response.json()['token']
        return response


