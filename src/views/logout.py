def logout_view(state):
  # Log out of the program. Sets the state dictionary of logged_in into false,
  # Changing the menu.
  print("Logging out...")
  state["logged_in"] = False