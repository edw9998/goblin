import requests as r
import os

# We get the ROOTURL from the environment variable. Why?
# That's because URLs can change depending on where we deploy our backend
# application. For example, for development we may deploy it in localhost. So:
# localhost:xxxx or 127.0.0.1:xxxx. And when we deploy it to the internet,
# we may use an IP address or domain. So, this needs to be specified.
ROOT_URL = os.getenv("ROOTURL", "http://127.0.0.1:5000")

def get_topics():
  """Does a HTTP GET request to the topics

  Returns:
      [array]: Array of the topics
  """
  res = r.get(ROOT_URL + "/forum/topics")
  return res.json()

def create_topic(name, user_id, token):
  """Creates a new topic in the database. Requires token auth

  Args:
      name (str): Name of the user
      user_id (int): ID of the user 
      token (str): JWT Token

  Raises:
      Exception: Creating topic error
  """
  res = r.post(
    ROOT_URL + "/forum/topics",
    json={
      "topic": name,
      "id": user_id
    },
    headers={
      "Authorization": "Bearer " + token
    }
  )
  if res.text != "Success!":
    raise Exception("Error creating a topic!\n " + res.text)
  
def get_messages_topic(topicid):
  """Gets all the messages for the specified topic id

  Args:
      topicid (int): Topic ID

  Returns:
      [array]: Array of the messages
  """
  res = r.get(ROOT_URL + f"/forum/topics/{topicid}/message")
  return res.json()

def add_message_topic(topicid, userid, msg, token):
  """Adds a message to a specified topic

  Args:
      topicid (int): Topic ID
      userid (int): User ID
      msg (str): Message content
      token (str): JWT Token

  Raises:
      Exception: Error creating message
  """
  res = r.post(
    ROOT_URL + f"/forum/topics/{topicid}/message",
    json={
      "msg": msg,
      "userId": userid
    },
    headers={
      "Authorization": "Bearer " + token
    }
  )

  if res.text != "Success!":
    raise Exception("Error sending a message!\n " + res.text)