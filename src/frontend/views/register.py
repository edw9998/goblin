from util import validate_input, check_name, check_password, print_sep
from api.userapi import register_user

def register_view():
  print_sep()
  # Asks for the username
  name = validate_input("Register your username: ", check_name)
  print(f"your username is {name}")
  
  # Asks for the password two times and checks if both of them is the same.
  # If the password is not the same, then retry inserting the password.
  while True:
    pwd = validate_input("Enter your password: ", check_password)
    same_pwd = validate_input("Enter your password a second time: ", check_password)
    
    if pwd != same_pwd:
      print("Password does not match!")
    else:
      break
  
  # Registers the user in the database using the API
  register_user(name, pwd)
  print("You are registered successfully!")
