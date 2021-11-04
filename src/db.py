from mysql.connector import connect

# Connect to the database
__db = connect(
  host="sigma.jasoncoding.com",
  user="alpha",
  password="bestdatabase",
  database="classicmodels",
  port=5555
)

# Simple logic that will reconnect if the connection is severed
def getDb():
  if not __db.is_connected():
    __db.reconnect()
  return __db
