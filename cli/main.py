from flask import Flask

app = Flask(__name__, static_folder='templates')

@app.route('/')
def index():
    return app.send_static_file('index.html')

def goLive(runArgs):
    app.run(host=runArgs['host'], port=runArgs['port'])
