import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
  return 'fjdafsda;'

@app.route('/movies')
def movie():
  return 'I am movie man man'