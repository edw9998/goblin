from util import validate_input, check_name, check_password, print_sep
from api.userapi import login_user

def login_view(state):
  print_sep()
  
  # Asks for the username and password
  name = validate_input("Enter your username: ", check_name)
  pwd = validate_input("Enter your password: ", check_password)
  
  # Logs in the user using the API
  res = login_user(name, pwd)
  
  # Sets the state of the program if the user's credentials are matched with
  # the one in the database. The menu changes once state["logged_in"] is true.
  # Don't forget to also put the user id.
  if res != False:
    print("You are logged in!")
    state["logged_in"] = True
    state["user_id"] = res
  else:
    print("Wrong credentials")