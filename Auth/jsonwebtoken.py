import jwt
from jwt import exceptions


def Validate(token, secret, algorithm):
    try:
        data = jwt.decode(token, secret, algorithm)
        return {"success": True, "data": data}
    except exceptions.InvalidAlgorithmError:
        return {"success": False, "message": "Algorithm is not valid."}
    except exceptions.DecodeError:
        return {"success": False, "message": "Error while decoding."}
    except exceptions.ExpiredSignatureError:
        return {"success": False, "message": "Signature is expired."}
    except exceptions.InvalidTokenError:
        return {"success": False, "message": "Token is not valid."}
    except exceptions.InvalidKeyError:
        return {"success": False, "message": "Key is not valid."}
    except exceptions as e:
        return {"success": False, "message": str(e)}


def Token(json, secret, algorithm):
    return jwt.encode(json, secret, algorithm)


def GenerateAccessAndRefreshTokens(access, refresh):
    return {
        "accessToken": Token(**access),
        "refreshToken": Token(**refresh)
    }
