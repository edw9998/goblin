from api.forumapi import get_topics, create_topic
from views.forum import forum_view
from util import validate_input

def topics_view(state):
  print("List of topics:")
  # List of topics
  topics = get_topics()
  for topic in topics:
    print()
    print(f"{topic[0]}. {topic[1]} by {topic[3]}")
    print(f"Created in {topic[2]}")
  
  print("\nEnter the number of the topic that you want.")
  print("Alternatively, if you want to create a new topic, enter a name.")
  
  choice = input()
  if choice.isnumeric():
    choice = int(choice)
    for topic in topics:
      if choice == topic[0]:
        # Go to the forum view
        print(f"Going to forum {topic[1]}")
        forum_view(state, topic[0])
  else:
    create_topic(choice, state["user_id"])
    print(f"Created topic {choice}!")