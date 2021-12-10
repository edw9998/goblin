import flask
from backend.routes.forum import forum_bl
from backend.routes.user import user_bl

app = flask.Flask(__name__)

@app.route('/')
def hello():
  return 'fjdafsda;'

app.register_blueprint(forum_bl, url_prefix="/forum")
app.register_blueprint(user_bl)