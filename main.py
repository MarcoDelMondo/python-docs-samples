
from flask import Flask
import os
from google.cloud import datastore

app = Flask(__name__)

dataclient = datastore.Client()

def addVisitor():
    ent = dataclient.key('data', 'visitors')
    total = dataclient.get(key=ent)
    if total:
        total['total'] += 1
        dataclient.put(total)
    else:
        total = datastore.Entity(key=ent)
        total['total'] = 0
        dataclient.put(total)
@app.route('/visitors')
def getVisitor():
    addVisitor()
    ent = dataclient.key('data', 'visitors')
    total = dataclient.get(key=ent)
    if total:
        return 'Total visitors: ' + str(total['total'])
    else:
        return 'Total Broke!'

@app.route('/about')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hi Fritter hope all is well! Ben Carrier 300290267'

@app.route('/version')
def VersA():
    return 'This is app version B!'

@app.route('/instance')
def getid():
    instanceid = os.getenv('GAE_INSTANCE')
    return str(instanceid)

@app.route('/version-id')
def getversionid():
    addVisitor()
    versionid = os.getenv('GAE_VERSION')
    return str(versionid)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
