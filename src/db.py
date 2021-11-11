from mysql.connector import connect
import mysql.connector

# Connect to the database
# Double underscore means private. Means that it cannot be imported from this
# file.
# Host can either be IP or the URL of the server.
# User is the MySQL user
# database is the initial database that you want to start with
# Port is the port of the server in which MySQL server listens to
__db = connect(
  host="sigma.jasoncoding.com",
  user="alpha",
  password="bestdatabase",
  database="goblin_db",
  port=5555
)

# Simple logic that will reconnect the sql connection object if the
# connection is severed
def getDb():
  if not __db.is_connected():
    __db.reconnect()
  return __db

# Returns the mysql error object to use in exceptions
def getError():
  return mysql.connector.Error