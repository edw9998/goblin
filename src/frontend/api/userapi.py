import requests as r
import os

ROOT_URL = os.getenv("ROOTURL", "http://127.0.0.1:5000")

def register_user(name, pwd):
  res = r.post(
    ROOT_URL + "/register",
    json={
      "username": name,
      "password": pwd,
    }
  )
  
  if res.text != "Success!":
    raise Exception("Error registering!")
  
def login_user(name, pwd):
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