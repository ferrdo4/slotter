import discord
import os

from keep_alive import keep_alive
from event_handler import create_event, set_times, set_desc, check_zeus

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!help'):
    await message.channel.send('''!create [nazov misie]
    !set_times [cas irl] [cas v hre]''')

  if msg.startswith('!create'):
    mission = msg.replace('!create', '')
    embed_msg = create_event(message.author.name, mission)
    await message.channel.send(embed=embed_msg)

  if msg.startswith('!set_times'):
    params = msg.split(' ')
    message = await client.get_channel(message.channel.id).fetch_message(params[1])
    embed = message.embeds[0]
    if not check_zeus(embed, message.author.name):
      await message.channel.send("Nie si Zeus!")
      return
    new_embed = set_times(embed, params[2], params[3])
    await message.edit(embed=new_embed)

  if msg.startswith('!set_desc'):
    params = msg.split(' ')
    message = await client.get_channel(message.channel.id).fetch_message(params[1])
    embed = message.embeds[0]
    if not check_zeus(embed, message.author.name):
      await message.channel.send("Nie si Zeus!")
      return
    new_embed = set_desc(embed, params[2])
    await message.edit(embed=new_embed)

keep_alive()
client.run(os.getenv('TOKEN'))
