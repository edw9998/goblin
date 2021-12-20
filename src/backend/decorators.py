from functools import wraps
import flask
from backend.routes.user import JWT_SECRET
import jwt

def auth_required(func):
  """A login required decorator for flask routes. Basically, use this decorator
  for paths (routes) that you want to protect. To use the route, basically the
  client HTTP (frontend) has to specify a valid JWT token in the "Authorization"
  header in this format:
  
  "Authorization": "Bearer <token>"
  
  This decorator will check the validity of the token first before going into
  the actual route that you want to protect. If the token is invalid, then
  the execution will stop, and an error message will be sent instead of the
  route. If it is valid, the execution will continue and the route will be run
  as usual.
  
  If you want to look up more about decorators, I suggest this article:
  https://realpython.com/primer-on-python-decorators/

  Args:
      func (func): Route that you want to decorate

  Returns:
      func: Decorated route
  """
  @wraps(func)
  def decorated(*args, **kwargs):
    # The jwt.decode function will throw an error if the token is invalid.
    # Catch them in except blocks.
    try:
      # Gets the header from the HTTP request, defaulting as `None` if the
      # header does not exist.
      auth_header = flask.request.headers.get("Authorization", None)
      if not auth_header: return "No authentication header!"
      
      # Splitting in auth header just meants to separate the "Bearer" part with
      # the "token" part. So, "Bearer <token>" becomes ["Bearer", "<token>"],
      # and you can just get the second index for the token.
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