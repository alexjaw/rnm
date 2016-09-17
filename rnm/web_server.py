from flask import Flask

from rnm import NetworkConnection

app = Flask(__name__)

@app.route('/')
def index():
    return  '<h1>Hello, my IP is ' + str(rnm.get_ip()) + '</h1>'


if __name__ == '__main__':
    rnm = NetworkConnection()
    app.run(host='0.0.0.0')
