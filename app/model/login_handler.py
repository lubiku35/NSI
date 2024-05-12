from model import db

def login_user(data):
    email = data.get('email')
    password = data.get('password')

    if not db.is_email_registered(email):
        return 'Invalid Email or Password'

    if not db.verify_password(password, email):
        return 'Invalid Email or Password'

    return True