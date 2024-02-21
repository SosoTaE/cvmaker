# built in
from datetime import datetime, timedelta
import json

# installed
from flask import request, Response
from bson.objectid import ObjectId



# written by me
from database.database import usersCollection
from message import Message
from Auth.password import verifyPassword
from Auth.jsonwebtoken import GenerateAccessAndRefreshTokens
from configs.config import accessTokenParams, refreshTokenParams

body_json_example = {
    "email": str,
    "password": str
}

def login():
    body = request.get_json()

    # user information
    email = body.get("email")
    password = body.get("password")
    createdAt = datetime.utcnow()

    # check if email is in database
    usersCollectionResponse = usersCollection.find_one({"email": email})

    # check if user exists
    if not usersCollectionResponse:
        message = json.dumps(Message("This user does not exist."))
        return Response(message, status=401, content_type="application/json")

    hashedPassword = usersCollectionResponse.get("password", "")

    # verify password
    if not verifyPassword(password, hashedPassword):
        message = json.dumps(Message("This password is incorrect."))
        return Response(message, status=401, content_type="application/json")

    # prepare parameters json to generate tokens
    json_for_token = {
        "_id": str(usersCollectionResponse.get("_id")),
        "email": email,
        'exp': datetime.utcnow() + timedelta(seconds=600)
    }
    accessTokenParameters = {
        "json": json_for_token,
    }
    accessTokenParameters.update(accessTokenParams)
    refreshTokenParameters = {
        "json": json_for_token,
    }
    refreshTokenParameters.update(refreshTokenParams)

    # generate tokens
    tokens = GenerateAccessAndRefreshTokens(accessTokenParameters, refreshTokenParameters)

    # update refresh tokens array
    update_query = {"$push": {"refreshTokens": tokens.get("refreshToken")}}

    # find user with id
    find_query = {"_id": ObjectId(usersCollectionResponse.get("_id"))}

    # update user document
    usersCollection.update_one(find_query, update_query)

    message = json.dumps(tokens)
    return Response(message, status=200, content_type="application/json")





