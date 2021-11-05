from db import getDb
from bcrypt import gensalt, hashpw, checkpw


def register_user(username, password: str):
    db = getDb()
    cursor = db.cursor()

    query = "INSERT INTO users (username, password) VALUES (%s, %s);"
    new_pass = hashpw(str.encode(password), gensalt())

    values = (username, new_pass.decode())
    cursor.execute(query, values)

    # Very important when inserting data
    db.commit()


def login_user(username, password):
    db = getDb()
    cursor = db.cursor()

    query = "SELECT password FROM users WHERE username=%s;"
    # Brackets are important! It only accepts tuple
    cursor.execute(query, (username, ))

    hashed_pass = cursor.fetchone()[0]
    return checkpw(str.encode(password), str.encode(hashed_pass))
