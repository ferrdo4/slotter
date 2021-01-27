import discord

def create_event(zeus, mission):
  embed = discord.Embed(title = 'Misia')
  embed.add_field(name = 'Misia', value = mission, inline = False)
  embed.add_field(name = 'Zeus', value = zeus, inline = False)
  embed.add_field(name = 'Cas irl', value = 'none')
  embed.add_field(name = 'Cas v hre', value = 'none')
  embed.add_field(name = 'Popis', value = 'none', inline = False)
#  embed.add_field(name = "Omega", value = f'> PL\t\tempty\n> O1\t\tempty\n> O2\t\tempty\n', inline = False)
#  embed.add_field(name = "Alpha", value =  f'> TL\t\tempty\n> A1\t\tempty\n> A2\t\tempty\n')
#  embed.add_field(name = "Beta", value =  f'> TL\t\tempty\n> B1\t\tempty\n> B2\t\tempty\n')
#  embed.add_field(name = "Delta", value = f'> TL\t\tempty\n> D1\t\tempty\n> D2\t\tempty\n')
#  embed.add_field(name = "Echo", value =  f'> TL\t\tempty\n> E1\t\tempty\n> E2\t\tempty\n')
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

def set_team(embed, team, slots, in_line = False):
  text = ''
  for i in slots.split(','):
    text += f'''> {i} empty\n'''
  embed.add_field(name = team, value = f'{text}', inline = in_line)
  return embed

def rm_team(embed, team):
  new_embed = discord.Embed(title = embed.title)
  for f in embed.fields:
    if f.name == team:
      continue
    new_embed.add_field(name = f.name, value = f.value, inline = f.inline)
  return new_embed

def check_zeus(embed, user):
  for f in embed.fields:
    if f.name == 'Zeus':
      if f.value == user:
        return True
      else:
        return False
