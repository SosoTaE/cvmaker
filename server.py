# installed
from flask import Flask

# written by me
from routes.registration import registration
from routes.login import login
from routes.refresh import refresh
from middlewares.verify import verifyAccessToken

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "<h1>Hello World</h1>"


@app.before_request
def VerifyAccessToken():
    return verifyAccessToken()


@app.route('/registration', methods=["POST"])
def Registration():
    return registration()


@app.route('/login', methods=["POST"])
def Login():
    return login()


@app.route('/refresh', methods=["POST"])
def Refresh():
    return refresh()


if __name__ == "__main__":
    app.run("0.0.0.0", 8000, threaded=True, debug=True)
