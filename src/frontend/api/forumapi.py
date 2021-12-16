import requests as r

def get_topics():
  res = r.get("http://127.0.0.1:5000/forum/topics")
  return res.json()

def create_topic(name, user_id, token):
  res = r.post(
    "http://127.0.0.1:5000/forum/topics",
    json={
      "topic": name,
      "id": user_id
    },
    headers={
      "Authorization": "Bearer " + token
    }
  )
  if res.text != "Success!":
    raise Exception("Error creating a topic!")
  
def get_messages_topic(topicid):
  res = r.get(f"http://127.0.0.1:5000/forum/topics/{topicid}/message")
  return res.json()

def add_message_topic(topicid, userid, msg, token):
  res = r.post(
    f"http://127.0.0.1:5000/forum/topics/{topicid}/message",
    json={
      "msg": msg,
      "userId": userid
    },
    headers={
      "Authorization": "Bearer " + token
    }
  )

  if res.text != "Success!":
    raise Exception("Error sending a message!")