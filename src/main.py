from db import getDb
from state import state
from api.forumapi import get_messages_topic
from views.exit import exit_view
from views.logout import logout_view
from views.register import register_view
from views.login import login_view
from views.topics import topics_view

while True:
  print("Welcome to Goblin")
  
  if not state["logged_in"]:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    opt = input("Select a number: ")
    if opt == "1":
      register_view()
    elif opt == "2":
      login_view(state)
    elif opt == "3":
      exit_view()
    else:
      print("Wrong number, enter again")
    
  else:
    print("1. Topics")
    print("2. Logout")
    print("3. Exit")
    opt = input("Select a number: ")
    if opt == "1":
      topics_view(state)
    elif opt == "2":
      logout_view(state)
    elif opt == "3":
      exit_view()
    else:
      print("Wrong number, enter again")
  
  print()
