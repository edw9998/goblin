from functools import wraps
import flask
from backend.routes.user import JWT_SECRET
import jwt

def auth_required(func):
  @wraps(func)
  def decorated(*args, **kwargs):
    try:
      auth_header = flask.request.headers.get("Authorization", None)
      if not auth_header: return "No authentication header!"
      jwt.decode(
        auth_header.split()[1],
        JWT_SECRET,
        algorithms=["HS256"]
      )
      return func(*args, **kwargs)
    except jwt.ExpiredSignatureError:
      return "Token is expired!"
    except jwt.InvalidSignatureError:
      return "Token invalid!"
    except jwt.DecodeError:
      return "JWT decode error!"
  return decorated