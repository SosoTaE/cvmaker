# built in
import json

# installed
from flask import request, Response

# written by me
from database.database import professionsCollection


def getProfessions():
    response = professionsCollection.find_one({})
    _from = request.args.get("from", 0)
    _to = request.args.get("to", len(response['professions']) - 1)
    professions = response['professions'][int(_from):int(_to)]
    response.pop("_id", None)

    return Response(json.dumps({
        "professions": professions
    }), mimetype='application/json', status=200)