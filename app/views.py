from flask import render_template
import requests
import json
from requests.auth import HTTPBasicAuth
from app import app

@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():

    url = "http://localhost:5000/chrono_test/api/"
    tests = requests.get(url + "tests",
                         auth = HTTPBasicAuth(app.config['CURRENT_TOKEN'],""))

    # Check if token has expired or it hasn't been set to anything.
    if((app.config['CURRENT_TOKEN'] == None) or tests.status_code == 401):
        set_token()

    tests = requests.get(url + "tests",
                         auth = HTTPBasicAuth(app.config['CURRENT_TOKEN'],""))

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


@app.route('/tests/<test_name>')
@app.route('/tests/<test_name>/')
def test(test_name):

    url = "http://localhost:5000/chrono_test/api/tests/" + test_name
    tests = requests.get(url, auth = HTTPBasicAuth(app.config['CURRENT_TOKEN'], ""))

    # Check if token has expired
    if(tests.status_code == 401):
        set_token()

    title = 'Testing Infrastructure for Chrono'
    user = app.config['HELLO']

    if(tests.status_code == 200):
        return render_template('test_all.html',
            title = title,
            user = user,
            tests = tests.json())
    else:
        return render_template('test_all.html',
            title = title,
            user = "ERROR " + str(tests.status_code))

@app.route('/tests/t/<test_run>')
@app.route('/tests/t/<test_run>')
def test_run(test_run):

    


def set_token():
    url = "http://localhost:5000/chrono_test/api/"
    json_data = open(app.config['PATH'],'r')
    data = json.load(json_data)
    json_data.close()
    response = requests.get(url + "token",
                            auth = HTTPBasicAuth(data["username"], data["pw"]))
    app.config['CURRENT_TOKEN'] = response.json()['token']

