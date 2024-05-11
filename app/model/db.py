import sqlite3, hashlib, sys

DB = 'appDatabase.db'
    
# ==== USER MANAGEMENT ====

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


# ==== MEASUREMENT MANAGEMENT ====

def create_measurements_table():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS measurements
                 (id INTEGER PRIMARY KEY, timestamp DATETIME, temp REAL)''')
    conn.commit()
    conn.close()


def load_data():
    create_measurements_table()

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT * FROM measurements')
    data = c.fetchall()
    conn.close()

    return [{'id': item[0], 'timestamp': item[1], 'temp': item[2]} for item in data]

def load_data_by_id(item_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT * FROM measurements WHERE id = ?', (item_id,))
    item = c.fetchone()
    conn.close()

    return {'id': item[0], 'timestamp': item[1], 'temp': item[2]} if item else None

def load_data_by_items(items):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT * FROM measurements LIMIT ?', (items,))
    data = c.fetchall()
    conn.close()

    return [{'id': item[0], 'timestamp': item[1], 'temp': item[2]} for item in data]


def update_data(item_id, new_data):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('UPDATE measurements SET timestamp = ?, temp = ? WHERE id = ?', (new_data['timestamp'], new_data['temp'], item_id))
    conn.commit()
    conn.close()

    return True

def create_data(new_data):
    create_measurements_table()

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO measurements (timestamp, temp) VALUES (?, ?)', (new_data['timestamp'], new_data['temp']))
    except sqlite3.Error as e:
        print(e, file=sys.stderr)
        return False        
    conn.commit()
    conn.close()

    return True

def delete_data(item_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('DELETE FROM measurements WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()

    return True

