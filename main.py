import discord
import os

from keep_alive import keep_alive

client = discord.Client()

sad_words = ["kill"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!help'):
    await message.channel.send('do you need help ?!')

keep_alive()
client.run(os.getenv('TOKEN'))
