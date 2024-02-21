# database configuration
CONNECTION_STRING = "mongodb://localhost:27017"
DATABASE = "cvmaker"
USERS_COLLECTION = "users"

SECRET_KEY_LENGTH = 64

ACCESS_SECRET_KEY = None
# read access token
with open("configs/accessTokenSecretKey.pem", "r") as file:
    ACCESS_SECRET_KEY = file.read()

REFRESH_SECRET_KEY = None
# read refresh token
with open("configs/refreshTokenSecretKey.pem", "r") as file:
    REFRESH_SECRET_KEY = file.read()

ALGORITHM = 'HS256'

refreshTokenParams = {
    "algorithm": ALGORITHM,
    "secret": REFRESH_SECRET_KEY
}

accessTokenParams = {
    "algorithm": ALGORITHM,
    "secret": ACCESS_SECRET_KEY
}

