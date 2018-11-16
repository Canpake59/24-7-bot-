import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
hero = ['Zen', 'Mercy', 'Ana', 'Lucio', 'Brigitte', 'Moira', 'Sym', 'Torb', 'Doomfist', 'Sombra', 'Tracer', 'Genji', 'Hanzo', 'Bastion', 'Widowmaker', 'Soldier: 76', 'Mccree', 'Ashe', 'Junkrat', 'Reaper', 'Pharah', 'Mei', 'D.va', 'Winston', 'Hammond', 'Rein', 'Zarya', 'Roadhog', 'Orisa']

Client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.content.lower().startswith("!!"):
        userID = message.author.id
        command = message.content[2:]
        if command == "bat":
            await client.send_message(message.channel, "<@%s> Do you want a random hero? !!y for yes, !!comp for a normal 2:2:2 comp, or type !!six for a team of 6 random heroes." % (userID))
        if command == "y":
            await client.send_message(message.channel,(random.choice(hero)))   
        if command == "six":
            random.shuffle(hero)
            await client.send_message(message.channel,(hero[:6]))
        if command == "comp":
            support = ['Zen', 'Mercy', 'Ana', 'Lucio', 'Brigitte', 'Moira']
            damage = ['Sym', 'Torb', 'Doomfist', 'Sombra', 'Tracer', 'Genji', 'Hanzo', 'Bastion', 'Widowmaker', 'Daddy: 76', 'Mccree', 'Ashe', 'Junkrat', 'Reaper', 'Pharah', 'Mei']
            tank = ['D.va', 'Winston', 'Hammond', 'Rein', 'Zarya', 'Roadhog', 'Orisa']
            random.shuffle(support)
            random.shuffle(damage)
            random.shuffle(tank)
            await client.send_message(message.channel,(support[:2]))
            await client.send_message(message.channel,(damage[:2]))
            await client.send_message(message.channel,(tank[:2]))

client.run("NTEzMTE4NTA2MTM3NjgxOTIw.DtDW2w.gflGncV7QD1N4SeGBRRploEf-vg")
