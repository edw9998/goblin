# This state variable is to keep track of variables that we are going
# to use througout the program. We can edit the dictionary and the data will
# persist througout the runtime of the program.
# These are the initial / default values of the dictionary. You will see it
# being changed throughout the program.

# We put user id here because all the APIs need user id to function (So we
# don't need to do crazy joins in the API)
state = {
    "logged_in": False,
    "username": "",
    "user_id": None,
}
