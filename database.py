import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGODB_IP", "127.0.0.1"), 27017)
db = client.message_database
collection = db.message_collection


def add_message(message_id, time, content, author, guild, channel):
    post = {
        "message_id": str(message_id),
        "time": str(time),
        "content": str(content),
        "author": str(author),
        "guild": str(guild),
        "channel": str(channel)
    }

    collection.insert_one(post)
