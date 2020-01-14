# bot.py
import os
import subprocess
import json
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
DEVICE_MODEL_ID = os.getenv('DEVICE_MODEL_ID')
DEVICE_ID = os.getenv('DEVICE_ID')

client = discord.Client()

# @client.event
# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})\n'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    batcmd='python ../Assistant/talk.py --query "'+message.content+'" --device-model-id '+DEVICE_MODEL_ID+' --device-id '+ DEVICE_ID + ''
    result = subprocess.check_output(batcmd)
    with open('out.json', 'r') as in_f:
        data = json.load(in_f)
    await message.channel.send(data['string'])

client.run(TOKEN)