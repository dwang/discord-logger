import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGODB_IP", "127.0.0.1"), 27017)
db = client.discord_logger


def add_message(guild, message_id, time, content, author, channel):
    post = {
        "message_id": str(message_id),
        "time": str(time),
        "content": str(content),
        "author": str(author),
        "channel": str(channel)
    }

    db[str(guild)].insert_one(post)
