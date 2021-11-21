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
    client.unload_extension("cogs.Events")
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

@client.event
async def on_message_delete(message):
        if message.content.startswith(".say"):
            return
        else:
            pass
        if not message.author.bot:
            pass
        else:
            return
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        guild = client.guilds[0]
        channel = message.channel
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
        if bool(log) == True:
        # with open('F:\\bot\\logs\\log.txt', 'a') as f:
        #     f.write(f'[{current_time}]Message deleted by {snipe_message_author[channel.id]}.\n   Content:{snipe_message_content[channel.id]}\n')
        #     f.close()
            if message.guild.id == 876826249207640096:
                c = client.get_channel(881181406582165525)
                em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
                em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
                await c.send(embed = em)
            else:
                pass
        else:
            pass

@client.event
async def on_message_edit(message_before, message_after):
        global author
        author = message_before.author
        guild = message_before.guild.id
        channel = message_before.channel
        global before
        before = message_before.content
        global after
        after = message_after.content
        if bool(log):
            if guild == 876826249207640096:
                c = client.get_channel(881199227190013992)
                em = discord.Embed(description = f"**Message before**: {message_before.content}\n**Message after**: {message_after.content}")
                em.set_footer(text = f"This message was edited by {message_before.author}")
                await c.send(embed = em)
            else:
                pass
        else:
            pass


@client.event
async def on_guild_join(guild):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} guilds | .help"))

@client.event
async def on_guild_remove(guild):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} guilds | .help"))
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
