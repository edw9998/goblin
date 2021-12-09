from backend.db import getDb, getError
import time
import mysql.connector


def create_topic(topic_name, user_id):
    """Creates a new topic with the corresponding user id

    Args:
        topic_name (str): The name of the topic
        user_id (int): The id of the user
    """
    db = getDb()
    cursor = db.cursor()

    try:
        # To avoid SQL Injections, replace the values in the original SQL query
        # with `%s`. Then the values will be replaced with a tuple created in
        # the next lines
        query = "INSERT INTO topics (name, userId, dateCreated) VALUES (%s, %s, %s);"
        
        # To insert dates, you have to do this format in python. Use the
        # builtin python time library
        # Here we create a tuple with the values that we want to insert into
        # the SQL query
        values = (topic_name, user_id, time.strftime('%Y-%m-%d %H:%M:%S'))
        cursor.execute(query, values)
        db.commit()
    except(mysql.connector.Error) as e:
        # Handle topic name too long, print
        print(e)


def get_topics():
    """Gets all of the topics in the database

    Returns:
        [[id, name, date, username]]: 2D array (Table) of the topic id, name,
        date created, and username.
    """
    db = getDb()
    cursor = db.cursor()
    cursor.execute("SELECT t.id, name, dateCreated, username FROM topics AS t JOIN users AS u ON t.userId=u.id;")
    return cursor.fetchall()


def get_messages_topic(topic_id):
    """Gets all the messages associated with the topic

    Args:
        topic_id (int): Id of the topic you want to get the messages of

    Returns:
        [[username, date, content]]: 2D array (Table) of the username, date,
        and content of the messages in the topic.
    """
    db = getDb()
    cursor = db.cursor()

    # This query gets all the messages associated with a topic, with the
    # corresponding user name who sent the message
    query = "SELECT u.username AS user, m.dateCreated as msgTime, content FROM topics AS t JOIN messages AS m ON t.id=m.topicId JOIN users AS u ON m.userId=u.id WHERE t.id=%s;"
    
    # VERY IMPORTANT. For single values tuple in mysql, you have to trail it
    # with a single comma. For example: (yes, )
    cursor.execute(query, (topic_id, ))
    return cursor.fetchall()


def add_message_topic(topic_id, user_id, msg):
    """Adds a message to the specified topic

    Args:
        topic_id (int): The id of the topic
        user_id (int): The id of the user
        msg (str): Message content
    """
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
