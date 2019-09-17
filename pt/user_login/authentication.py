from passlib.apps import custom_app_context as pwd_context

def hash_password(password):
        return pwd_context.hash(password)

users = {'user': 'hash'}

def verify_login(username, password):
    if username in users:
        verification = pwd_context.verify(password, users[username])
        if verification:
            return True
    return False
