# built in
import secrets

# written by me
from configs.config import SECRET_KEY_LENGTH


# generates random bytes and converts into hex
def Key(length):
    return secrets.token_bytes(length).hex()


# writes random keys in file
def WriteKey(path, length):
    with open(path, "w") as file:
        key = Key(length)
        file.write(key)


# if __name__ == "__main__":
#     # for access secret key
#     WriteKey("../configs/accessTokenSecretKey.pem", SECRET_KEY_LENGTH)
#
#     # for refresh secret key
#     WriteKey("../configs/refreshTokenSecretKey.pem", SECRET_KEY_LENGTH)