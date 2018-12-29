import os

import discord
from loguru import logger

import database

logger.add("messages.log", enqueue=True, colorize=True,
           format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> "
           "<level>{message}</level>")
client = discord.Client()


@client.event
async def on_ready():
    logger.info("Logged in as {0.user}", client, feature="f-strings")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = (message.attachments[0].proxy_url
               if message.attachments else message.content)

    database.add_message(message.id, message.created_at, content,
                         message.author.id, message.guild.id,
                         message.channel.id)

    logger.info("({0.guild} - #{0.channel}) {0.author}: {1}", message,
                content, feature="f-strings")

client.run(os.environ.get("DISCORD_API_KEY"))
