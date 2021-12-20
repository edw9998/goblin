import flask
from flask import request
import backend.api.forumapi as api
import backend.decorators as decs

forum_bl = flask.Blueprint("forum", __name__)

@forum_bl.route("/topics")
def get_topics():
  """Gets all the topics in the server

  Returns:
      [arr]: Array of topics
  """
  return flask.jsonify(api.get_topics())

@forum_bl.route("/topics/<id>/message", methods=["GET"])
def get_messages(id):
  """Gets all the messages associated with the topic id specified
  
  id: forum topic id

  Args:
      id (str): Topic id
  """
  return flask.jsonify(api.get_messages_topic(id))

@forum_bl.route("/topics", methods=["POST"])
@decs.auth_required
def create_topic():
  """Creates a topic in the program. Needs:
  {
    topic: str, # topic id
    id: int # user id
  }

  Returns:
      str: If the operation is a success
  """
  req = request.get_json(force=True)
  api.create_topic(req["topic"], req["id"])
  return "Success!"

@forum_bl.route("/topics/<id>/message", methods=["POST"])
@decs.auth_required
def create_message(id):
  """Creates a new message in the specified topic by `id`. Needs:
  {
    userId: int, # User id
    msg: str, # Msg id
  }
  
  id: forum topic id

  Args:
      id (str): Topic id
  """
  req = request.get_json(force=True)
  api.add_message_topic(id, req["userId"], req["msg"])
  return "Success!"

# For delete routes, use the "DELETE" HTTP method
############# ! Challenge: Create a delete route for a message!
############# ! Challenge: Create a delete route for a topic (Along with its messages)!
