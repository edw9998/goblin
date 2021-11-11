from util import validate_input, check_name, check_password
from api.userapi import login_user

def login_view(state):
  name = validate_input("Enter your username: ", check_name)
  pwd = validate_input("Enter your password: ", check_password)
  
  res = login_user(name, pwd)
  
  if res != False:
    print("You are logged in!")
    state["logged_in"] = True
    state["user_id"] = res
  else:
    print("Wrong credentials")