import flask
from flask import request
import backend.api.userapi as api
import jwt
import time
import os

"""Do logins and registers"""

# Gets the JWT secret from environment variable
JWT_SECRET = os.getenv("JWT_SECRET", "testing")

# When will the token will expire (You can modify this!)
EXPIRE_IN = 60 * 60 * 24 * 3 # Expires in 3 days #########!Challenge: Make this a environment variable in the env example file and do your best to comment it there!

user_bl = flask.Blueprint("user", __name__)

@user_bl.route("/register", methods=["POST"])
def register_user():
  """Route for registering the user. Needs:
  {
    username: str,
    password: str
  }

  Returns:
      str: If registering is successful
  """
  req = request.get_json(force=True)
  api.register_user(req["username"], req["password"])
  return "Success!"

@user_bl.route("/login", methods=["POST"])
def login_user():
  """Route for loggin in the user. Needs:
  {
    username: str,
    password: str
  }

  Returns:
      str: If login is successful, return token.
  """
  req = request.get_json(force=True)
  result = api.login_user(req["username"], req["password"])
  if not result:
    return "Login Error"
  else:
    token = jwt.encode(
      {
        "sub": result,
        "iat": time.time(),
        "exp": time.time() + EXPIRE_IN,
      },
      JWT_SECRET,
      algorithm="HS256"
    )
    return flask.jsonify(token)
