import os
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv("CONNECTION_STRING")
if not CONNECTION_STRING:
    raise ValueError("CONNECTION_STRING environment variable is not set")

DATABASE = os.getenv("DATABASE")
if not DATABASE:
    raise ValueError("DATABASE environment variable is not set")

USERS_COLLECTION = os.getenv("USERS_COLLECTION")
if not USERS_COLLECTION:
    raise ValueError("USERS_COLLECTION environment variable is not set")

UNIVERSITY_COLLECTION = os.getenv("UNIVERSITY_COLLECTION")
if not UNIVERSITY_COLLECTION:
    raise ValueError("UNIVERSITY_COLLECTION environment variable is not set")

PROFESSION_COLLECTION = os.getenv("PROFESSION_COLLECTION")
if not PROFESSION_COLLECTION:
    raise ValueError("PROFESSION_COLLECTION environment variable is not set")

SECRET_KEY_LENGTH = os.getenv("SECRET_KEY_LENGTH")
if not SECRET_KEY_LENGTH:
    raise ValueError("SECRET_KEY_LENGTH environment variable is not set")

ALGORITHM = os.getenv("ALGORITHM")
if not ALGORITHM:
    raise ValueError("ALGORITHM environment variable is not set")

SECRET_KEY_LENGTH = os.getenv("SECRET_KEY_LENGTH")
if not SECRET_KEY_LENGTH:
    raise ValueError("SECRET_KEY_LENGTH environment variable is not set")

ACCESS_SECRET_KEY = None
# read access token
with open("configs/accessTokenSecretKey.pem", "r") as file:
    ACCESS_SECRET_KEY = file.read()

REFRESH_SECRET_KEY = None
# read refresh token
with open("configs/refreshTokenSecretKey.pem", "r") as file:
    REFRESH_SECRET_KEY = file.read()

refreshTokenParams = {
    "algorithm": ALGORITHM,
    "secret": REFRESH_SECRET_KEY
}

accessTokenParams = {
    "algorithm": ALGORITHM,
    "secret": ACCESS_SECRET_KEY
}

