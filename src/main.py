from db import getDb
from state import state
from api.forumapi import get_messages_topic
from views.exit import exit_view
from views.logout import logout_view

while True:
  print("Welcome to Goblin")
  
  if not state["logged_in"]:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    opt = input("Select a number:")
    if opt == "1":
      pass
    elif opt == "2":
      pass
    elif opt == "3":
      exit_view()
    else:
      print("Wrong number, enter again")
    
  else:
    print("1. topics")
    print("2. logout")
    print("3. exit")
    opt = input("Select a number:")
    if opt == "1":
      pass
    elif opt == "2":
      logout_view(state)
    elif opt == "3":
      exit_view()
    else:
      print("Wrong number, enter again")
