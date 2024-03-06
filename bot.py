# bot.py
import os

import discord
from dotenv import load_dotenv
from bot_functions import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        # split message content by spaces
        command = message.content.split(' ')
        # if the first word after / is 'hello'
        if command[0] == '!help':
            # send a message to the channel
            await message.channel.send(print_help_message())
        # if the first word after / is 'bye'
        elif command[0] == '!voff':
            # send a message to the channel
            await message.channel.send(print_voff_message())
    

client.run(TOKEN)
