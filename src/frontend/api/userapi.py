import requests as r
import os

# We get the ROOTURL from the environment variable. Why?
# That's because URLs can change depending on where we deploy our backend
# application. For example, for development we may deploy it in localhost. So:
# localhost:xxxx or 127.0.0.1:xxxx. And when we deploy it to the internet,
# we may use an IP address or domain. So, this needs to be specified.
ROOT_URL = os.getenv("ROOTURL", "http://127.0.0.1:5000")

def register_user(name, pwd):
  """Registers the user

  Args:
      name (str): Username of the user
      pwd (str): User password

  Raises:
      Exception: Error registering
  """
  res = r.post(
    ROOT_URL + "/register",
    json={
      "username": name,
      "password": pwd,
    }
  )
  
  if res.text != "Success!":
    raise Exception("Error registering!\n " + res.text)
  
def login_user(name, pwd):
  """Logs in the user and returns a JWT Token

  Args:
      name (str): Username of the user
      pwd (str): User password

  Returns:
      str: JWT Token
  """
  res = r.post(
    ROOT_URL + "/login",
    json={
      "username": name,
      "password": pwd,
    }
  )
  
  if res.text == "Login Error":
    return False
  return res.text[1:-2]