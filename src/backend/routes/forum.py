import flask
from flask import request
import backend.api.forumapi as api

forum_bl = flask.Blueprint("forum", __name__)

@forum_bl.route("/topics")
def get_topics():
  return flask.jsonify(api.get_topics())

@forum_bl.route("/topics/<id>/message", methods=["GET"])
def get_messages(id):
  """Gets all the messages associated with the topic id specified

  Args:
      id (str): Topic id
  """
  return flask.jsonify(api.get_messages_topic(id))

@forum_bl.route("/topics", methods=["POST"])
def create_topic():
  req = request.get_json(force=True)
  api.create_topic(req["topic"], req["id"])
  return "Success!"

@forum_bl.route("/topics/<id>/message", methods=["POST"])
def create_message(id):
  """Creates a new message in the specified topic by `id`

  Args:
      id (str): Topic id
  """
  req = request.get_json(force=True)
  api.add_message_topic(id, req["userId"], req["msg"])
  return "Success!"