# installed
import bcrypt

# hash password
def hashPassword(password):
    password = password.encode('utf-8')

    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password
    return bcrypt.hashpw(password, salt)


# verify password
def verifyPassword(enteredPassword, hashed_oass):
    entered_password = enteredPassword.encode('utf-8')

    # Check if the entered password matches the hashed password
    if bcrypt.checkpw(entered_password, hashed_oass):
        return True
    else:
        return False
