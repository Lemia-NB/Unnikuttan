import discord
import os
import requests
intents = discord.Intents.all()

#establish connection with discord client
client = discord.Client(intents=intents)

#on_message events
@client.event
async def on_message(message):
  print(message.id)
  if message.author == client.user:
    return

  if message.content.startswith("$integrate"):
    url = message.content.split()[1]
    apikey = message.content.split()[2]
    headers={'Authorization': "Bearer {}".format(apikey)}
    response = requests.get(url, headers=headers)
    print(response.json())
    
    await message.channel.send('Integration success')

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  
#to establish connection with client using bot token
client.run(os.environ['TOKEN'])
