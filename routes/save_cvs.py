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
from database.database import database


def save_cvs():
    body = request.get_json()

    accessToken = request.headers.get("Authorization")
    validationResponse = Validate(accessToken, **accessTokenParams)

    data = validationResponse.get("data")
    _id = data.get("_id")

    collection = database.get_collection(_id)
    collection.insert_one(body)

    return Response(json.dumps({"message": "data saved successfully"}), mimetype="application/json")