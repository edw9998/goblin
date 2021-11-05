from db import getDb
from bcrypt import gensalt, hashpw


def register_user(username, password: str):
    db = getDb()
    cursor = db.cursor()

    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    new_pass = hashpw(str.encode(password), gensalt())

    values = (username, new_pass.decode())
    cursor.execute(query, values)

    # Very important when inserting data
    db.commit()
