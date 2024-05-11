import sqlite3, hashlib

DB = 'appDatabase.db'
    

def create_users_table():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def register_user(data):
    name = data.get('name')
    email = data.get('email')
    password = hash_password(data.get('password'))

    # Create users table if it doesn't exist
    create_users_table()

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
    conn.commit()
    conn.close()

    return True

def get_user_password(email):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE email = ?', (email,))
    user = c.fetchone()
    conn.close()

    return user[0] if user else None

def get_user_by_email(email):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = c.fetchone()
    conn.close()

    return user

# SHA-256 Hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, email):
    hashed_password = get_user_password(email)
    return hash_password(password) == hashed_password

def is_email_registered(email):
    return get_user_by_email(email) is not None
