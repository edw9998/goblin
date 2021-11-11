from util import validate_input, check_name, check_password
from api.userapi import register_user

def register_view():
  name = validate_input("Register your username: ", check_name)
  print(f"your username is {name}")
    
  while True:
    pwd = validate_input("Enter your password: ", check_password)
    same_pwd = validate_input("Enter your password a second time: ", check_password)
    
    if pwd != same_pwd:
      print("Password does not match!")
    else:
      break
    
  register_user(name, pwd)
  print("You are registered successfully!")
