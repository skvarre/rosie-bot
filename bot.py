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
    global latest_author
    global command
    if message.author == client.user:
        return

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
        elif command[0] == '!rep':
            latest_author = message.author
            command = 'rep'
            answer = await message.channel.send(print_rep_message())
            await answer.add_reaction('1️⃣')
            await answer.add_reaction('2️⃣')
            await answer.add_reaction('❌')

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return
    if user == latest_author and command == 'rep':
        await rep_planerare(reaction)
        

async def rep_planerare(reaction):
    if reaction.emoji == '1️⃣':
            answer = await reaction.message.channel.send(check_availability())
            # Add reaction for each day of the week
            await answer.add_reaction('🇲')
            await answer.add_reaction('🇹')
            await answer.add_reaction('🇴')
            await answer.add_reaction('✝️')
            await answer.add_reaction('🇫')
            await answer.add_reaction('🇱')
            await answer.add_reaction('🇸')
            await reaction.message.delete()
    elif reaction.emoji == '2️⃣':
            await reaction.message.channel.send("Du valde 2")
    elif reaction.emoji == '❌':
            await reaction.message.delete()

client.run(TOKEN)

