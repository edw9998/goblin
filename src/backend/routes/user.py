import flask
from flask import request
import backend.api.userapi as api
import jwt
import time
import os

"""Do logins and registers"""

JWT_SECRET = os.getenv("JWT_SECRET", "testing")
EXPIRE_IN = 60 * 60 * 24 * 3 # Expires in 3 days
user_bl = flask.Blueprint("user", __name__)

@user_bl.route("/register", methods=["POST"])
def register_user():
  req = request.get_json(force=True)
  api.register_user(req["username"], req["password"])
  return "Success!"

@user_bl.route("/login", methods=["POST"])
def login_user():
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
