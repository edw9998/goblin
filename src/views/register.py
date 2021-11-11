from util import validate_input
from api.userapi import register_user

def check_name(msg):
  # Check whitespace
  for x in msg:
    if x == " ":
      return False
 
  # Less than 20 characters 
  if len(msg) > 20 or len(msg) < 3:
    return False
  
  return True

def check_password(msg):
  # Less than 30 characters 
  if len(msg) > 30 or len(msg) < 5:
    return False
  
  number_there = False
  # Check number
  for x in msg:
    if x.isnumeric():
      number_there = True
      
  return number_there

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
