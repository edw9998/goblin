import flask
from flask import request
import backend.api.forumapi as api

forum_bl = flask.Blueprint("forum", __name__)

@forum_bl.route("/topics")
def get_topics():
  return flask.jsonify(api.get_topics())

# <id> is an argument
@forum_bl.route("/topics/<id>")
def get_topic(id):
  return flask.jsonify(api.get_messages_topic(id))

@forum_bl.route("/topics", methods=["POST"])
def create_topic():
  req = request.get_json(force=True)
  api.create_topic(req["topic"], req["id"])
  return "Success!"