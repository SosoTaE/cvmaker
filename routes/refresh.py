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


def refresh():
    body = request.get_json()

    refreshToken = body.get("refreshToken")

    refreshTokenValidationParameters = {
        "token": refreshToken
    }

    refreshTokenValidationParameters.update(refreshTokenParams)

    validationResponse = Validate(**refreshTokenValidationParameters)

    if not validationResponse.get("success"):
        message = json.dumps(Message(validationResponse.get("message", "Refresh token is not valid.")))
        return Response(message, status=403, content_type="application/json")

    userInfo = validationResponse.get("data")

    find_query = {
        "_id": ObjectId(userInfo.get('_id')),
        "refreshTokens": refreshToken
    }

    usersCollectionResponse = usersCollection.find_one(find_query)

    if not usersCollectionResponse:
        message = json.dumps(Message(validationResponse.get("message", "Refresh token is not valid.")))
        return Response(message, status=401, content_type="application/json")

    delete_query = {
        "$pull": {
            "refreshTokens": refreshToken
        }
    }

    usersCollection.update_one(find_query, delete_query)

    # prepare parameters json to generate tokens
    json_for_token = {
        "_id": str(usersCollectionResponse.get("_id")),
        "email": usersCollectionResponse.get("email")
    }
    json_for_token["exp"] = datetime.utcnow() + timedelta(seconds=600)

    accessTokenParameters = {
        "json": json_for_token,
    }
    accessTokenParameters.update(accessTokenParams)

    json_for_token["exp"] = datetime.utcnow() + timedelta(seconds=3600 * 24)
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
