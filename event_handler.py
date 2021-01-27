import discord

def create_event(zeus, mission):
  embed = discord.Embed(title = 'Misia')
  embed.add_field(name = 'Misia', value = mission, inline = False)
  embed.add_field(name = 'Zeus', value = zeus, inline = False)
  embed.add_field(name = 'Cas irl', value = 'none')
  embed.add_field(name = 'Cas v hre', value = 'none')
  embed.add_field(name = 'Popis', value = 'none', inline = False)
  return embed

def set_times(embed, time_irl, time_game):
  new_embed = discord.Embed(title = embed.title)
  for f in embed.fields:
    if f.name == 'Cas irl':
      f.value = time_irl

    if f.name == 'Cas v hre':
      f.value = time_game

    new_embed.add_field(name = f.name, value = f.value, inline = f.inline)
  return new_embed

def set_desc(embed, desc):
  if desc.startswith('http'):
    desc = '[doc](%s)' % desc

  new_embed = discord.Embed(title = embed.title)
  for f in embed.fields:
    if f.name == 'Popis':
      f.value = desc

    new_embed.add_field(name = f.name, value = f.value, inline = f.inline)
  return new_embed

def check_zeus(embed, user):
  for f in embed.fields:
    print(f.name)
    if f.name == 'Zeus':
      print(f.value)
      print(user)
      if f.value == user:
        return True
      else:
        return False
