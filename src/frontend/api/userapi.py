import requests as r

def register_user(name, pwd):
  res = r.post(
    "http://127.0.0.1:5000/register",
    json={
      "username": name,
      "password": pwd,
    }
  )
  
  if res.text != "Success!":
    raise Exception("Error registering!")
  
def login_user(name, pwd):
  res = r.post(
    "http://127.0.0.1:5000/login",
    json={
      "username": name,
      "password": pwd,
    }
  )
  
  if res.text == "Login Error":
    return False
  return res.text[1:-2]