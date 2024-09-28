# installed
from flask import Flask
from flask_cors import CORS

# written by me
from routes.registration import registration
from routes.login import login
from routes.refresh import refresh
from middlewares.verify import verifyAccessToken
from routes.getUniversities import getUniversities
from routes.getProfessions import getProfessions

app = Flask(__name__)

CORS(app, origins=["*"])


@app.route("/", methods=["GET", "OPTIONS"])
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

@app.route("/api/data/universities", methods=["GET"])
def GetUniversities():
    return getUniversities()

@app.route("/api/data/professions", methods=["GET"])
def GetProfessions():
    return getProfessions()

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
