# built in
from datetime import datetime, timedelta
import json

# installed
from flask import request, Response
from bson.objectid import ObjectId

# written by me
from Auth.jsonwebtoken import Validate
from configs.config import accessTokenParams
from database.database import database


def get_cvs():
    accessToken = request.headers.get("Authorization")

    validationResponse = Validate(accessToken, **accessTokenParams)

    data = validationResponse.get("data")

    _id = data.get("_id")

    collection = database.get_collection(_id)

    collection_response = collection.find({})

    cvs = list(collection_response)

    for each in cvs:
        each.pop("_id")

    return Response(json.dumps({"data": cvs}), mimetype="application/json")