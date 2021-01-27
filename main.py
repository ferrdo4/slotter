import discord
import os

from keep_alive import keep_alive
from event_handler import create_event, set_times, set_desc, check_zeus, set_team, rm_team

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!create'):
    mission = msg.replace('!create', '')
    embed_msg = create_event(message.author.name, mission)
    await message.channel.send(embed=embed_msg)
    return

  if msg.startswith('!set_times'):
    params = msg.split(' ')
    if len(params) != 4:
      await message.channel.send("use !set_times [message_id] [time irl] [time ingame]")
      return
    old_message = await client.get_channel(message.channel.id).fetch_message(params[1])
    embed = old_message.embeds[0]
    if not check_zeus(embed, message.author.name):
      await message.channel.send("Nie si Zeus!")
      return
    new_embed = set_times(embed, params[2], params[3])
    await old_message.edit(embed=new_embed)
    return

  if msg.startswith('!set_desc'):
    params = msg.split(' ')
    if len(params) < 3:
      await message.channel.send("use !set_desc [message_id] [desc/url]")
      return
    old_message = await client.get_channel(message.channel.id).fetch_message(params[1])
    embed = old_message.embeds[0]
    if not check_zeus(embed, message.author.name):
      await message.channel.send("Nie si Zeus!")
      return
    new_embed = set_desc(embed, msg.replace('!set_desc ', '').replace('%s '%params[1], ''))
    await old_message.edit(embed=new_embed)
    return

  if msg.startswith('!set_team'):
    params = msg.split(' ')
    if len(params) != 5:
      await message.channel.send("use !set_team [message_id] [team] [role,role] [inline(True/False)]")
      return
    old_message = await client.get_channel(message.channel.id).fetch_message(params[1])
    embed = old_message.embeds[0]
    if not check_zeus(embed, message.author.name):
      await message.channel.send("Nie si Zeus!")
      return
    new_embed = set_team(embed, params[2], params[3], params[4])
    await old_message.edit(embed=new_embed)
    return

  if msg.startswith('!rm_team'):
    params = msg.split(' ')
    if len(params) != 3:
      await message.channel.send("use !rm_team [message_id] [team]")
      return
    old_message = await client.get_channel(message.channel.id).fetch_message(params[1])
    embed = old_message.embeds[0]
    if not check_zeus(embed, message.author.name):
      await message.channel.send("Nie si Zeus!")
      return
    new_embed = rm_team(embed, params[2])
    await old_message.edit(embed=new_embed)
    return

keep_alive()
client.run(os.getenv('TOKEN'))
