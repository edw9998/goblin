from api.forumapi import get_messages_topic, add_message_topic
from util import validate_input, print_sep

def forum_view(state, topicid):
  # Will continue looping so that the user can continue to send messages
  # until it is broken by the `\quit` command
  while True:
    print_sep()
    msgs = get_messages_topic(topicid)
    
    if len(msgs) == 0:
      print("This topic is empty. Be the first one to send a message!")
    
    # Display all messages
    for rows in msgs:
      print()
      print(f"{rows[0]} ({rows[1]}) says:")
      print(rows[2])
      
    print()
    
    # Lambda is a way to declare a single line function that you can pass
    # to a function as a parameter
    inp = validate_input(
      "Enter your message. To quit from this topic, type `\\quit`",
      lambda msg : len(msg) != 0,
      "Message error. Enter your command again."
    )
    
    if inp == "\\quit":
      break
    else:
      add_message_topic(topicid, state["user_id"], inp, state["token"])
      print("Succesfully sent a message!")