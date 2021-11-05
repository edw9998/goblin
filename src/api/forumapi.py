from db import getDb
import time


def create_topic(topic_name, user_id):
    """Creates a new topic with the corresponding user
    multiline comments"""
    db = getDb()
    cursor = db.cursor()

    # Try because code can throw error. Must handle it in except but we dont handle lol
    # SCORE_TODO: Anyone who can fill except with proper handling code gets 100
    # Pull request in GitHub
    # Requirements: The except code has to handle ONLY MYSQL ERRORS
    try:
        query = "INSERT INTO topics (name, userId, dateCreated) VALUES (%s, %s, %s);"
        values = (topic_name, user_id, time.strftime('%Y-%m-%d %H:%M:%S'))
        cursor.execute(query, values)
        db.commit()
    except:
        # Handle topic name too long, print
        pass


def get_topics():
    """Gets all of the topics in the database"""
    db = getDb()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM topics;")
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

    # SCORE_TODO: Anyone who can fill except with proper handling code gets 100
    # MUST PULL REQUEST
    # Requirements: The except code has to handle ONLY MYSQL ERRORS
    try:
        query = "INSERT INTO messages (content, dateCreated, userId, topicId) VALUES (%s, %s, %s, %s)"
        values = (msg, time.strftime('%Y-%m-%d %H:%M:%S'), user_id, topic_id)
        cursor.execute(query, values)
        db.commit()
    except:
        pass
