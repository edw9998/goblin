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
    """Returns if the user is correct

    Args:
        username (str): Username
        password (str): Password

    Returns:
        bool: Whether the user credentials are correct
    """
    db = getDb()
    cursor = db.cursor()

    query = "SELECT password FROM users WHERE username=%s;"
    # Brackets are important! It only accepts tuple
    cursor.execute(query, (username, ))
    
    res = cursor.fetchone()
    if res == None:
        return False

    hashed_pass = res[0]
    return checkpw(str.encode(password), str.encode(hashed_pass))
