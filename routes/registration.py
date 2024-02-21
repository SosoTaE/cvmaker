# built in
from datetime import datetime
import json

# installed
from flask import request, Response

# written by me
from database.database import usersCollection
from message import Message
from Auth.password import hashPassword

body_json_example = {
    "email": str,
    "password": str
}


def registration():
    body = request.get_json()

    # user information
    email = body.get("email")
    password = body.get("password")
    createdAt = datetime.utcnow()

    # check if email is in database
    usersCollectionResponse = usersCollection.find_one({"email": email})

    if usersCollectionResponse:
        # jsonify message dict
        message = json.dumps(Message("This email was already used."))
        return Response(message, status=400, content_type="application/json")

    # user data for insertion
    user = {
        "email": email,
        "password": hashPassword(password),
        "createdAt": createdAt,
        "refreshTokens": []
    }

    usersCollection.insert_one(user)

    # jsonify message dict
    message = json.dumps(Message("User registered successfully."))
    return Response(message, status=200, content_type="application/json")
