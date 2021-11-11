from api.forumapi import get_topics, create_topic
from views.forum import forum_view
from util import validate_input

def topics_view(state):
  print("List of topics:")
  # List of topics
  topics = get_topics()
  
  # Prints all the topics in the database and formats it. to make it pretty
  for topic in topics:
    print()
    print(f"{topic[0]}. {topic[1]} by {topic[3]}")
    print(f"Created in {topic[2]}")
  
  print("\nEnter the number of the topic that you want.")
  print("Alternatively, if you want to create a new topic, enter a name.")
  
  # Here we take input from the user, and we can do two things depending on
  # what the user inputs.
  # If the user inputs a number, then the user will go to the specified topic
  # with the topic id matching the number
  # If the user enters a text, it will create a new topic entry instead.
  choice = input()
  if choice.isnumeric():
    # Converts the choice to integer. Because the one that we are matching from
    # the database is an integer type.
    choice = int(choice)
    
    # Search if there is an associated topic id inputted by the user that
    # is gotten from the database.
    for topic in topics:
      if choice == topic[0]:
        # Go to the forum view
        print(f"Going to forum {topic[1]}")
        forum_view(state, topic[0])
      else:
        print("Topic ID does not exist!")
  else:
    create_topic(choice, state["user_id"])
    print(f"Created topic {choice}!")