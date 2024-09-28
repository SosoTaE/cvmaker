# built in
import json

# installed
from flask import request, Response

# written by me
from database.database import universityCollection


def getUniversities():
    response = universityCollection.find_one({})
    _from = request.args.get("from", 0)
    _to = request.args.get("to", len(response['universities']) - 1)
    universities = response['universities'][int(_from):int(_to)]
    response.pop("_id", None)

    return Response(json.dumps({
        "universities": universities
    }), mimetype='application/json', status=200)