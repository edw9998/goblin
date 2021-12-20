import flask
from backend.routes.forum import forum_bl
from backend.routes.user import user_bl
from dotenv import load_dotenv

# This file will be run first by the `flask run` command in the terminal
# (or startdevserver.py).

# Load .env file
load_dotenv()

# Creates a new flask app using the current name
app = flask.Flask(__name__)

# Route just for testing
@app.route('/')
def hello():
  return 'Server is up!'

# Register blueprints (Blueprints are basically routes combined into one object)
app.register_blueprint(forum_bl, url_prefix="/forum")
app.register_blueprint(user_bl)