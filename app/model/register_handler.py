# Registration Handler

from model import db

RESERVED_USERNAMES = ['admin', 'root', 'sysadmin', 'administrator', 'superuser', 'moderator']

def register_user(data):
    validated = validate_form_data(data)

    if validated is not True: return validated
    else:         
        db.register_user(data)
        return True
 
def validate_form_data(data):
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    password_repeat = data.get('password-repeat')
    
    if not name or not email or not password or not password_repeat:
        return "Missing required fields"
    
    if name.lower() in RESERVED_USERNAMES:
        return "Username is reserved"
       
    if db.is_email_registered(email):
        return "Email already registered"

    if password != password_repeat:
        return "Passwords do not match"

    if validate_password_entropy(password) is not True:
        return validate_password_entropy(password)
             
    return True

def validate_password_entropy(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    
    if password.isalpha() or password.isdigit():
        return "Password must contain both letters and numbers"
    
    if password.islower() or password.isupper():
        return "Password must contain both upper and lower case letters"
    
    if password.isalnum():
        return "Password must contain special characters"
        
    return True