from db import getDb, getError
import time
import mysql.connector


def create_topic(topic_name, user_id):
    """Creates a new topic with the corresponding user
    multiline comments"""
    db = getDb()
    cursor = db.cursor()

    try:
        query = "INSERT INTO topics (name, userId, dateCreated) VALUES (%s, %s, %s);"
        values = (topic_name, user_id, time.strftime('%Y-%m-%d %H:%M:%S'))
        cursor.execute(query, values)
        db.commit()
    except(mysql.connector.Error) as e:
        # Handle topic name too long, print
        print(e)


def get_topics():
    """Gets all of the topics in the database"""
    db = getDb()
    cursor = db.cursor()
    cursor.execute("SELECT t.id, name, dateCreated, username FROM topics AS t JOIN users AS u ON t.userId=u.id;")
    return cursor.fetchall()


def get_messages_topic(topic_id):
    """Gets all the messages associated with the topic"""
    db = getDb()
    cursor = db.cursor()

    # This query gets all the messages associated with a topic, with the
    # corresponding user name who sent the message
    query = "SELECT u.username AS user, m.dateCreated as msgTime, content FROM topics AS t JOIN messages AS m ON t.id=m.topicId JOIN users AS u ON m.userId=u.id WHERE t.id=%s;"
    cursor.execute(query, (topic_id, ))
    return cursor.fetchall()


def add_message_topic(topic_id, user_id, msg):
    """Adds a message to the specified topic"""
    db = getDb()
    cursor = db.cursor()

    try:
        query = "INSERT INTO messages (content, dateCreated, userId, topicId) VALUES (%s, %s, %s, %s)"
        values = (msg, time.strftime('%Y-%m-%d %H:%M:%S'), user_id, topic_id)
        cursor.execute(query, values)
        db.commit()
    except getError() as err:
        print("Something went wrong: {}".format(err))
        pass
