### Modules ###
import os
import sys
import time
import praw
import math
import random
import pickle
import string
import os.path
import discord
import json
import asyncio
import datetime
import requests
import threading
import traceback
import itertools
import youtube_dl
from time import sleep
import multiprocessing
from random import randint
from functools import partial
from discord.utils import get
from discord.ext import tasks
from discord import TextChannel
from discord.ext import commands
from youtube_dl import YoutubeDL
from async_timeout import timeout
from discord.ext.commands import *
from discord import FFmpegPCMAudio
from discord.voice_client import VoiceClient
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
### Modules end ###

### Startup/variables ###
console = False
log = True
intents = discord.Intents.all()
errHandlerVer = 'v1.1'
botVer = 'v1.3'
currencyVer = 'v1.0'
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
client = commands.Bot(command_prefix=".", intents=intents)
slash = SlashCommand(client, sync_commands=False)
global startTime
startTime = time.time()
client.remove_command('help')
cwd = os.getcwd()

class Data: 
    def __init__(self, wallet, bank, xp, level, warnings, swearFilter, isBlacklisted, passiveMode):
        self.wallet = wallet        
        self.bank = bank
        self.xp = xp
        self.level = level
        self.warnings = warnings
        self.swearFilter = swearFilter
        self.isBlacklisted = isBlacklisted
        self.passiveMode = passiveMode

## Events ###
@client.event
async def on_ready():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} guilds | .help"))
    print('Bot is online')
    print('==================')
    print('Bot config:')
    print('------------------')
    print(f'Ping: {round(client.latency * 1000)}')
    print('------------------')
    boot = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    print(f'Startup time: {boot}')
    print('------------------')
    print(f'Server count: {str(len(client.guilds))}')
    print('------------------')
### Events end ###

# cwd = os.getcwd()                                          
# data_filename = f"{cwd}/data.db"

# def load_data():
#     if os.path.isfile(data_filename):                     
#         if os.path.getsize(data_filename) > 0: 
#             with open(data_filename, "rb") as file:
#                 pickle.load(file)
#     else:
#         return dict()

# def load_member_data(user_id:int):
#     data = load_data()

#     if user_id not in data:
#         return Data(0, 0, 0, 0, 0, 0, 0, 0)
#     return data[user_id]

# def save_member_data(user_id, member_data):
#     data = load_data()

#     data[user_id] = member_data

#     with open(data_filename, "wb") as file:
#         pickle.dump(data, file)

@client.command()
async def load(ctx, *, arg1):
    if ctx.message.author.id == 705462972415213588:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        return
    client.load_extension(f'cogs.{arg1}')
    await ctx.send("Loaded Cog")

@client.command()
async def unload(ctx, *, arg1):
    if ctx.message.author.id == 705462972415213588:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        return
    client.unload_extension(f'cogs.{arg1}')
    await ctx.send("Unloaded Cog")


@client.command()
async def reload(ctx, *, arg1):
    if ctx.message.author.id == 705462972415213588:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        return
    client.unload_extension(f'cogs.{arg1}')
    client.load_extension(f'cogs.{arg1}')
    await ctx.send("Reloaded Cog")

client.run("ODU5ODY5OTQxNTM1OTk3OTcy.YNy-SQ.WBkUfwsxxaBfUnvGmPvuViqXyrE")
