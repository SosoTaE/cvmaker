# built in
from datetime import datetime, timedelta
import json

# installed
from flask import request, Response
from bson.objectid import ObjectId

# written by me
from Auth.jsonwebtoken import Validate, GenerateAccessAndRefreshTokens
from configs.config import refreshTokenParams, accessTokenParams
from message import Message
from database.database import usersCollection

routes_object = {
    "/registration": True,
    "/login": True,
    "/refresh": True,
    "/": True
}

def verifyAccessToken():
    if request.method == 'OPTIONS':
        # Construct a basic response for OPTIONS (CORS preflight)
        response = Response('', status=200)
        response.headers['Access-Control-Allow-Origin'] = '*'  # Or specify allowed origins
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response

    route = request.url_rule.rule

    if route in routes_object:
        return

    accessToken = request.headers.get("Authorization")

    if not accessToken:
        message = json.dumps(Message("There is no accessToken"))
        return Response(message, status=403, content_type="application/json")

    validationResponse = Validate(accessToken, **accessTokenParams)

    if not validationResponse.get("success"):
        message = json.dumps(Message(validationResponse.get("message",  "Access token is not valid.")))
        return Response(message, status=403, content_type="application/json")


