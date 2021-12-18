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
import asyncio
import datetime
import json
import requests
import threading
import prawcore
import aiohttp
import traceback
from time import sleep
from random import randint
from discord.utils import get
from discord.ext import tasks
from discord import TextChannel
from discord.ext import commands
from async_timeout import timeout
from discord.ext.commands import *
### Modules end ###
on_cooldown = {}
cd = {}
work_cooldown = 1700
invest_time = 18000
no_invest_cooldown = [
    705462972415213588,
    884765170184896562
]
ids = [
    738290097170153472,
    705462972415213588,
    695640751933096027,
    706697300872921088,
    884765170184896562
]
beta = [
    778241840562044960
]
bad = [
    "fuck",
    "dick",
    "nigga",
    "nigger",
    "cock",
    "asshole",
    "bitch"
]
links = [
    "https://",
    "http://"
    "www."
    "ww1.",
    "www1.",
    "ww2.",
    "www2"
]
global startTime
startTime = time.time()
owner = 'thatOneArchUser#5794'
cwd = os.getcwd()  
data_filename = f"{cwd}/data.db"
currency = True
client = commands.Bot
log = True
reddit = praw.Reddit(client_id='_pazwWZHi9JldA',
                     client_secret='1tq1HM7UMEGIro6LlwtlmQYJ1jB4vQ',
                     user_agent='idk', check_for_async=False)

class colors: 
    cyan = '\033[96m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

with open(f'{cwd}/database/wallet.json', 'r') as f:
    global wallet
    wallet = json.load(f)
with open(f'{cwd}/database/bank.json', 'r') as f:
    global bank
    bank = json.load(f)
with open(f'{cwd}/database/swearfilter.json', 'r') as f:
    global swearfilter
    swearfilter = json.load(f)
with open(f'{cwd}/database/passiveUsers.json', 'r') as f:
    global passiveUsers
    passiveUsers = json.load(f)
with open(f'{cwd}/database/warnings.json', 'r') as f:
    global warnings
    warnings = json.load(f)
with open(f'{cwd}/database/levels.json', 'r') as f:
    global levels
    levels = json.load(f)
with open(f'{cwd}/database/xp.json', 'r') as f:
    global xp
    xp = json.load(f)
with open(f'{cwd}/database/windows10.json', 'r') as f:
    global windows10
    windows10 = json.load(f)
with open(f'{cwd}/database/bronzecoin.json', 'r') as f:
    global bronzecoin
    bronzecoin = json.load(f)
with open(f'{cwd}/database/silvercoin.json', 'r') as f:
    global silvercoin
    silvercoin = json.load(f)
with open(f'{cwd}/database/goldcoin.json', 'r') as f:
    global goldcoin
    goldcoin = json.load(f)
with open(f'{cwd}/database/jobs.json', 'r') as f:
    global jobs
    jobs = json.load(f)
with open(f'{cwd}/database/invest.json', 'r') as f:
    global invest
    invest = json.load(f)
with open(f'{cwd}/database/devbox.json', 'r') as f:
    global devbox
    devbox = json.load(f)
with open(f'{cwd}/database/dailybox.json', 'r') as f:
    global dailybox
    dailybox = json.load(f)
with open(f'{cwd}/database/link.json', 'r') as f:
    global link
    link = json.load(f)
with open(f'{cwd}/database/normalbox.json', 'r') as f:
    global normalbox
    normalbox = json.load(f)

### Commands ###
class MainCog(commands.Cog):
    def __init__(self, client : commands.Bot):
        self.client = client

    def load(self):
        return

    def save(self):
        with open(f'{cwd}/database/wallet.json', 'w+') as f:
            json.dump(wallet, f)
        with open(f'{cwd}/database/bank.json', 'w+') as f:
            json.dump(bank, f)
        with open(f'{cwd}/database/xp.json', 'w+') as f:
            json.dump(xp, f)
        with open(f'{cwd}/database/levels.json', 'w+') as f:
            json.dump(levels, f)
        with open(f'{cwd}/database/passiveUsers.json', 'w+') as f:
            json.dump(passiveUsers, f)
        with open(f'{cwd}/database/warnings.json', 'w+') as f:
            json.dump(warnings, f)
        with open(f'{cwd}/database/wallet.json', 'w+') as f:
            json.dump(wallet, f)
        with open(f'{cwd}/database/swearfilter.json', 'w+') as f:
            json.dump(swearfilter, f)
        with open(f'{cwd}/database/windows10.json', 'w+') as f:
            json.dump(windows10, f)
        with open(f'{cwd}/database/bronzecoin.json', 'w+') as f:
            json.dump(bronzecoin, f)
        with open(f'{cwd}/database/silvercoin.json', 'w+') as f:
            json.dump(silvercoin, f)
        with open(f'{cwd}/database/goldcoin.json', 'w+') as f:
            json.dump(goldcoin, f)
        with open(f'{cwd}/database/jobs.json', 'w+') as f:
            json.dump(jobs, f)
        with open(f'{cwd}/database/invest.json', 'w+') as f:
            json.dump(invest, f)
        with open(f'{cwd}/database/devbox.json', 'w+') as f:
            json.dump(devbox, f)
        with open(f'{cwd}/database/dailybox.json', 'w+') as f:
            json.dump(dailybox, f)
        with open(f'{cwd}/database/link.json', 'w+') as f:
            json.dump(link, f)
        with open(f'{cwd}/database/normalbox.json', 'w+') as f:
            json.dump(normalbox, f)

    def convert(self, time):
        pos = ["s", "m", "h", "d", "w"]
        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24, "w": 3600 * 24 * 7}
        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        global author
        author = message_before.author
        guild = message_before.guild.id
        channel = message_before.channel
        global before
        before = message_before.content
        global after
        after = message_after.content

    @commands.Cog.listener()
    async def on_message(self, message): 
        if not message.author.bot:
            self.load()
            if "705462972415213588" not in jobs:
                jobs["705462972415213588"] = "ab"
            if str(message.guild.id) in swearfilter:
                pass
            else:
                swearfilter[str(message.guild.id)] = 0
            if str(message.author.id) in invest:
                pass
            else:
                invest[str(message.author.id)] = 0
            if str(message.author.id) in xp:
                xp[str(message.author.id)] += 1
            else:
                xp[str(message.author.id)] = 1
            if str(message.author.id) in levels:
                pass
            else:
                levels[str(message.author.id)] = 1
            if str(message.author.id) in wallet:
                pass
            else:
                wallet[str(message.author.id)] = 0
            if str(message.author.id) in bank:
                pass
            else:
                bank[str(message.author.id)] = 0
            if str(message.author.id) in passiveUsers:
                pass
            else:
                passiveUsers[str(message.author.id)] = 0
            if str(message.author.id) in windows10:
                pass
            else:
                windows10[str(message.author.id)] = 0
            if str(message.author.id) in bronzecoin:
                pass
            else:
                bronzecoin[str(message.author.id)] = 0
            if str(message.author.id) in silvercoin:
                pass
            else:
                silvercoin[str(message.author.id)] = 0
            if str(message.author.id) in goldcoin:
                pass
            else:
                goldcoin[str(message.author.id)] = 0
            if str(message.author.id) in devbox:
                pass
            else:
                devbox[str(message.author.id)] = 0
            if str(message.author.id) in dailybox:
                pass
            else:
                dailybox[str(message.author.id)] = 0
            if str(message.guild.id) not in link:
                link[str(message.guild.id)] = 0
            xpreq = 0
            if levels[str(message.author.id)] == 1:
                xpreq = 25
            else:             
                for level in range(int(levels[str(message.author.id)])):
                    xpreq += 25
                    if xpreq >= 5000:
                        break
                    else:
                        pass
            if int(xp[str(message.author.id)]) >= xpreq:
                xp[str(message.author.id)] -= xp[str(message.author.id)]
                levels[str(message.author.id)] += 1
                await message.channel.send(f"{message.author.mention} You just leveled up to level **{levels[str(message.author.id)]}**!")
            else:
                pass
            xpreq = 0
            self.save()
            if any(x in message.content.lower() for x in bad):
                if str(message.author.id) not in warnings:
                    warnings[str(message.author.id)] = 0
                if str(message.guild.id) not in swearfilter:
                    swearfilter[str(message.guild.id)] = 0
                if swearfilter[str(message.guild.id)] == 1:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} Watch your language")
                    warnings[str(message.author.id)] += 1
                    self.save()                                                             
                else:
                    pass
            if any(x in message.content.lower() for x in links):
                if str(message.author.id) not in warnings:
                    warnings[str(message.author.id)] = 0
                if str(message.guild.id) not in link:
                    link[str(message.guild.id)] = 0
                if link[str(message.guild.id)] == 1:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} No links")
                    warnings[str(message.author.id)] += 1
                    self.save()
                else:
                    pass
            else:   
                pass
        #await self.client.process_commands(message)
    
    @commands.command()
    async def pulldb(self, ctx):
        if ctx.message.author.id == 705462972415213588:
            channel = await ctx.message.author.create_dm()
            for filename in os.listdir("./database"):
                if filename.endswith(".json"):
                    #await channel.send(file=discord.File(f"./database/{filename}"))
                     await ctx.send(file=discord.File(f"./database/{filename}"))

    @commands.command()
    async def credits(self, ctx):
        em = discord.Embed(title="Arch bot developers team", description="thatOneArchUser#5794, Main developer\nnotsniped#0002, made purge command, bot administrator\nMarios1Gr#3949, made deposit/withdraw\nαrchιshα#5518, bot administrator\ngalaxy#2203, tester\nxristos_hal#4383, bot administrator", color=discord.Colour.random())
        await ctx.reply(embed=em, mention_author=False)
    
    @commands.command(aliases=["vs"])
    async def viewsettings(self, ctx):
        self.load()
        em = discord.Embed(description=f"Passive mode: {passiveUsers[str(ctx.message.author.id)]}\nSwear filter: {swearfilter[str(ctx.message.guild.id)]}\nLink blocker: {link[str(ctx.message.guild.id)]}", color=discord.Colour.random())
        await ctx.reply(embed=em, mention_author=False)

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def linktoggle(self, ctx):
        if str(ctx.message.guild.id) not in link:
            link[str(ctx.message.guild.id)] = 0
        if link[str(ctx.message.guild.id)] == 0:
            await ctx.reply("Enabled link blocker.")
            link[str(ctx.message.guild.id)] = 1
            self.save()
            return
        elif link[str(ctx.message.guild.id)] == 1:
            await ctx.reply("Disabled link blocker")
            link[str(ctx.message.guild.id)] = 0
            self.save()
            return
    
    @commands.command()
    async def shop(self, ctx):
        color = discord.Colour.random()
        page1 = discord.Embed(
            title=f"Arch bot shop",
            description=f"Windows 10 key\nDescription: Windows 10 lisence key, too expensive for an os\nCost: 69420\nId: `windows10`\n\nBronze coin\nCost: 50000 coins\nId: `bronzecoin`\n\nSilver coin\nCost: 250000 coins\nId: `silvercoin`",
            color=color
        )
        page2 = discord.Embed(
            title=f"Arch bot shop",
            description=f"Gold coin\nCost: 1000000 coins\nId: `goldcoin`\n\nDeveloper box\nCost: 69000000000000 coins\nId: `devbox`\n\nNormal box\nCost: 5000 coins\nId: `normalbox`",
            color=color
        )
        page1.set_footer(text="Tip: type .buy <item_id> [amount] to buy an item")
        page2.set_footer(text="Tip: type .buy <item_id> [amount] to buy an item")
        pages = [
            page1,
            page2
        ]
        message = await ctx.send(embed = page1)
        await message.add_reaction('◀')
        await message.add_reaction('▶')
        def check(reaction, user):
            return user == ctx.author
        i = 0
        reaction = None
        while True:
            if str(reaction) == '◀':
                if i > 0:
                    i -= 1
                    await message.edit(embed = pages[i])
            elif str(reaction) == '▶':
                if i < 1:
                    i += 1
                    await message.edit(embed = pages[i])
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout = 30.0, check = check)
                await message.remove_reaction(reaction, user)
            except:
                break
        await message.clear_reactions()
        
    @commands.command(aliases=['inv'])
    async def inventory(self, ctx, user : discord.User=None):
        self.load()
        if user == None:
            em = discord.Embed(title=f"{ctx.message.author.display_name}'s inventory", description=f"Windows 10 keys: {windows10[str(ctx.message.author.id)]}\nBronze coins: {bronzecoin[str(ctx.message.author.id)]}\nSilver coins: {silvercoin[str(ctx.message.author.id)]}\nGold coins: {goldcoin[str(ctx.message.author.id)]}\nDaily boxes: {dailybox[str(ctx.message.author.id)]}\nDeveloper boxes: {devbox[str(ctx.message.author.id)]}\nNormal boxes: {normalbox[str(ctx.message.author.id)]}", color=discord.Colour.random())
            await ctx.reply(embed=em, mention_author=False)
        else:
            em = discord.Embed(title=f"{user.display_name}'s inventory", description=f"Windows 10 keys: {windows10[str(user.id)]}\nBronze coins: {bronzecoin[str(user.id)]}\nSilver coins: {silvercoin[str(user.id)]}\nGold coins: {goldcoin[str(user.id)]}\nDaily boxes: {dailybox[str(user.id)]}\nDeveloper boxes: {devbox[str(user.id)]}\nNormal boxes: {normalbox[str(user.id)]}", color=discord.Colour.random())
            await ctx.reply(embed=em, mention_author=False)

    @commands.command()
    async def rich(self, ctx):
        def rmmax(rich_id):
            values.remove(max(values))
            keys.remove(rich_id)
        keys = list(wallet.keys())
        values = list(wallet.values())
        rich_id1 = keys[values.index(max(values))]
        user1 = self.client.get_user(int(rich_id1))
        amount1 = max(values)
        rmmax(rich_id1)
        rich_id2 = keys[values.index(max(values))]
        user2 = self.client.get_user(int(rich_id2))
        amount2 = max(values)
        rmmax(rich_id2)
        rich_id3 = keys[values.index(max(values))]
        user3 = self.client.get_user(int(rich_id3))
        amount3 = max(values)
        rmmax(rich_id3)
        rich_id4 = keys[values.index(max(values))]
        user4 = self.client.get_user(int(rich_id4))
        amount4 = max(values)
        rmmax(rich_id4)
        rich_id5 = keys[values.index(max(values))]
        user5 = self.client.get_user(int(rich_id5))
        amount5 = max(values)
        rmmax(rich_id5)
        em = discord.Embed(title="Richest people in arch bot database", description=f"1. {user1}\n{amount1}\n\n2. {user2}\n{amount2}\n\n3. {user3}\n{amount3}\n\n4. {user4}\n{amount4}\n\n5. {user5}\n{amount5}", color=discord.Colour.random()) 
        await ctx.send(embed=em)
  
    @commands.command(aliases=["open"])
    async def use(self, ctx, item:str, amount:int=None):
        if int(amount) >= sys.maxsize:
            await ctx.reply("no more than int64 limit")
            return
        if str(item) == "developer" or str(item) == "devbox":
            if amount == None or int(amount) == 1:
                if int(devbox[str(ctx.message.author.id)]) < 1:
                    await ctx.reply("You don\'t owm this item")
                    return
                else:
                    items = [
                        "coins",
                        "windows10",
                        "goldcoin"
                    ]
                    rnd = random.choice(items)
                    msg = await ctx.reply("Opening developer box...")
                    async with ctx.typing():
                        await asyncio.sleep(2)
                    devbox[str(ctx.message.author.id)] -= 1
                    if rnd == "coins":
                        c = random.randint(100000, 69696969696969)
                        wallet[str(ctx.message.author.id)] += c
                        await msg.edit(content=f"You earned {c} coins from a developer box!")
                        self.save()
                        return
                    elif rnd == "windows10":
                        w = random.randint(69, 69420)
                        windows10[str(ctx.message.author.id)] += w
                        await msg.edit(content=f"You earned {w} windows 10 keys from a developer box!")
                        self.save()
                        return
                    elif rnd == "goldcoin":
                        g = random.randint(6969, 6969420)
                        goldcoin[str(ctx.message.author.id)] += g
                        await msg.edit(content=f"You earned {g} golden coins from a developer box!")
                        self.save()
                        return
            elif int(amount) == 0:
                await ctx.reply(f"Oppened 0 developer boxes and got......................\nNOTHING!!!")
                return
            elif int(amount) < 0:
                await ctx.reply("Don\'t try to break me")
                return
            else:
                if int(devbox[str(ctx.message.author.id)]) < int(amount):
                    await ctx.reply("You don\'t have that many developer boxes")
                    return
                else:
                    items = [
                        "coins",
                        "windows10",
                        "goldcoin"
                    ]
                    c = 0
                    w = 0
                    g = 0
                    for i in range(int(amount)):
                        rnd = random.choice(items)
                        if rnd == "coins":
                            c += 1
                        elif rnd == "windows10":
                            w += 1
                        elif rnd == "goldcoin":
                            g += 1
                    if c != 0:
                        coin0 = random.randint(100000, 69696969696969)
                        coin1 = round(coin0 * c)
                    if w != 0:
                        win0 = random.randint(69, 69420)
                        win1 = round(win0 * w)
                    if g != 0:
                        gold0 = random.randint(6969, 6969420)
                        gold1 = round(gold0 * g)
                    msg = await ctx.reply(f"Opening {amount} developer boxes...")
                    async with ctx.typing():
                        await asyncio.sleep(2)
                    windows10[str(ctx.message.author.id)] += int(win1)
                    wallet[str(ctx.message.author.id)] += int(coin1)
                    goldcoin[str(ctx.message.author.id)] += int(gold1)
                    devbox[str(ctx.message.author.id)] -= int(amount)
                    self.save()
                    embed = discord.Embed(description="You earned:", color=discord.Colour.random())
                    if c != 0:
                        embed.add_field(name="Coins", value=str(coin1))
                        pass
                    if w != 0:
                        embed.add_field(name="Windows 10 keys", value=str(win1))
                        pass
                    if g != 0:
                        embed.add_field(name="Golden coins", value=str(gold1))
                        pass
                    embed.set_footer(text=f"These rewards are from {amount} developer boxes")
                    await msg.edit(embed=embed)
                    return
        elif str(item) == "daily" or str(item) == "dailybox":
            if amount == None or int(amount) == 1:
                if int(dailybox[str(ctx.message.author.id)]) < 1:
                    await ctx.reply("You don\'t own this item")
                    return
                else:
                    items = [
                        "coins",
                        "windows10",
                        "bronzecoin",
                        "silvercoin",
                        "goldcoin"
                    ]
                    rnd = rnd = ''.join(map(str, random.choices(items, weights=[40, 5, 3, 1, 0.5], k=1)))
                    msg = await ctx.reply("Opening daily box...")
                    async with ctx.typing():
                        await asyncio.sleep(2)
                    dailybox[str(ctx.message.author.id)] -= 1
                    if rnd == "coins":
                        c = random.randint(1000, 100000)
                        wallet[str(ctx.message.author.id)] += c
                        await msg.edit(content=f"You earned {c} coins from a daily box!")
                        self.save()
                        return
                    elif rnd == "windows10":
                        w = random.randint(1, 2)
                        windows10[str(ctx.message.author.id)] += w
                        await msg.edit(content=f"You earned {w} windows 10 keys from a daily box!")
                        self.save()
                        return
                    elif rnd == "bronzecoin":
                        b = random.randint(1, 2)
                        bronzecoin[str(ctx.message.author.id)] += b
                        await msg.edit(content=f"You earned {b} bronze coins from a daily box!")
                        self.save()
                        return
                    elif rnd == "silvercoin":
                        s = random.randint(1, 2)
                        silvercoin[str(ctx.message.author.id)] += s
                        await msg.edit(content=f"You earned {s} silver coins from a daily box!")
                        self.save()
                        return
                    elif rnd == "goldcoin":
                        g = random.randint(1, 2)
                        goldcoin[str(ctx.message.author.id)] += g
                        await msg.edit(content=f"You earned {g} golden coins from a daily box!")
                        self.save()
                        return
            elif int(amount) == 0:
                await ctx.reply(f"Oppened 0 daily boxes and got......................\nNOTHING!!!")
                return
            elif int(amount) < 0:
                await ctx.reply("Don\'t try to break me")
                return
            else:
                if int(dailybox[str(ctx.message.author.id)]) < int(amount):
                    await ctx.reply("You don\'t have that many daily boxes")
                    return
                else:
                    items = [
                        "coins",
                        "windows10",
                        "bronzecoin",
                        "silvercoin",
                        "goldcoin"
                    ]
                    c = 0
                    w = 0
                    g = 0
                    b = 0
                    s = 0
                    for i in range(int(amount)):
                        rnd = rnd = rnd = ''.join(map(str, random.choices(items, weights=[40, 5, 3, 1, 0.5], k=1)))
                        if rnd == "coins":
                            c += 1
                        elif rnd == "windows10":
                            w += 1
                        elif rnd == "goldcoin":
                            g += 1
                        elif rnd == "silvercoin":
                            s += 1
                        elif rnd == "bronzecoin":
                            b += 1
                    if c != 0:
                        coin0 = random.randint(1000, 100000)
                        coin1 = round(coin0 * c)
                    if w != 0:
                        win0 = random.randint(1, 2)
                        win1 = round(win0 * w)
                    if g != 0:
                        gold0 = random.randint(1, 2)
                        gold1 = round(gold0 * g)
                    if s != 0:
                        silver0 = random.randint(1, 2)
                        silver1 = round(silver0 * s)
                    if b != 0:
                        b0 = random.randint(1, 2)
                        b1 = round(b0 * b)
                    msg = await ctx.reply(f"Opening {amount} daily boxes...")
                    async with ctx.typing():
                        await asyncio.sleep(2)
                    windows10[str(ctx.message.author.id)] += int(win1)
                    wallet[str(ctx.message.author.id)] += int(coin1)
                    goldcoin[str(ctx.message.author.id)] += int(gold1)
                    dailybox[str(ctx.message.author.id)] -= int(amount)
                    self.save()
                    embed = discord.Embed(description="You earned:", color=discord.Colour.random())
                    if c != 0:
                        embed.add_field(name="Coins", value=str(coin1))
                        pass
                    if w != 0:
                        embed.add_field(name="Windows 10 keys", value=str(win1))
                        pass
                    if g != 0:
                        embed.add_field(name="Golden coins", value=str(gold1))
                        pass
                    embed.set_footer(text=f"These rewards are from {amount} daily boxes")
                    await msg.edit(embed=embed)
                    return
        elif str(item) == "normal" or str(item) == "normalbox":
            if amount == None or int(amount) == 1:
                if int(normalbox[str(ctx.message.author.id)]) < 1:
                    await ctx.reply("You don\'t own this item")
                    return
                else:
                    items = [
                        "coins",
                        "windows10",
                        "bronzecoin",
                        "silvercoin",
                        "goldcoin"
                    ]
                    rnd = rnd = ''.join(map(str, random.choices(items, weights=[40, 2.5, 1.5, 0.5, 0.01], k=1)))
                    msg = await ctx.reply("Opening normal box...")
                    async with ctx.typing():
                        await asyncio.sleep(2)
                    normalbox[str(ctx.message.author.id)] -= 1
                    if rnd == "coins":
                        c = random.randint(1000, 10000)
                        wallet[str(ctx.message.author.id)] += c
                        await msg.edit(content=f"You earned {c} coins from a normal box!")
                        self.save()
                        return
                    elif rnd == "windows10":
                        windows10[str(ctx.message.author.id)] += 1
                        await msg.edit(content=f"You earned 1 windows 10 key from a normal box!")
                        self.save()
                        return
                    elif rnd == "bronzecoin":
                        bronzecoin[str(ctx.message.author.id)] += 1
                        await msg.edit(content=f"You earned 1 bronze coin from a daily box!")
                        self.save()
                        return
                    elif rnd == "silvercoin":
                        silvercoin[str(ctx.message.author.id)] += 1
                        await msg.edit(content=f"You earned silver coin from a daily box!")
                        self.save()
                        return
                    elif rnd == "goldcoin":
                        goldcoin[str(ctx.message.author.id)] += 1
                        await msg.edit(content=f"You earned golden coin from a daily box!")
                        self.save()
                        return
            elif int(amount) == 0:
                await ctx.reply(f"Oppened 0 normal boxes and got......................\nNOTHING!!!")
                return
            elif int(amount) < 0:
                await ctx.reply("Don\'t try to break me")
                return
            else:
                if int(normalbox[str(ctx.message.author.id)]) < int(amount):
                    await ctx.reply("You don\'t have that many normal boxes")
                    return
                elif int(normalbox[str(ctx.message.author.id)]) == 0:
                    await ctx.reply("You don\'t own this item")
                    return
                else:
                    items = [
                        "coins",
                        "windows10",
                        "bronzecoin",
                        "silvercoin",
                        "goldcoin"
                    ]
                    c = 0
                    w = 0
                    g = 0
                    b = 0
                    s = 0
                    for i in range(int(amount)):
                        rnd = rnd = ''.join(map(str, random.choices(items, weights=[40, 2.5, 1.5, 0.5, 0.01], k=1)))
                        if rnd == "coins":
                            c += 1
                        elif rnd == "windows10":
                            w += 1
                        elif rnd == "goldcoin":
                            g += 1
                        elif rnd == "silvercoin":
                            s += 1
                        elif rnd == "bronzecoin":
                            b += 1
                    if c != 0:
                        coin0 = random.randint(1000, 10000)
                        coin1 = round(coin0 * c)
                    if w != 0:
                        win0 = 1
                        win1 = round(win0 * w)
                    if g != 0:
                        gold0 = 1
                        gold1 = round(gold0 * g)
                    if s != 0:
                        silver0 = 1
                        silver1 = round(silver0 * s)
                    if b != 0:
                        b0 = 1
                        b1 = round(b0 * b)
                    msg = await ctx.reply(f"Opening {amount} normal boxes...")
                    async with ctx.typing():
                        await asyncio.sleep(2)
                    windows10[str(ctx.message.author.id)] += int(win1)
                    wallet[str(ctx.message.author.id)] += int(coin1)
                    goldcoin[str(ctx.message.author.id)] += int(gold1)
                    normalbox[str(ctx.message.author.id)] -= int(amount)
                    self.save()
                    embed = discord.Embed(description="You earned:", color=discord.Colour.random())
                    if c != 0:
                        embed.add_field(name="Coins", value=str(coin1))
                        pass
                    if w != 0:
                        embed.add_field(name="Windows 10 keys", value=str(win1))
                        pass
                    if g != 0:
                        embed.add_field(name="Golden coins", value=str(gold1))
                        pass
                    embed.set_footer(text=f"These rewards are from {amount} normal boxes")
                    await msg.edit(embed=embed)
                    return
        else:
            await ctx.reply(f"No such item: {item}")
            return
                    
    @commands.command()
    async def add_item(self, ctx, user : discord.User, item:str, amount:int=None):
        self.load()
        if ctx.message.author.id not in ids:
            await ctx.reply("You cant use this")
            return
        else:
            if str(item) == "windows10":
                if amount == None or int(amount) == 1:
                    if str(user.id) not in windows10:
                        windows10[str(user.id)] = 0
                        self.save()
                    windows10[str(user.id)] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `windows10` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    if str(user.id) not in windows10:
                        windows10[str(user.id)] = 0
                        self.save()
                    windows10[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} windows 10 keys to {user.display_name}")
                    return
            elif str(item) == "normalbox":
                if amount == None or int(amount) == 1:
                    if str(user.id) not in normalbox:
                        normalbox[str(user.id)] = 0
                        self.save()
                    normalbox[str(user.id)] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `normalbox` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    if str(user.id) not in normalbox:
                        normalbox[str(user.id)] = 0
                        self.save()
                    normalbox[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} normal boxes to {user.display_name}")
                    return
            elif str(item) == "bronzecoin":
                if amount == None or int(amount) == 1:
                    if str(user.id) not in bronzecoin:
                        bronzecoin[str(user.id)] = 0
                        self.save()
                    bronzecoin[str(user.id)] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `bronzecoin` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    if str(user.id) not in bronzecoin:
                        bronzecoin[str(user.id)] = 0
                        self.save()
                    bronzecoin[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} bronze coins to {user.display_name}")
                    return
            elif str(item) == "silvercoin":
                if amount == None or int(amount) == 1:
                    if str(user.id) not in silvercoin:
                        silvercoin[str(user.id)] = 0
                        self.save()
                    silvercoin[str(user.id)] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `silvercoin` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    if str(user.id) not in silvercoin:
                        silvercoin[str(user.id)] = 0
                        self.save()
                    silvercoin[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} silver coins to {user.display_name}")
                    return
            elif str(item) == "goldcoin":
                if amount == None or int(amount) == 1:
                    if str(user.id) not in goldcoin:
                        goldcoin[str(user.id)] = 0
                        self.save()
                    goldcoin[str(user.id)] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `goldcoin` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    if str(user.id) not in goldcoin:
                        goldcoin[str(user.id)] = 0
                        self.save()
                    goldcoin[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} gold coins to {user.display_name}")
                    return
            elif str(item) == "devbox":
                if amount == None or int(amount) == 1:
                    if str(user.id) not in devbox:
                        devbox[str(user.id)] = 0
                        self.save()
                        pass
                    devbox[str(user.id)] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `developer box` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    if str(user.id) not in devbox:
                        devbox[str(user.id)] = 0
                        self.save()
                    devbox[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} developer boxes to {user.display_name}")
                    return
            elif str(item) == "dailybox":
                if amount == None or int(amount) == 1:
                    if str(user.id) not in dailybox:
                        dailybox[str(user.id)] = 0
                        self.save()
                        pass
                    dailybox[str(user.id)] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `daily box` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    if str(user.id) not in dailybox:
                        devbox[str(user.id)] = 0
                        self.save()
                    dailybox[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} daily boxes to {user.display_name}")
                    return
            elif str(item) == "all":
                if amount == None or int(amount) == 1:
                    if str(user.id) not in windows10:
                        windows10[str(user.id)] = 0
                    if str(user.id) not in bronzecoin:
                        bronzecoin[str(user.id)] = 0
                    if str(user.id) not in silvercoin:
                        silvercoin[str(user.id)] = 0
                    if str(user.id) not in goldcoin:
                        goldcoin[str(user.id)] = 0
                    if str(user.id) not in devbox:
                        devbox[str(user.id)] = 0
                    if str(user.id) not in dailybox:
                        dailybox[str(user.id)] = 0
                    if str(user.id) not in normalbox:
                        normalbox[str(user.id)] = 0
                    self.save()
                    windows10[str(user.id)] += 1
                    bronzecoin[str(user.id)] += 1
                    silvercoin[str(user.id)] += 1
                    goldcoin[str(user.id)] += 1
                    devbox[str(user.id)] += 1
                    dailybox[str(user.id)] += 1
                    normalbox[str(user.id)] += 1
                    self.save()
                    await ctx.reply(f"Added all items once in {user.display_name}\'s profile", mention_author=False)
                    return
                else:
                    if str(user.id) not in windows10:
                        windows10[str(user.id)] = 0
                    if str(user.id) not in bronzecoin:
                        bronzecoin[str(user.id)] = 0
                    if str(user.id) not in silvercoin:
                        silvercoin[str(user.id)] = 0
                    if str(user.id) not in goldcoin:
                        goldcoin[str(user.id)] = 0
                    if str(user.id) not in devbox:
                        devbox[str(user.id)] = 0
                    if str(user.id) not in dailybox:
                        dailybox[str(user.id)] = 0
                    if str(user.id) not in normalbox:
                        normalbox[str(user.id)] = 0
                    self.save()
                    windows10[str(user.id)] += int(amount)
                    bronzecoin[str(user.id)] += int(amount)
                    silvercoin[str(user.id)] += int(amount)
                    goldcoin[str(user.id)] += int(amount)
                    devbox[str(user.id)] += int(amount)
                    dailybox[str(user.id)] += int(amount)
                    normalbox[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"Added all items {amount} times in {user.display_name}\'s profile", mention_author=False)
                    return
            else:
                await ctx.reply("No such item")

    @commands.command()
    @commands.has_role("Giveaways")
    async def giveaway(self, ctx):
        embedq1 = discord.Embed(title=":gift: | setup",
                                description=f"Answer the following questions to settup the giveaway")
        embedq1.add_field(name=":star: | Question 1",
                          value="Where should we host the Giveaway?\n\n **Example**: `#general`")
        embedq2 = discord.Embed(title=":gift: | setup",
                                description="Great! Let's move onto the next question.")
        embedq2.add_field(name=":star: | Question 2",
                          value="How long should it last? ``<s|m|h|d|w>``\n\n **Example**:\n `1d`")
        embedq3 = discord.Embed(title=":gift: | setup",
                                description="Awesome. You've made it to the last question!")
        embedq3.add_field(name=":star: | Question 3",
                          value="What is the prize the winner will receive?\n\n **Example**:\n `nitro`")

        questions = [embedq1,
                     embedq2,
                     embedq3]

        answers = []

        def check(msg):
                return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

        for i in questions:
            await ctx.send(embed=i)

            try:
                msg = await self.client.wait_for('message', check=check)
            except asyncio.TimeoutError:
                embed = discord.Embed(title=":gift: **Giveaway Setup**",
                                      description=":x: You didn't answer in time!")
                await ctx.send(embed=embed)
                return
            else:
                answers.append(msg.content)

        try:
            c_id = int(answers[0][2: -1])
        except:
            embed = discord.Embed(title=":gift: **Giveaway setup**",
                                  description=":x: You didnt mention a channel correctly!")
            await ctx.send(embed=embed)
            return

        channel = self.client.get_channel(c_id)

        time = self.convert(answers[1])
        if time == -1:
            embed = discord.Embed(title=":gift: **Giveaway setup**",
                                  description=":x: You didnt setup time properly!")
            await ctx.send(embed=embed)
            return
        elif time == -2:
            embed = discord.Embed(title=":gift: **Giveaway setup**",
                                  description=":x: Time must be an integer")
            await ctx.send(embed=embed)
            return
        prize = answers[2]

        embed = discord.Embed(title=":gift: **Giveaway setup**",
                              description="Done, the giveaway is starting..")
        embed.add_field(name="Hosted Channel:", value=f"{channel.mention}")
        if answers[1].endswith("s"):
            embed.add_field(name="Time:", value=f"{answers[1][:-1]} seconds")
        elif answers[1].endswith("m"):
            embed.add_field(name="Time:", value=f"{answers[1][:-1]} minutes")
        elif answers[1].endswith("h"):
            embed.add_field(name="Time:", value=f"{answers[1][:-1]} hours")
        elif answers[1].endswith("d"):
            embed.add_field(name="Time:", value=f"{answers[1][:-1]} days")
        elif answers[1].endswith("w"):
            embed.add_field(name="Time:", value=f"{answers[1][:-1]} weeks")
        embed.add_field(name="Prize:", value=prize)
        await ctx.send(embed=embed)
        print(
            f"New Giveaway Started! Hosted By: {ctx.message.author.display_name} | Hosted Channel: {channel.id} | Time: {answers[1]} | Prize: {prize}")
        print("------")
        embed = discord.Embed(title=f":gift: **GIVEAWAY FOR: {prize}**",
                              description=f"React With 🎉 To Participate!")
        embed.add_field(name="Lasts:", value=answers[1])
        embed.add_field(name=f"Hosted By:", value=ctx.author.mention)
        msg = await channel.send(embed=embed)

        await msg.add_reaction("🎉")
        await asyncio.sleep(time)

        new_msg = await channel.fetch_message(msg.id)
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)
        amogus = True
        if amogus == True:
            await channel.send(f":tada: Congratulations! {winner.mention} won: **{prize}**!")
            print(f"New Winner! User: {winner.mention} | Prize: {prize}")
            print("------")

        embed2 = discord.Embed(title=f":gift: **GIVEAWAY FOR: {prize}**",
                               description=f":trophy: **Winner:** {winner.mention}")
        embed2.set_footer(text="Giveaway Has Ended")
        await msg.edit(embed=embed2)

    @commands.command()
    @commands.has_role("Giveaways")
    async def reroll(self, ctx, channel: discord.TextChannel, id_: int):
        try:
            new_msg = await channel.fetch_message(id_)
            users = await new_msg.reactions[0].users().flatten()
            users.pop(users.index(self.client.user))
            winner = random.choice(users)
            await ctx.channel.send(f":tada: The new winner is: {winner.mention}!")
        except Exception as e:
            await ctx.send(f"An error occured: {e}")

    @reroll.error
    async def reroll_error(self, error, ctx):
        if isinstance(error, commands.MissingRole):
            await ctx.reply("You need a role named \"Giveaways\" to run this command")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Command usage: `.reroll <channel_id> <message_id>`")

    @commands.command(pass_context=True)
    async def poll(self, ctx, question, *options: str):
        if len(options) <= 1:
            await ctx.send('You need more than one option to make a poll')
            returnnest_asyncio.apply()
        if len(options) > 10:
            await ctx.send('You cant make a poll for more than 10 options')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description))
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
        embed.set_footer(text='poll ID: {}'.format(react_message.id))
        await react_message.edit(embed=embed)

    @commands.command()
    async def buy(self, ctx, item:str, amount:int=None):
        self.load()
        if str(item) == "windows10":
            if amount == None or int(amount) == 1:
                if wallet[str(ctx.message.author.id)] < 69420:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {round(69420 - wallet[str(ctx.message.author.id)])} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a windows 10 key! Now you have {round(wallet[str(ctx.message.author.id)] - 69420)} coins in your wallet.", mention_author=False)
                    wallet[str(ctx.message.author.id)] -= 69420
                    windows10[str(ctx.message.author.id)] += 1
                    self.save()
                    return
            elif int(amount) < 0:
                await ctx.reply("Don\'t try to break me **dood**")
                return
            elif int(amount) == 0:
                await ctx.reply("Here you go, 0 windows 10 keys for 0 coins!")
                return
            else:
                a = 69420 * amount
                if wallet[str(ctx.message.author.id)] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - wallet[str(ctx.message.author.id)]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} windows 10 keys for {a} coins. Now you have {wallet[str(ctx.message.author.id)] - a} coins in your wallet")
                    wallet[str(ctx.message.author.id)] -= a
                    windows10[str(ctx.message.author.id)] += amount
                    self.save()
                    return
        if str(item) == "bronzecoin":
            if amount == None or int(amount) == 1:
                if wallet[str(ctx.message.author.id)] < 50000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {50000 - wallet[str(ctx.message.author.id)]} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a bronze coin! Now you have {wallet[str(ctx.message.author.id)] - 50000} coins in your wallet.", mention_author=False)
                    wallet[str(ctx.message.author.id)] -= 50000
                    bronzecoin[str(ctx.message.author.id)] += 1
                    self.save()
                    return
            elif int(amount) < 0:
                await ctx.reply("Don\'t try to break me **dood**")
                return
            elif int(amount) == 0:
                await ctx.reply("Here you go, 0 bronze coins for 0 coins!")
                return
            else:
                a = 50000 * amount
                if wallet[str(ctx.message.author.id)] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - wallet[str(ctx.message.author.id)]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} bronze coins for {a} coins. Now you have {wallet[str(ctx.message.author.id)] - a} coins in your wallet")
                    wallet[str(ctx.message.author.id)] -= a
                    bronzecoin[str(ctx.message.author.id)] += amount
                    self.save()
                    return
        if str(item) == "silvercoin":
            if amount == None or int(amount) == 1:
                if wallet[str(ctx.message.author.id)] < 250000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {250000 - wallet[str(ctx.message.author.id)]} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a silver coin! Now you have {wallet[str(ctx.message.author.id)] - 250000} coins in your wallet.", mention_author=False)
                    wallet[str(ctx.message.author.id)] -= 250000
                    bronzecoin[str(ctx.message.author.id)] += 1
                    self.save()
                    return
            elif int(amount) < 0:
                await ctx.reply("Don\'t try to break me **dood**")
                return
            elif int(amount) == 0:
                await ctx.reply("Here you go, 0 silver coins for 0 coins!")
                return
            else:
                a = 250000 * amount
                if wallet[str(ctx.message.author.id)] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - wallet[str(ctx.message.author.id)]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} silver coins for {a} coins. Now you have {wallet[str(ctx.message.author.id)] - a} coins in your wallet")
                    wallet[str(ctx.message.author.id)] -= a
                    silvercoin[str(ctx.message.author.id)] += amount
                    self.save()
                    return
        if str(item) == "goldcoin":
            if amount == None or int(amount) == 1:
                if wallet[str(ctx.message.author.id)] < 1000000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {1000000 - wallet[str(ctx.message.author.id)]} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought gold coin! Now you have {wallet[str(ctx.message.author.id)] - 1000000} coins in your wallet.", mention_author=False)
                    wallet[str(ctx.message.author.id)] -= 1000000
                    goldcoin[str(ctx.message.author.id)] += 1
                    self.save()
                    return
            elif int(amount) < 0:
                await ctx.reply("Don\'t try to break me **dood**")
                return
            elif int(amount) == 0:
                await ctx.reply("Here you go, 0 gold coins for 0 coins!")
                return
            else:
                a = 1000000 * amount
                if wallet[str(ctx.message.author.id)] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - wallet[str(ctx.message.author.id)]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} gold coins for {a} coins. Now you have {wallet[str(ctx.message.author.id)] - a} coins in your wallet")
                    wallet[str(ctx.message.author.id)] -= a
                    goldcoin[str(ctx.message.author.id)] += amount
                    self.save()
                    return
        if str(item) == "devbox":
            if amount == None or int(amount) == 1:
                if wallet[str(ctx.message.author.id)] < 69000000000000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {69000000000000 - wallet[str(ctx.message.author.id)]} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought gold coin! Now you have {wallet[str(ctx.message.author.id)] - 69000000000000} coins in your wallet.", mention_author=False)
                    wallet[str(ctx.message.author.id)] -= 69000000000000
                    devbox[str(ctx.message.author.id)] += 1
                    self.save()
                    return
            elif int(amount) < 0:
                await ctx.reply("Don\'t try to break me **dood**")
                return
            elif int(amount) == 0:
                await ctx.reply("Here you go, 0 developer boxes for 0 coins!")
                return
            else:
                a = 69000000000000 * amount
                if wallet[str(ctx.message.author.id)] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - wallet[str(ctx.message.author.id)]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} developer boxes for {a} coins. Now you have {wallet[str(ctx.message.author.id)] - a} coins in your wallet")
                    wallet[str(ctx.message.author.id)] -= a
                    devbox[str(ctx.message.author.id)] += amount
                    self.save()
                    return
        elif str(item) == "normalbox":
            if amount == None or int(amount) == 1:
                if wallet[str(ctx.message.author.id)] < 5000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {round(5000 - wallet[str(ctx.message.author.id)])} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a normal box! Now you have {round(wallet[str(ctx.message.author.id)] - 5000)} coins in your wallet.", mention_author=False)
                    wallet[str(ctx.message.author.id)] -= 5000
                    normalbox[str(ctx.message.author.id)] += 1
                    self.save()
                    return
            elif int(amount) < 0:
                await ctx.reply("Don\'t try to break me **dood**")
                return
            elif int(amount) == 0:
                await ctx.reply("Here you go, 0 normal boxes for 0 coins!")
                return
            else:
                a = 5000 * amount
                if wallet[str(ctx.message.author.id)] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - wallet[str(ctx.message.author.id)]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} normal boxes for {a} coins. Now you have {wallet[str(ctx.message.author.id)] - a} coins in your wallet")
                    wallet[str(ctx.message.author.id)] -= a
                    normalbox[str(ctx.message.author.id)] += amount
                    self.save()
                    return
        else:
            await ctx.reply(f"No item {item} found. Type `.shop` to get the list of items")
            return
                  
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sweartoggle(self, ctx):
        self.load()
        if int(swearfilter[str(ctx.message.guild.id)]) == 0:
            swearfilter[str(ctx.message.guild.id)] = 1
            self.save()
            await ctx.reply("Enabled swear filter for this server")
        elif int(swearfilter[str(ctx.message.guild.id)]) == 1:
            swearfilter[str(ctx.message.guild.id)] = 0
            self.save()
            await ctx.reply("Disabled swear filter for this server")

    @commands.command(aliases=['goldfish'])
    async def fstab(self, ctx):    
        await ctx.reply('https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg')

    @commands.command(aliases=['xp'])
    async def rank(self, ctx, user : discord.User=None):
        self.load()
        if user == None:
            xpreq = 0
            if levels[str(ctx.message.author.id)] == 0:
                xpreq = 25
            else:
                for level in range(int(levels[str(ctx.message.author.id)])):
                    xpreq += 25
                    if xpreq >= 5000:
                        break
                    else:
                        pass
            embed = discord.Embed(title=f"{ctx.message.author.display_name}'s Rank", color=discord.Colour.random())
            embed.add_field(name="Level", value=str(levels[str(ctx.message.author.id)]))
            xpv = f"{xp[str(ctx.message.author.id)]}/{xpreq}"
            embed.add_field(name="Exp", value=str(xpv))
            embed.set_footer(text=f'Leveling api made by {owner}')
            await ctx.send(embed=embed)
        else:
            xpreq = 0
            if str(user.id) not in levels:
                levels[str(user.id)] = 1
            if str(user.id) not in xp:
                xp[str(user.id)] = 0
            if levels[str(user.id)] == 1:
                xpreq = 25
            else:
                for level in range(int(levels[str(user.id)])):
                    xpreq += 25
                    if xpreq >= 5000:
                        break
                    else:
                        pass
            embed = discord.Embed(title=f"{user.display_name}'s Rank", color=0xff0000)
            embed.add_field(name="Level", value=str(levels[str(user.id)]))
            xpv = f"{xp[str(user.id)]}/{xpreq}"
            embed.add_field(name="Exp", value=str(xpv))
            embed.set_footer(text=f'Leveling api made by {owner}')
            await ctx.send(embed=embed)

    blAdd_xp = True
    @commands.command()
    async def add_xp(self, ctx, user : discord.User, amount:int):
        self.load()
        if str(ctx.message.author.id) not in ids:
            await ctx.reply(f'101% sure that this command doesn\'t exist :eyes:')
        else:
            if amount.isdigit:
                if not currency:
                    return
                else:
                    if str(user.id) not in xp:
                        xp[str(user.id)] = 0
                    xp[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f'Added {amount} xp to {user.display_name}')
            else:
                await ctx.reply(f'{amount} is not a number')

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def passive(self, ctx):
        self.load()
        if passiveUsers[str(ctx.message.author.id)] == 1:
            passiveUsers[str(ctx.message.author.id)] = 0
            self.save()
            await ctx.reply(f"Disabled passive mode")
        else:
            passiveUsers[str(ctx.message.author.id)] = 1
            self.save()
            await ctx.reply(f"Enabled passive mode")

    blEdit_snipe = True
    @commands.command()
    async def edit_snipe(self, ctx): 
        try:
            if any(x in after.lower() for x in bad):
                r = lambda: random.randint(0,255)
                col = '#%02X%02X%02X' % (r(),r(),r())
                em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:||{after}||', color=discord.Colour.random())
                em.set_footer(text=f'This message was edited by {author}\nWARNING: this message contains banned text')
            else:
                em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:{after}', color=discord.Colour.random())
                em.set_footer(text=f'This message was edited by {author}')
            await ctx.send(embed = em)
        except:
            await ctx.reply('No recent edited messages here :eyes:')

    blAdd_lvl = True
    @commands.command()
    async def add_lvl(self, ctx, user : discord.User, *, arg1):
        self.load()
        if ctx.message.author.id not in ids:
            pass
        else:
            if arg1.isdigit:
                if int(arg1) > sys.maxsize:
                    pass
                if str(user.id) not in levels:
                    levels[str(user.id)] = 1
                levels[str(user.id)] += int(arg1)
                self.save()
                await ctx.reply(f"Added {int(arg1)} levels to {user.display_name}")
            else:
                await ctx.reply(f'{arg1} is not a number')

    blInvite = True
    @commands.command()
    async def invite(self, ctx):
        #await ctx.reply('This command is disabled')
        #return
        await ctx.reply("https://discord.com/api/oauth2/authorize?client_id=859869941535997972&permissions=8&scope=bot")
        #await ctx.reply("https://discord.com/api/oauth2/authorize?client_id=881092078132670484&permissions=0&scope=bot")

    blSay = True
    @commands.command()
    async def say(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(f'{text}')

    blUptime = True
    @commands.command()
    async def uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        await ctx.send(uptime)

    @commands.command()
    async def ping(self, ctx):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await ctx.send(f'Pong! My ping is {round(self.client.latency * 1000)}ms')
        if bool(log) == True:
            # with open('F:\\bot\\logs\\log.txt', 'a') as f:
            #     f.write(f'[{current_time}]Bot ping is {round(client.latency * 1000)}ms\n')
            #     f.close()
            pass
        else:
            return

    @commands.command()
    async def help(self, ctx, *, arg1=None):
        colors = [
        0x000000,
        0xff0000,
        0x00ff00,
        0x0000ff,
        0x800080,
        0x00ffff,
        0xbfff00
    ]
        def rndcol():
            rnd = random.choice(colors)
            return int(hex(rnd))
        if arg1 == None:
            helpMain = discord.Embed(title='**COMMAND LIST**', description='Economy\nbeg, balance, daily, weekly, monthly, postmeme, work, guess, give, deposit, withdraw, shop, buy, inventory, passive, highlow, rob, invest, use\n\nModeration\nban, kick, purge, nuke, snipe, warns, sweartoggle, viewsettings, edit_snipe, warn\n\nMisc\nmeme, linuxmeme, softwaregore, ihadastroke, windowsmeme, stroke, say, rank, isSus, kill, slap, 8ball, credits, giveaway, reroll, poll\n\nMusic\nsummon, play, leave, queue, join, volume, now, pause, resume, stop, skip, remove, loop', color=discord.Colour.random())
            helpMain.set_footer(text='*type .help [command] to get more info about a command*')
            await ctx.reply(embed = helpMain)
        elif arg1 == 'beg':
            em1 = discord.Embed(title='\'Beg\' command use', description='Gives an amount of coins to the user.\nCooldown: 30 seconds\nUsage: `.beg`', color=discord.Colour.random())
            await ctx.reply(embed=em1)
        elif arg1 == 'balance' or arg1 == 'bal':
            em2 = discord.Embed(title='\'Balance\' command use', description='Shows the amount of a user\nAliases: bal\nUsage `.balance|.bal` [@user]', color=discord.Colour.random())
            em2.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em2)
        elif arg1 == 'hunt':
            em3 = discord.Embed(title='\'Hunt\' command use', description='Goes for hunting to get moneu\nCooldown: 30 seconds\nUsage: `.hunt`', color=discord.Colour.random())
            await ctx.reply(embed=em3)
        elif arg1 == 'daily':
            em4 = discord.Embed(title='\'Daily\' command use', description='Gives an amount of coins\nCooldown: 1 day\nUsage: `.daily`', color=discord.Colour.random())
            await ctx.reply(embed=em4)
        elif arg1 == 'weekly':
            em5 = discord.Embed(title='\'Weekly\' command use', description='Gives an amount of coins\nCooldown: 1 week\nUsage: `.weekly`', color=discord.Colour.random())
            await ctx.reply(embed=em5)
        elif arg1 == 'monthly':
            em6 = discord.Embed(title='\'Monthly\' command use', description='Gives an amount of coins\nCooldown: 1 month\nUsage: `.monthly`', color=discord.Colour.random())
            await ctx.reply(embed=em6)
        elif arg1 == 'postmeme' or arg1 == 'pm':
            em7 = discord.Embed(title='\'Post meme\' command use', description='Posts a meme and gets money\nCooldown: 40 seconds\nUsage: `.postmeme|.pm`', color=discord.Colour.random())
            await ctx.reply(embed=em7)
        elif arg1 == 'ban':
            em8 = discord.Embed(title='\'Ban\' command use', description='Bans a user from the server\nUsage: `.ban <@user>`\nPermissions needed: ban members', color=discord.Colour.random())
            em8.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em8)
        elif arg1 == 'kick':
            em9 = discord.Embed(title='\'Kick\' command use', description='Kicks a user from the server\nUsage: `.kick <@user>`\nPermissions needed: kick members', color=discord.Colour.random())
            em9.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em9)
        elif arg1 == 'nuke':
            em10 = discord.Embed(title='\'Nuke\' command use', description='Deletes all the messages from a channel\nUsage: `.nuke <#channel>`\nPermissions needed: manage channels', color=discord.Colour.random())
            em10.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em10)
        elif arg1 == 'purge':
            em11 = discord.Embed(title='\'Purge\' command use', description='Deletes an amount of messages in the channel\nUsage: `.purge <amount>`\nPermissions needed: manage messages or manage channels')
            em11.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em11)
        elif arg1 == '8ball':
            em12 = discord.Embed(title='\'8ball\' command use', description='Asks a qustion to the bot and responds with a random answer\nUsage: `.8ball <question>', color=discord.Colour.random())
            em12.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em12)
        elif arg1 == 'meme':
            em13 = discord.Embed(title='\'Meme\' command use', description='Sends a random meme from r/memes\nUsage: `.meme`', color=discord.Colour.random())
            await ctx.reply(embed=em13)
        elif arg1 == 'ihadastroke':
            em14 = discord.Embed(title='\'Ihadastroke\' command use', description='Sends a random image from r/ihadastroke\nUsage: `.ihadastroke`', color=discord.Colour.random())
            await ctx.reply(embed=em14)
        elif arg1 == 'softwaregore' or arg1 == 'sg':
            em15 = discord.Embed(title='\'Softwaregore\' command use', description='Sends a random image from r/softwaregore\nUsage: `.softwaregore|.sg`', color=discord.Colour.random())
            await ctx.reply(embed=em15)
        elif arg1 == 'linuxmeme' or arg1 == 'lm':
            em16 = discord.Embed(title='\'Linuxmeme\' command use', description='Sends a random meme from r/linuxmemes\nUsage: `.linuxmeme|.lm`', color=discord.Colour.random())
            await ctx.reply(embed=em16)
        elif arg1 == 'work':
            em17 = discord.Embed(title='\'Work\' command use', description='Gets a big amount of money\nCooldown: 1 hour (except `.work list`)\nUsage: `.work [list/resign/job_id]`', color=discord.Colour.random())
            await ctx.reply(embed=em17)
        elif arg1 == 'stroke':
            em18 = discord.Embed(title='\'Stroke\' command use', description='Sends a stroke (not irl stroke)\nUsage: `.stroke <amount>`\nAmount limit: 750', color=discord.Colour.random())
            em18.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em18)
        elif arg1 == 'invites':
            em19 = discord.Embed(title='\'Invites\' command use', description='Shows the amount of people the user invited\nUsage: `.invites [user]`', color=discord.Colour.random())
            em19.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em19)
        elif arg1 == 'snipe':
            em20 = discord.Embed(title='\'Snipe\' command use', description='Shows the last deleted message in the channel\nUsage: `.snipe`', color=discord.Colour.random())
            await ctx.reply(embed=em20)
        elif arg1 == 'edit_snipe' or arg1 == 'edit-snipe' or arg1 == 'edit':
            em21 = discord.Embed(title='\'Edit snipe\' command use', description='Shows the last edited message in the channel\nUsage: `.edit_snipe|.edit`\nAvailability: beta only', color=discord.Colour.random())
            await ctx.reply(embed=em21)
        elif arg1 == 'highlow' or arg1 == 'hl':
            em22 = discord.Embed(title='\'Highlow\' command use', description='The bot generates 2 random numbers. The first one doesn\'t send it and the second one does. You have to guess if the hidden number is lower, higher or equal to the sent one\nCooldown: 40 seconds\nUsage: `.highlow|.hl`\nResponses: higher, lower, jackpot', color=discord.Colour.random())
            await ctx.reply(embed=em22)
        elif arg1 == 'kill':
            em23 = discord.Embed(title='\'Kill\' command use', description='*kills* a user\nUsage: `.kill <@user>`', color=discord.Colour.random())
            em23.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em23)
        elif arg1 == 'fstab' or arg1 == 'fstab.goldfish':
            em24 = discord.Embed(title='\'Fstab\' command use', description='Sends the meme fstab.goldfish\nUsage: `.fstab`', color=discord.Colour.random())
            await ctx.reply(embed=em24)
        elif arg1 == 'slap':
            em25 = discord.Embed(title='\'Slap\' command use', description='*slaps* a user\nUsage: `.slap <@user>', color=discord.Colour.random())
            await ctx.reply(embed=em25)
        elif arg1 == 'guess':
            em26 = discord.Embed(title='\'Guess\' command use', description='You have to gues a number from 1 to 10. If you find it you get some coins\nCooldown: 30 seconds\nUsage: `.guess <number>`', color=discord.Colour.random())
            em26.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em26)
        elif arg1 == 'give' or arg1 == 'gift':
            em27 = discord.Embed(title='\'Give\' command use', description='Gives coins to a user mentioned\nUsage: `.give|.gift <@user> <amount> [item]', color=discord.Colour.random())
            em27.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em27)
        elif arg1 == 'isSus' or arg1 == 'sus':
            em28 = discord.Embed(title='\'Sus\' command use', description='Checks if a user is sus\nUsage: `.isSus|.sus <@user>`', color=discord.Colour.random())
            em28.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em28)
        elif arg1 == 'add':
            em29 = discord.Embed(title='\'Add\' command use', description='Adds coins to a user\nAvailability: __developer only__\nUsage: `.add <@user> <amount:int/hex/bin>`', color=discord.Colour.random())
            em29.set_footer(text=f'This command can be only used by {owner}')
            await ctx.reply(embed=em29)
        elif arg1 == 'add_xp':
            em30 = discord.Embed(title='\'Add xp\' command use', description='Adds xp to a user\nAvailability: __developer only__\nUsage: `.add_xp <@user> <amount:int/hex/bin>`', color=discord.Colour.random())
            em30.set_footer(text=f'This command can be only used by {owner}')
            await ctx.reply(embed=em30)
        elif arg1 == 'add_lvl':
            em31 = discord.Embed(title='\'Add levels\' command use', description='Adds levels to a user\nAvailability: __developer only__\nUsage: `.add_lvl <@user> <amount:int/hex/bin>', color=discord.Colour.random())
            em31.set_footer(text=f'This command can be only used by {owner}')
            await ctx.reply(embed=em31)
        elif arg1 == 'fish':
            em32 = discord.Embed(title='\'Fish\' command use', description='Fishes stuff\nCooldown: 30 seconds\nUsage `.fish`', color=discord.Colour.random())
            await ctx.reply(embed=em32)
        elif arg1 == 'deposit' or arg1 == 'dep':
            em33 = discord.Embed(title='\'Deposit\' command use', description='Deposits coins and puts them in the bank\nUsage: `.deposit|.dep <max/all/amount:int>`', color=discord.Colour.random())
            em33.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em33)
        elif arg1 == 'withdraw' or arg1 == 'with':
            em34 = discord.Embed(title='\'Withdraw\' command use', description='Withdraws coins and puts them in the wallet\nUsage: `.withdraw|.with <max/all/amount:int>', color=discord.Colour.random())
            em34.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em34)
        elif arg1 == 'shop':
            em35 = discord.Embed(title='\'Shop\' command use', description='Shows the items in shop\nUsage: `.shop`', color=discord.Colour.random())
            await ctx.reply(embed=em35)
        elif arg1 == 'inventory' or arg1 == 'inv':
            em36 = discord.Embed(title='\'Inventory\' command use', description='Shows a user\'s inventory\nUsage: `.inventory|.inv [@user]', color=discord.Colour.random())
            em36.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em36)
        elif arg1 == 'rob':
            em37 = discord.Embed(title='\'Rob\' command use', description='Robs a user\nUsage: `.rob <@user>`', color=discord.Colour.random())
            em37.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em37)
        elif arg1 == 'networth' or arg1 == 'nw':
            em38 = discord.Embed(title='\'Networth\' command use', description='Shows the networth of a player in hypixel skyblock\nUsage: `.networth|.nw <playername> [profile]', color=discord.Colour.random())
            em38.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em38)
        elif arg1 == 'auctionhouse' or arg1 == 'ah' or arg1 == 'auction_house':
            em39 = discord.Embed(title='\'Auction house\' command use', description='Shows the auction stats of an item in hypixel skyblock\nUsage: `.auctionhouse|.ah <item_id>`', color=discord.Colour.random())
            em39.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em39)
        elif arg1 == 'lbin':
            em40 = discord.Embed(title='\'Lowest BIN\' command use', description='Shows the lowest price of an item in hypixel skyblock\nUsage: `.lbin <item_id>`', color=discord.Colour.random())
            em40.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em40)
        elif arg1 == 'say':
            em41 = discord.Embed(title='\'Say\' command use', description='Says stuff\nUsage: `.say <text>', color=discord.Colour.random())
            em41.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em41)
        elif arg1 == 'play':
            em42 = discord.Embed(title='\'Play\' command use', description='Plays a song in a voice channel\nUsage: `.play|.p <song_name/url>`\n**This command is under development**', color=discord.Colour.random())
            em42.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em42)
        elif arg1 == 'join':
            em43 = discord.Embed(title='\'Join\' command use', description='Joins a voice channel\nUsage `.join [#channel]`', color=discord.Colour.random())
            await ctx.reply(embed=em43)
        elif arg1 == 'leave':
            em44 = discord.Embed(title='\'Leave\' command use', description='Leaves the current connected voice channel\nUsage: `.leave`', color=discord.Colour.random())
            await ctx.reply(embed=em44)
        elif arg1 == 'stop':
            em45 = discord.Embed(title='\'Stop\' command use', description='Stops the current playing song\nUsage: `.stop`', color=discord.Colour.random())
            await ctx.reply(embed=em45)
        elif arg1 == 'pause':
            em46 = discord.Embed(title='\'Pause\' command use', description='Pauses the current playing song\nUsage: `.pause`', color=discord.Colour.random())
            await ctx.reply(embed=em46)
        elif arg1 == 'resume':
            em47 = discord.Embed(title='\'Resume\' command use', description='Resumes a paused song\nUsage: `.resume`', color=discord.Colour.random())
            await ctx.reply(embed=em47)
        elif arg1 == 'masterhacker':
            em48 = discord.Embed(title='\'Masterhacker\' command use', description='Sends a random image from r/masterhacker\nUsage: `.masterhacker`', color=discord.Colour.random())
            await ctx.reply(embed=em48)
        elif arg1 == 'passive':
            em49 = discord.Embed(title='\'Passive\' command use', description='Toggles passive mode. If it is turned on people\ncan\'t rob you but you can\'t rob people too\nCooldown: 1 hour\nUsage `.passive`', color=discord.Colour.random())
            await ctx.reply(embed=em49)
        elif arg1 == 'sweartoggle':
            em50 = discord.Embed(title='\'Sweartoggle\' command use', description='Toggles swear filter for a server. If enabled, when someone sends\na banned word, i will delete it and give the user a warn\nPermissions required: Administrator\nUsage: `.sweartoggle`', color=discord.Colour.random())
            await ctx.reply(embed=em50)
        elif arg1 == 'summon':
            em51 = discord.Embed(title='\'Summon\' command use', description='Joins in the channel where the message author is\nUsage: `.summon`', color=discord.Colour.random())
            await ctx.reply(embed=em51)
        elif arg1 == 'now':
            em52 = discord.Embed(title='\'Now\' command use', description='Shows the current playing song', color=discord.Colour.random())
            await ctx.reply(embed=em52)
        elif arg1 == 'queue':
            em53 = discord.Embed(title='\'Queue\' command use', description='Shows songs in queue', color=discord.Colour.random())
            await ctx.reply(embed=em53)
        elif arg1 == 'buy':
            em54 = discord.Embed(title='\'Buy\' command use', description='Buys an item from the shop (`.shop`)\nUsage: `.buy <item> [amount]`', color=discord.Colour.random())
            em54.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em54)
        elif arg1 == 'rank' or arg1 == 'xp':
            em55 = discord.Embed(title='\'Rank\' command use', description='Shows user activity with levels and xp\nUsage: `.rank|.xp [user]`', color=discord.Colour.random())
            em55.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em55)
        elif arg1 == 'credits':
            em56 == discord.Embed(title='\'Credits\' command use', description='Shows the arch bot developer team\nUsage: `.credits.`', color=discord.Colour.random())
            await ctx.reply(embed=em56)
        elif arg1 == 'invest':
            em57 = discord.Embed(title='\'Invest\' command use', description='Invests coins and claims them after 5 hours with a random amount of profit\nCooldown: random\nUsage: `.invest <claim/amount/all>`', color=discord.Colour.random())
            em57.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em57)
        elif arg1 == 'windowsmeme' or arg1 == 'windowshatememe' or arg1 == 'wm':
            em58 = discord.Embed(title='\'windowsmeme\' command use', description="Shows a windows hate meme cause windows bad\nUsage: `.windowsmeme|.wm`", color=discord.Colour.random())
            await ctx.reply(embed=em58)
        elif arg1 == 'use' or arg1 == 'open':
            em59 = discord.Embed(title='\'use\' command', description="Opens a box\nUsage: `.use|.open <item> [amount]`", color=discord.Colour.random())
            em59.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em59)
        elif arg1 == 'warn':
            em60 = discord.Embed(title="\'warn\' command use", description="Warns a user\nUsage: `.warn <user> <reason>`\nPermissions: manage messages", color=discord.Colour.random())
            em60.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em60)
        elif arg1 == 'giveaway':
            em61 = discord.Embed(title='\'giveaway\' command use', description="Starts a giveaway in a mentioned channel a mentioned amount of time\nRoles: `Giveaways`\nUsage: `.giveaway`", color=discord.Colour.random())
            await ctx.reply(embed=em61)
        elif arg1 == 'reroll':
            em62 = discord.Embed(title='\'reroll\' command use', description="Rerolls a giveaway, picks a different winner\nRoles: `Giveaways`\nUsage: `.reroll <#channel> <message_id>`\nExample: `.reroll #giveaways 919224004345208862")
            await ctx.reply(embed=em62)
        elif arg1 == 'poll':
            em63 = discord.Embed(title='\'poll\'command use', description="Starts a poll with 10 max options\nUsage: `.poll <\"question\"> <option1> <option2> [option3-10]")
            await ctx.reply(embed=em63)
        elif arg1 == "reddit":
            em65 = discord.Embed(title='\'reddit\' command use', description="Gets random image from a selected subreddit.\nUsage: `.reddit <subreddit>`")
            await ctx.reply(embed=em65)
        elif arg1 == 'help':
            await ctx.reply('You want help for help command?')
            def check(msg):
                return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

            msg = await self.client.wait_for("message", check=check)
            if msg.content == 'yes':
                await ctx.send('ok gimme a sec')
                async with ctx.typing():
                    await asyncio.sleep(2)
                h = discord.Embed(title='\'Help\' command use', description='helps\nusage: .help [command]', color=discord.Colour.random())
                h.set_footer(text='why the fk do u need help with this command')
                await ctx.send(embed=h)
            elif msg.content == 'no':
                await ctx.send("ok")
            else:
                pass
        else:
            await ctx.reply(f"No command \"{arg1}\" found")

    @commands.command(aliases=['warnings'])
    async def warns(self, ctx, *, user : discord.User=None):
        self.load()
        if user == None:
            if str(ctx.message.author.id) not in warnings:
                warnings[str(ctx.message.author.id)] = 0
            await ctx.reply(f"You have {warnings[str(ctx.message.author.id)]} warnings")
        else:
            if str(user.id) not in warnings:
                warnings[str(user.id)] = 0
            await ctx.reply(f"{user.display_name} has {warnings[str(user.id)]} warnings")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clearwarns(self, ctx, user : discord.User):
        warnings[str(user.id)] = 0
        self.save()
        await ctx.reply(f"Cleared all of **{user.display_name}**")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, user : discord.User, *, reason:str):
        guild = self.client.get_guild(ctx.guild.id)
        self.load()
        if str(user.id) not in warnings:
            warnings[str(user.id)] = 0
        await ctx.reply(f"**{user.display_name}** has been warned with reason: {reason}")
        warnings[str(user.id)] += 1
        self.save()
        dm = await user.create_dm()
        em = discord.Embed(title=f"You have been warned in {guild}", description=f"Reason: {reason}", color=discord.Colour.random())
        em.set_footer(text=f"You got warned by {ctx.message.author}")
        await dm.send(embed=em)
        return
    
    @commands.command()
    async def stroke(self, ctx, *, arg1):
        if arg1.isdigit:
            if int(arg1) > 750:
                return
            else:
                pass
            strok = ("").join(random.choices(string.ascii_lowercase + string.digits, k=int(arg1)))
            await ctx.send(strok)
        else:
            await ctx.reply(f"{arg1} isnt a number dood")

    bl8ball = True
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        colors = [
            0x000000,
            0xff0000,
            0x00ff00,
            0x0000ff,
            0x800080,
            0x00ffff,
            0xbfff00
    ]
        def rndcol():
            rnd = random.choice(colors)
            return hex(rnd)
        responses = [
                "no?????.",
                "when you grow a braincell, yes",
                "you stupid, of course not",
                "lol no",
                "As I see it, yes.",
                "Most likely.",
                "Yes.",
                "try again",
                "ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good."
        ]
        e = discord.Embed(title=f'{question}', description=f'{random.choice(responses)}', color=discord.Colour.random())
        await ctx.send(embed=e)

    blNuke = True
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        if channel == None: 
            await ctx.send("You did not mention a channel!")
            return

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            new_channel = await nuke_channel.clone(reason="Has been Nuked!")
            await nuke_channel.delete()
            await new_channel.send("This channel has been nuked!")
            await ctx.send("Nuked the Channel sucessfully!")
            if bool(log) == True:
                # with open('F:\\bot\\logs\\log.txt', 'a') as f:
                #     f.write(f'[{current_time}]{ctx.message.author.display_name}nuked{nuke_channel}\n')
                #     f.close()
                print(f'[{current_time}]{ctx.message.author.display_name} nuked {nuke_channel}')
            else:
                pass
        else:
            await ctx.send(f"No channel named {channel.name} was found!")

    blInvites = True
    @commands.command()
    async def invites(self, ctx, *, user : discord.User=None):
        colors = [
            0x000000,
            0xff0000,
            0x00ff00,
            0x0000ff,
            0x800080,
            0x00ffff,
            0xbfff00
    ]
        def rndcol():
            rnd = random.choice(colors)
            return hex(rnd)
        totalInvites = 0
        if user == None:
            for i in await ctx.guild.invites():
                if i.inviter == ctx.author:
                    totalInvites += i.uses
            e = discord.Embed(title=f'{ctx.message.author.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}", color=discord.Colour.random())
            await ctx.reply(embed=e)
        elif user.bot:
            await ctx.reply('This is a bot not a user')
            return
        else:
            for i in await ctx.guild.invites():
                if i.inviter == user:
                    totalInvites += i.uses
            e = discord.Embed(title=f'{user.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}", color=discord.Colour.random())
            await ctx.reply(embed=e)

    blPurge = True
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def purge(self, ctx, amount:int):
        colors = [
            0x000000,
            0xff0000,
            0x00ff00,
            0x0000ff,
            0x800080,
            0x00ffff,
            0xbfff00
    ]
        def rndcol():
            rnd = random.choice(colors)
            return hex(rnd)
        if int(amount) == 0:
            await ctx.reply("You can\'t purge 0 messages **dood**")
            return
        elif int(amount) < 0:
            await ctx.reply("You can\'t spawn messages")
            return
        elif int(amount) > 500:
            await ctx.reply("You can\'t purge more than 500 messages")
            return
        else:
            pass
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        embedSuccessPurge = discord.Embed(title='Purge Successful', description=f'Purged {amount} messages from this channel.', color=discord.Colour.random())
        await ctx.send(embed = embedSuccessPurge)

    blMeme = True
    @commands.command()
    async def meme(self, ctx):
        colors = [
            0x000000,
            0xff0000,
            0x00ff00,
            0x0000ff,
            0x800080,
            0x00ffff,
            0xbfff00
    ]
        def rndcol():
            rnd = random.choice(colors)
            return hex(rnd)
        async with ctx.typing():
            re = ['memes', 'meme', 'dankmemes']
            memes_submissions = reddit.subreddit(random.choice(re)).hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title, color=discord.Colour.random())
            embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

    @commands.command()
    @commands.is_nsfw()
    async def nudes(self, ctx):
        async with ctx.typing():
            memes_submissions = reddit.subreddit('Nude_Selfie').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title)
            embed.set_image(url=submission.url)
            embed.set_footer(text="guess who is horny")
        await ctx.send(embed = embed)

    blRstroke = True
    @commands.command()
    async def ihadastroke(self, ctx):
        colors = [
            0x000000,
            0xff0000,
            0x00ff00,
            0x0000ff,
            0x800080,
            0x00ffff,
            0xbfff00
    ]
        def rndcol():
            rnd = random.choice(colors)
            return hex(rnd)
        async with ctx.typing():
            memes_submissions = reddit.subreddit('ihadastroke').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title, color=discord.Colour.random())
            embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

    @commands.command(aliases=['mh'])
    async def masterhacker(self, ctx):
        colors = [
            0x000000,
            0xff0000,
            0x00ff00,
            0x0000ff,
            0x800080,
            0x00ffff,
            0xbfff00
    ]
        def rndcol():
            rnd = random.choice(colors)
            return hex(rnd)
        async with ctx.typing():
            memes_submissions = reddit.subreddit('masterhacker').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title, color=discord.Colour.random())
            embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def reddit(self, ctx, sub:str):
        block = [
            "nsfw",
            "nude",
            "nudes",
            "porn",
            "cum",
            "cock",
            "dick"
        ]
        if any(x in sub.lower() for x in block):
            if sub == "unixporn":
                pass
            else:
                await ctx.reply("no nsfw")
                return
        async with ctx.typing():
            try:
                memes_submissions = reddit.subreddit(sub).hot()
                post_to_pick = random.randint(1, 100)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)
                embed = discord.Embed(title = submission.title, color=discord.Colour.random())
                embed.set_image(url=submission.url)
                await ctx.send(embed = embed)
            except prawcore.exceptions.Redirect:
                await ctx.reply(f"No subreddit named {sub} found")
        
    @commands.command()
    async def shutdown(self, ctx):
        if ctx.message.author.id == 705462972415213588:
            def check(msg):
                return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)
            
            await ctx.send('You sure?')
            msg = await self.client.wait_for("message", check=check)
            if msg.content == 'y' or msg.content == 'yes':
                await ctx.send('Shutting down the bot...')
                time.sleep(0.5)
                raise SystemExit('Bot shutdown')
            elif msg.content == 'n' or msg.content == 'no':
                await ctx.send('ok')
            else:
                await ctx.send(f'What is {msg.content}? You are supposed to reply with yes or no')
        else:
            await ctx.send(f'101% that this command doesn\'t exist :eyes:')

    blHighlow = True
    @commands.command(aliases=['hl'])
    @commands.cooldown(1, 40, commands.BucketType.user)
    async def highlow(self, ctx):
        self.load()
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        numb = randint(1, 100)
        numb2 = randint(1, 100)
        id = str(ctx.message.author.id)
        coins = randint(300, 1000)

        def check(msg):
            return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

        await ctx.send(f'Your number is {numb} choose if the other is lower, higher or jackpot')
        msg = await self.client.wait_for("message", check=check)
        if msg.content == 'low':
            if numb > numb2:
                await ctx.send(f'Congrats, your number was {numb2} and you earned {coins} coins')
                wallet[str(ctx.message.author.id)] += coins
                self.save()
                return
                if bool(log) == True:
                    print(f'[{current_time}]{ctx.message.author.display_name} earned {coins} coins')
                else:
                    pass
            elif numb < numb2:
                await ctx.send(f'Incorrect the number was {numb2}')
            elif numb == numb2:
                await ctx.send(f'no')
        elif msg.content == 'jackpot':
            if numb == numb2:
                coins2 = randint(1000000, 5000000)
                await ctx.send(f'Congrats, your number was {numb2} and you earned {coins2} coins gg!')
                wallet[str(ctx.message.author.id)] += coins2
                self.save()
                return
                if bool(log) == True:
                    print(f'[{current_time}]{ctx.message.author.display_name} earned {coins2} coins')
                else:
                    pass
            else:
                await ctx.send(f'Incorrect the number was {numb2}')
                return
        elif msg.content == 'high':
            if numb < numb2:
                await ctx.send(f'Congrats, your number was {numb2} and you earned {coins} coins')
                wallet[str(ctx.message.author.id)] += coins
                self.save()
                return
                if bool(log) == True:
                    print(f'[{current_time}]{ctx.message.author.display_name} earned {coins} coins')
                else:
                    pass
            else:
                await ctx.send(f'Incorrect your number was {numb2}')
                return
        else:
            await ctx.send(f'{msg.content} is not an option')

    blKill = True
    @commands.command()
    async def kill(self, ctx, user : discord.User=None):
        if user == None:
            await ctx.send('Please tag someone to kill')
        elif user.id == ctx.message.author.id:
            await ctx.send('Ok you are dead, please tag someone else to kill')
        else:
            responses2 = [
                f"**{user.display_name}** died from a dang baguette",
                f"<@{ctx.message.author.id}> strikes **{user.display_name}** with the killing curse... *Avada Kedavra!*",
                f"**{user.display_name} dies from dabbing too hard",
                f"**{user.display_name}** ripped their own heart out to show their love for <@{ctx.message.author.id}>"
            ]
            await ctx.send(f'{random.choice(responses2)}')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, *, member : discord.Member):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if member == ctx.message.author:
            raise BadArgument
        else:
            await member.kick()
        await ctx.send(f'{member} has been kicked from the server')
        if bool(log) == True:
            print(f'[{current_time}]{ctx.message.author.display_name} kicked {member.display_name} from {ctx.message.guild.name}')
        else:
            pass

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, *, member : discord.Member):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if member == ctx.message.author:
            raise BadArgument
        else:
            await member.ban()
            await ctx.send(f'{member} has been banned from the server')
            if bool(log) == True:
                print(f'[{current_time}]{ctx.message.author.display_name} banned {member.display_name} from {ctx.message.guild.name}')
            else:
                pass 

    @commands.command()
    async def slap(self, ctx, user : discord.User):
        responses3 = [
            "https://cdn.weeb.sh/images/Hkw1VkYP-.gif",
            "https://cdn.weeb.sh/images/SJlkNkFwb.gif",
            "https://cdn.weeb.sh/images/rJ4141YDZ.gif",
            "https://cdn.weeb.sh/images/HJKiX1tPW.gif"
        ]
        e = discord.Embed(title=f'{ctx.message.author} slaps {user}', color=discord.Colour.random())
        e.set_image(url=f'{random.choice(responses3)}')
        await ctx.send(embed = e)

    @commands.command(aliases=['sg'])
    async def softwaregore(self, ctx):
        colors = [
            0x000000,
            0xff0000,
            0x00ff00,
            0x0000ff,
            0x800080,
            0x00ffff,
            0xbfff00
    ]
        def rndcol():
            rnd = random.choice(colors)
            return hex(rnd)
        async with ctx.typing():
            sg_submissions = reddit.subreddit('softwaregore').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in sg_submissions if not x.stickied)
        embed = discord.Embed(title = submission.title, color=discord.Colour.random())
        embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def guess(self, ctx, num:int):
        self.load()
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        x = randint(1, 10)
        if num == x:
            coins = randint(100, 1000)
            await ctx.reply(f'Correct! You got {coins} coins')
            wallet[str(ctx.message.author.id)] += coins
            self.save()
        else:
            await ctx.reply(f'Nope it was {x}')

    @commands.command(aliases=['sus'])
    async def isSus(self, ctx, *, user : discord.User):
        susvar = [
            True,
            False
        ]
        sus = random.choice(susvar)
        if bool(sus) == True:
            await ctx.send(f'{user.mention} is very sus')
        elif bool(sus) == False:
            await ctx.send(f'{user.mention} isn\'t sus')
        else:
            await ctx.reply('undefined')

    @commands.command(aliases=['pm'])
    @commands.cooldown(1, 40, commands.BucketType.user)
    async def postmeme(self, ctx):
        self.load()
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await ctx.send(f'{ctx.message.author.mention} What type of meme you want to post?\n`f` Fresh meme\n`d` Dank meme\n`c` Copypasta\n*more comming soon*')

        def check(msg):
            return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content) in ['f', 'd', 'c']
        
        msg = await self.client.wait_for("message", check=check)

        x = randint(0, 200)
        if x == 0:
            await ctx.send(f'{ctx.message.author.mention} You earned 0 coins xD')
        else:
            await ctx.send(f'You earned {x} coins')
            wallet[str(ctx.message.author.id)] += x
            self.save()
            if bool(log) == True:
                print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} has earned {colors.green}{x}{colors.end} coins')
            else:
                pass

    @commands.command()
    async def null(self, ctx):
        await ctx.reply('You got **null** coins dood.')

    @commands.command(aliases=['gift'])
    async def give(self, ctx, user : discord.User, amount:int, item:str=None):
        self.load()
        if user.id == ctx.message.author.id:
            await ctx.reply('You can\'t gift yourself')
            return
        if passiveUsers[str(ctx.message.author.id)] == 1:
            await ctx.reply("You have passive mode enabled, you can\'t gigt to other users", mention_author=False)
            return
        if passiveUsers[str(user.id)] == 1:
            await ctx.reply("This user has passive mode enabled. Leave them alone!", mention_author=False)
            return
        else:
            if item == None:
                if wallet[str(ctx.message.author.id)] < int(amount):
                    await ctx.reply('You don\'t have that many coins in your wallet')
                    return
                elif int(amount) < 0 or int(amount) == 0:
                    await ctx.reply('Don\'t try to break me **dood**')
                    return
                else:
                    wallet[str(ctx.message.author.id)] -= int(amount)
                    self.save()
                    wallet[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f'You gave {amount} coins to {user.display_name}')
            elif item == "windows10":
                if windows10[str(ctx.message.author.id)] < int(amount):
                    await ctx.reply("You don\'t have that many items")
                    return
                elif int(amount) < 0 or int(amount) == 0:
                    await ctx.reply("Don\'t try to break me **dood**")
                    return
                else:
                    if str(user.id) not in windows10:
                        windows10[str(user.id)] = 0
                    windows10[str(ctx.message.author.id)] -= int(amount)
                    self.save()
                    windows10[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"You gave {amount} windows 10 keys to {user.display_name}")
                    return
            elif item == "bronzecoin":
                if bronzecoin[str(ctx.message.author.id)] < int(amount):
                    await ctx.reply("You don\'t have that many items")
                    return
                elif int(amount) < 0 or int(amount) == 0:
                    await ctx.reply("Don\'t try to break me **dood**")
                    return
                else:
                    if str(user.id) not in bronzecoin:
                        bronzecoin[str(user.id)] = 0
                    bronzecoin[str(ctx.message.author.id)] -= int(amount)
                    self.save()
                    bronzecoin[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"You gave {amount} bronze coins to {user.display_name}")
                    return
            elif item == "silvercoin":
                if silvercoin[str(ctx.message.author.id)] < int(amount):
                    await ctx.reply("You don\'t have that many items")
                    return
                elif int(amount) < 0 or int(amount) == 0:
                    await ctx.reply("Don\'t try to break me **dood**")
                    return
                else:
                    if str(user.id) not in silvercoin:
                        silvercoin[str(user.id)] = 0
                    silvercoin[str(ctx.message.author.id)] -= int(amount)
                    self.save()
                    silvercoin[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"You gave {amount} silver coins keys to {user.display_name}")
                    return
            elif item == "goldcoin":
                if goldcoin[str(ctx.message.author.id)] < int(amount):
                    await ctx.reply("You don\'t have that many items")
                    return
                elif int(amount) < 0 or int(amount) == 0:
                    await ctx.reply("Don\'t try to break me **dood**")
                    return
                else:
                    if str(user.id) not in goldcoin:
                        goldcoin[str(user.id)] = 0
                    goldcoin[str(ctx.message.author.id)] -= int(amount)
                    self.save()
                    goldcoin[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"You gave {amount} gold coins keys to {user.display_name}")
                    return
            else:
                await ctx.reply("No such item")
                return
            
    @commands.command()
    async def add(self, ctx, user:discord.User, amount:int, place:str=None):
        self.load()
        if ctx.message.author.id not in ids:
            return
        else:
            if user == None:
                if place == None or str(place) == "wallet":
                    if str(user.id) not in wallet:
                        wallet[str(ctx.message.author.id)] = 0
                        self.save()
                    wallet[str(ctx.message.author.id)] += int(amount)
                    await ctx.reply(f"Added {amount} coins to your wallet")
                    self.save()
                    return
                elif place == "bank":
                    if str(user.id) not in bank:
                        bank[str(ctx.message.author.id)] = 0
                        self.save()
                    bank[str(ctx.message.author.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} coins to your bank")
                    return
                else:
                    raise BadArgument
            else:
                if place == None or str(place) == "wallet":
                    if str(user.id) not in wallet:
                        wallet[str(user.id)] = 0
                        self.save()
                    wallet[str(user.id)] += int(amount)
                    await ctx.reply(f"Added {amount} coins to {user.display_name}")
                    self.save()
                    return
                elif place == "bank":
                    if str(user.id) not in bank:
                        bank[str(user.id)] = 0
                        self.save()
                    bank[str(user.id)] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} coins in {user.display_name}\'s bank")
                    return
                else:
                    raise BadArgument
     
    @commands.command(name="invest")
    async def _invest(self, ctx, action:str):
        self.load()
        if str(ctx.message.author.id) not in invest:
            invest[str(ctx.message.author.id)] = 0
            self.save()
        if str(action) == "claim":
            if str(ctx.message.author.id) not in invest or invest[str(ctx.message.author.id)] == 0:
                await ctx.reply("You didnt invest any coins. Type `.invest <amount>` to invest some coins")
                return
            if ctx.message.author.id not in no_invest_cooldown:
                i = datetime.datetime.now() - cd[str(ctx.message.author.id)]
                if i is None or i.seconds > invest_time:
                    cd[str(ctx.message.author.id)] = datetime.datetime.now()
                    pass
                else:
                    await ctx.reply("You cant claim your money yet")
                    return
            else:
                pass
            rnd = ''.join(map(str, random.choices([1.25, 1.5, 1.75, 2, 2.5, 5], weights=[35, 10, 5, 3, 1, 0.5], k=1)))
            a = round(invest[str(ctx.message.author.id)] * float(rnd))
            wallet[str(ctx.message.author.id)] += a
            invest[str(ctx.message.author.id)] = 0
            self.save()
            await ctx.reply(f"You claimed {a} coins with {rnd} profit")
            return
        elif str(action) == "all" or str(action) == "max":
            if wallet[str(ctx.message.author.id)] < 10000:
                await ctx.reply("You can\'t invest less than 10000 coins")
                return
            else:
                m = round(sys.maxsize / 5)
                maxv = m - 1
                # if wallet[str(ctx.message.author.id)] > maxv:
                #     await ctx.reply("Warning: will invest 1844674407370955263, which is the max value for this command", mention_author=False)
                # else:
                #     pass
                def check(msg):
                    return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

                await ctx.reply(f"Are you sure you want to invest {wallet[str(ctx.message.author.id)]} coins? If you invest them you wont have them in your wallet for some time\nYou can claim after the coins after some time using `.invest claim`\nType yes or no")
                msg = await self.client.wait_for("message", check=check)
                if msg.content == "no":
                    await ctx.send("Ok guess you are not gonna invest today")
                    return
                elif msg.content == "yes":
                    if ctx.message.author.id not in no_invest_cooldown:
                        try:
                            i = datetime.datetime.now() - cd[str(ctx.message.author.id)]
                        except KeyError:
                            i = None
                            cd[str(ctx.message.author.id)] = datetime.datetime.now()
                        if i is None or i.seconds > invest_time:
                            cd[str(ctx.message.author.id)] = datetime.datetime.now()
                            pass
                        else:
                            await ctx.reply("You already have invested coins")
                            return
                    else:
                        pass
                    if invest[str(ctx.message.author.id)] == 0:
                        pass
                    else:
                        await ctx.send("There are unclaimed coins. Type `.invest claim` to claim them")
                        return
                    invest[str(ctx.message.author.id)] += wallet[str(ctx.message.author.id)]
                    if ctx.message.author.id not in no_invest_cooldown:
                        await ctx.send(f"You invested {action} coins. Come back in {round(invest_time / 3600)} hours to claim your coins")
                    else:
                        await ctx.send(f"You invested {wallet[str(ctx.message.author.id)]} coins. You have no cooldown so you can claim your coins now")
                        return
                    wallet[str(ctx.message.author.id)] -= wallet[str(ctx.message.author.id)]
                    self.save()
                    return
                else:
                    await ctx.send(f"You are supposed to type yes or no. Not {msg.content}")
                    return
        else:
            if action.isdigit:
                try:
                    int(action)
                except ValueError:
                    raise BadArgument
                if int(action) < 10000:
                    await ctx.reply("You can\'t invest less than 10000 coins")
                    return
                else:
                    if int(action) > wallet[str(ctx.message.author.id)]:
                        await ctx.reply("You dont have that many coins in your wallet")
                        return
                    else:
                        m = round(sys.maxsize / 5)
                        maxv = m - 1
                        def check(msg):
                            return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

                        await ctx.reply(f"Are you sure you want to invest {action} coins? If you invest them you wont have them in your wallet for some time\nYou can claim after the coins after some time using `.invest claim`\nType yes or no")
                        msg = await self.client.wait_for("message", check=check)
                        if msg.content == "no":
                            await ctx.send("Ok guess you are not gonna invest today")
                            return
                        elif msg.content == "yes":
                            if ctx.message.author.id not in no_invest_cooldown:
                                try:
                                    i = datetime.datetime.now() - cd[str(ctx.message.author.id)]
                                except KeyError:
                                    i = None
                                    cd[str(ctx.message.author.id)] = datetime.datetime.now()
                                if i is None or i.seconds > invest_time:
                                    cd[str(ctx.message.author.id)] = datetime.datetime.now()
                                    pass
                                else:
                                    await ctx.reply("You already have invested coins")
                                    return
                            else:
                                pass
                            if invest[str(ctx.message.author.id)] == 0:
                                pass
                            else:
                                await ctx.send("There are unclaimed coins. Type `.invest claim` to claim them")
                                return
                            invest[str(ctx.message.author.id)] += int(action)
                            wallet[str(ctx.message.author.id)] -= int(action)
                            self.save()
                            if ctx.message.author.id not in no_invest_cooldown:
                                await ctx.send(f"You invested {action} coins. Come back in {round(invest_time / 3600)} hours to claim your coins")
                            else:
                                await ctx.send(f"You invested {action} coins. You have no cooldown so you can claim your coins now")
                            return
                        else:
                            await ctx.send(f"You are supposed to type yes or no. Not {msg.content}")
                            return                        
            else:
                raise BadArgument
            
    @commands.command(aliases=["job"])
    async def work(self, ctx, *, arg1=None):
        self.load()
        if arg1 == None:
            if str(ctx.message.author.id) not in jobs:
                await ctx.reply("You dont have a job yet. Type `.work list` to see the list of jobs")
                return
            else:
                try:
                    last_work = datetime.datetime.now() - on_cooldown[str(ctx.message.author.id)]
                except KeyError:
                    last_work = None
                    on_cooldown[str(ctx.message.author.id)] = datetime.datetime.now()
                j = jobs[str(ctx.message.author.id)]
                if last_work is None or last_work.seconds > work_cooldown:
                      on_cooldown[str(ctx.message.author.id)] = datetime.datetime.now()
                      pass
                else:
                    await ctx.reply("This command is on cooldown")
                    return
                if j == "mod":
                    await ctx.reply("You earned 5000 coins from Discord Moderator job")
                    wallet[str(ctx.message.author.id)] += 5000
                    self.save()
                    return
                elif j == "yt":
                    await ctx.reply("You earned 6000 coins from YouTuber job")
                    wallet[str(ctx.message.author.id)] += 6000
                    self.save()
                    return
                elif j == "ts":
                    await ctx.reply("You earned 6900 coins from Twitch Streamer job")
                    wallet[str(ctx.message.author.id)] += 6900
                    self.save()
                    return
                elif j == "pg":
                    await ctx.reply("You earned 15000 coins from Pro Gamer job")
                    wallet[str(ctx.message.author.id)] += 15000
                    self.save()
                    return
                elif j == "dc":
                    await ctx.reply("You earned 20000 coins from Doctor job")
                    wallet[str(ctx.message.author.id)] += 20000
                    self.save()
                    return
                elif j == "dev":
                    await ctx.reply("You earned 25000 coins from Developer job")
                    wallet[str(ctx.message.author.id)] += 25000
                    self.save()
                    return
                elif j == "sc":
                    await ctx.reply("You earned 75000 coins from Scientist job")
                    wallet[str(ctx.message.author.id)] += 75000
                    self.save()
                    return
                elif j == "ab":
                    await ctx.reply("You earned 169420 coins and a **developer box** from Arch bot developer job")
                    wallet[str(ctx.message.author.id)] += 169420
                    devbox[str(ctx.message.author.id)] += 1
                    self.save()
                    return
        elif str(arg1) == "list":
            color = discord.Colour.random()
            page1 = discord.Embed(
                title="Jobs list",
                description="**Discord Mod**\nRequirement: `level 1`\nSalary: `5000 coins`\nId: `mod`\n\n**YouTuber**\nRequirememt: `level 5`\nSalary: `6000 coins`\nId: `yt`\n\n**Twitch streamer**\nRequirement: `level 5`\nSalary: `6900 coins`\nId: `ts`",
                color=color
            )
            page2 = discord.Embed(
                title="Jobs list",
                description="**Pro Gamer**\nRequirement: `level 10`\nSalary: `15000 coins`\nId: `pg`\n\n**Doctor**\nRequirement: `level 15`\nSalary: `20000 coins`\nId: `dc`\n\n**Developer**\nRequirement: `level 20`\nSalary: `25000 coins`\nId: `dev`",
                color=color
            )
            page3 = discord.Embed(
                title="Jobs list",
                description="**Scientist**\nRequirement: `level 50`\nSalary: `75000 coins`\nId: `sc`\n\n**Arch Bot Developer**\nRequirement: `level 69`\nSalary: `169420 coins`\nId: `ab`",
                color=color
            )
            page1.set_footer(text="Tip: type .work <job_id> to start a job")
            page2.set_footer(text="Tip: type .work <job_id> to start a job")
            page3.set_footer(text="Tip: type .work <job_id> to start a job")
            pages = [
                page1,
                page2, 
                page3
            ]
            message = await ctx.send(embed = page1)
            await message.add_reaction('◀')
            await message.add_reaction('▶')
            def check(reaction, user):
                return user == ctx.author
            i = 0
            reaction = None
            while True:
                if str(reaction) == '◀':
                    if i > 0:
                        i -= 1
                        await message.edit(embed = pages[i])
                elif str(reaction) == '▶':
                    if i < 2:
                        i += 1
                        await message.edit(embed = pages[i])
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout = 30.0, check = check)
                    await message.remove_reaction(reaction, user)
                except Exception as e:
                    print(e)
                    break
            await message.clear_reactions()
            return
        elif str(arg1) == "resign":
            if str(ctx.message.author.id) not in jobs:
                await ctx.reply("You dont have a job")
                return
            else:
                del jobs[str(ctx.message.author.id)]
                await ctx.reply("You resigned from your job.")
                self.save()
                return
        elif str(arg1) == "mod":
            if str(ctx.message.author.id) not in jobs:
                jobs[str(ctx.message.author.id)] = "mod"
                await ctx.reply("You are working as a **Discord Moderator** now!")
                self.save()
                return
            else:
                await ctx.reply("You already have a job. Type `.work resign` to quit your job.")
                return
        elif str(arg1) == "yt":
            if str(ctx.message.author.id) not in jobs:
                if levels[str(ctx.message.author.id)] >= 5:
                    jobs[str(ctx.message.author.id)] = "yt"
                    self.save()
                    await ctx.reply("You are now working as a **YouTuber**")
                    return
                else:
                    await ctx.reply("Your level is not high enough to work as a **YouTuber**")
                    return
            else:
                await ctx.reply("You already have a job. Type `.work resign` to quit your job.")
                return
        elif str(arg1) == "ts":
            if str(ctx.message.author.id) not in jobs:
                if levels[str(ctx.message.author.id)] >= 5:
                    jobs[str(ctx.message.author.id)] = "ts"
                    self.save()
                    await ctx.reply("You are now working as a **Twitch Streamer**")
                    return
                else:
                    await ctx.reply("Your level is not high enough to work as a **Twitch Streamer**")
                    return
            else:
                await ctx.reply("You already have a job. Type `.work resign` to quit your job.")
                return
        elif str(arg1) == "pg":
            if str(ctx.message.author.id) not in jobs:
                if levels[str(ctx.message.author.id)] >= 10:
                    jobs[str(ctx.message.author.id)] = "pg"
                    self.save()
                    await ctx.reply("You are now working as a **Pro Gamer**")
                    return
                else:
                    await ctx.reply("Your level is not high enough to work as a **Pro Gamer**")
                    return
            else:
                await ctx.reply("You already have a job. Type `.work resign` to quit your job.")
                return
        elif str(arg1) == "dc":
            if str(ctx.message.author.id) not in jobs:
                if levels[str(ctx.message.author.id)] >= 15:
                    jobs[str(ctx.message.author.id)] = "dc"
                    self.save()
                    await ctx.reply("You are now working as a **Doctor**")
                    return
                else:
                    await ctx.reply("Your level is not high enough to work as a **Doctor**")
                    return
            else:
                await ctx.reply("You already have a job. Type `.work resign` to quit your job.")
                return
        elif str(arg1) == "dev":
            if str(ctx.message.author.id) not in jobs:
                if levels[str(ctx.message.author.id)] >= 20:
                    jobs[str(ctx.message.author.id)] = "dev"
                    self.save()
                    await ctx.reply("You are now working as a **Developer**")
                    return
                else:
                    await ctx.reply("Your level is not high enough to work as a **Developer**")
                    return
            else:
                await ctx.reply("You already have a job. Type `.work resign` to quit your job.")
                return
        elif str(arg1) == "sc":
            if str(ctx.message.author.id) not in jobs:
                if levels[str(ctx.message.author.id)] >= 50:
                    jobs[str(ctx.message.author.id)] = "sc"
                    self.save()
                    await ctx.reply("You are now working as a **Scientist**")
                    return
                else:
                    await ctx.reply("Your level is not high enough to work as a **Scientist**")
                    return
            else:
                await ctx.reply("You already have a job. Type `.work resign` to quit your job.")
                return
        elif str(arg1) == "ab":
            if str(ctx.message.author.id) not in jobs:
                if levels[str(ctx.message.author.id)] >= 69:
                    jobs[str(ctx.message.author.id)] = "ab"
                    self.save()
                    await ctx.reply("You are now working as a **Arch bot developer**")
                    return
                else:
                    await ctx.reply("Your level is not high enough to work as a **Arch bot developer**")
                    return
            else:
                await ctx.reply("You already have a job. Type `.work resign` to quit your job.")
                return
        else:
            await ctx.reply(f"Invalid command/job id")
            return

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def beg(self, ctx):
        self.load()
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        coins = randint(1, 500)
        wallet[str(ctx.message.author.id)] += coins
        await ctx.send(f'You earned {coins} coins.')
        self.save()

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        self.load()
        if bool(currency) == False:
            await ctx.reply('Currency is disabled')
            return
        else:
            pass
        wallet[str(ctx.message.author.id)] += 10000
        dailybox[str(ctx.message.author.id)] += 1
        await ctx.send('You claimed 10,000 coins and a daily box!')
        self.save()

    @commands.command(aliases=['dep'])
    async def deposit(self, ctx, *, arg1):
        self.load()
        if bool(currency) == False:
            await ctx.send('Currency is disabled')
            return
        else:
            if arg1 == 'all' or arg1 == 'max':
                if wallet[str(ctx.message.author.id)] == 0:
                    await ctx.send('You don\'t have any coins in your wallet')
                    return
                else:
                    if wallet[str(ctx.message.author.id)] == 1:
                        await ctx.reply(f'You deposited 1 coin')
                    else:
                        await ctx.reply(f'You deposited {wallet[str(ctx.message.author.id)]} coins')
                    bank[str(ctx.message.author.id)] += int(wallet[str(ctx.message.author.id)])
                    wallet[str(ctx.message.author.id)] -= int(wallet[str(ctx.message.author.id)])
                    self.save()
                    return
            elif arg1.isdigit:
                if int(arg1) > wallet[str(ctx.message.author.id)]:
                    await ctx.reply('You don\'t have that many coins in your wallet')
                    return
                elif int(arg1) < 0:
                    await ctx.reply('Don\'t try to break me dood')
                    return
                else:
                    await ctx.send(f'You deposited {arg1} coins')
                    wallet[str(ctx.message.author.id)] -= int(arg1)
                    bank[str(ctx.message.author.id)] += int(arg1)
                    self.save()
                    return
            else:
                raise BadArgument

    @commands.command(aliases=['with'])
    async def withdraw(self, ctx, *, arg1):
        self.load()
        if bool(currency) == False:
            await ctx.send('Currency is disabled')
            return
        else:
            if arg1 == 'all' or arg1 == 'max':
                if bank[str(ctx.message.author.id)] == 0:
                    await ctx.send('You don\'t have any coins in your bank')
                    return
                else:
                    if bank[str(ctx.message.author.id)] == 1:
                        await ctx.reply(f'You withdrawn {bank[str(ctx.message.author.id)]} coin')
                    else:
                        await ctx.reply(f'You withdrawn {bank[str(ctx.message.author.id)]} coins')
                    wallet[str(ctx.message.author.id)] += int(bank[str(ctx.message.author.id)])
                    bank[str(ctx.message.author.id)] -= int(bank[str(ctx.message.author.id)])
                    self.save()
                    return
            elif arg1.isdigit:
                if int(arg1) > bank[str(ctx.message.author.id)]:
                    await ctx.reply('You don\'t have that many coins in your bank')
                    return
                elif int(arg1) < 0:
                    await ctx.reply('Don\'t try to break me dood')
                    return
                else:
                    await ctx.send(f'You withdrawn {arg1} coins')
                    wallet[str(ctx.message.author.id)] += int(arg1)
                    bank[str(ctx.message.author.id)] -= int(arg1)
                    self.save()
                    return
            else:
                raise BadArgument

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def rob(self, ctx, *, user : discord.User):
        self.load()
        if bool(currency) == False:
            await ctx.send('Currency is disabled')
            return
        else:
            pass
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if ctx.message.author.id == user.id:
            await ctx.send('you cant rob yourself xd')
            return
        else:
            if str(user.id) not in wallet:
                wallet[str(user.id)] = 0
            if str(user.id) not in passiveUsers:
                passiveUsers[str(user.id)] = 0
            if passiveUsers[str(ctx.message.author.id)] == 1:
                await ctx.reply(f"You are on passive mode. You can\'t rob other people")
                return
            if passiveUsers[str(user.id)] == 1:
                await ctx.reply(f"{user.display_name} has passive mode turned on. You can\'t rob them")
                return
            if wallet[str(user.id)] < 500:
                await ctx.send('This user has less than 500 coins')
            elif wallet[str(user.id)] >= 500:
                coins = randint(500, wallet[str(user.id)])
                if bool(log) == True:
                    print(f'[{current_time}]{ctx.message.author.display_name} stole {coins} coins from {user.display_name}')
                else:
                    pass
                wallet[str(user.id)] -= coins
                self.save()
                wallet[str(ctx.message.author.id)] += coins
                self.save()
                await ctx.send(f'You stole {coins} coins from **{user.display_name}**')

    @commands.command()
    @commands.cooldown(1, 604800, commands.BucketType.user)
    async def weekly(self, ctx):
        self.load()
        if bool(currency) == False:
            await ctx.send('Currency is disabled')
            return
        else:
            pass
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        wallet[str(ctx.message.author.id)] += 50000
        await ctx.reply('You claimed 50,000 coins')
        self.save()
        if bool(log) == True:
            print(f'[{current_time}]{ctx.message.author.display_name} claimed 50k coins from weekly command')
        else:
            pass

    @commands.command()
    @commands.cooldown(1, 2592000, commands.BucketType.user)
    async def monthly(self, ctx):
        self.load()
        if bool(currency) == False:
            await ctx.send('Currency is disabled')
            return
        else:
            pass
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        wallet[str(ctx.message.author.id)] += 100000
        await ctx.send('You claimed 100,000 coins')
        self.save()
        if bool(log) == True:
            print(f'[{current_time}]{ctx.message.author.display_name} claimed 100k coins from monthly command')
        else:
            pass

    @commands.command(aliases=['bal'])
    async def balance(self, ctx, user : discord.User=None):
        self.load()
        colors = [
            0x000000,
            0xff0000,
            0x00ff00,
            0x0000ff,
            0x800080,
            0x00ffff,
            0xbfff00
    ]
        def rndcol():
            rnd = random.choice(colors)
            return hex(rnd)
        if bool(currency) == False:
            await ctx.send('Currency is disabled')
            return
        else:
            pass
        if user == None:
            if str(ctx.message.author.id) not in wallet:
                wallet[str(ctx.message.author.id)] = 0
            if str(ctx.message.author.id) not in bank:
                bank[str(ctx.message.author.id)] = 0
            if str(ctx.message.author.id) not in windows10:
                windows10[str(ctx.message.author.id)] = 0
            if str(ctx.message.author.id) not in bronzecoin:
                bronzecoin[str(ctx.message.author.id)] = 0
            if str(ctx.message.author.id) not in silvercoin:
                silvercoin[str(ctx.message.author.id)] = 0
            if str(ctx.message.author.id) not in goldcoin:
                goldcoin[str(ctx.message.author.id)] = 0
            self.save()
            win10v = windows10[str(ctx.message.author.id)] * 69420
            bcoinv = bronzecoin[str(ctx.message.author.id)] * 50000
            scoinv = silvercoin[str(ctx.message.author.id)] * 250000
            gcoinv = goldcoin[str(ctx.message.author.id)] * 1000000
            dboxv = devbox[str(ctx.message.author.id)] * 69000000000000
            dailyboxv = dailybox[str(ctx.message.author.id)] * 10000
            networth = wallet[str(ctx.message.author.id)] + bank[str(ctx.message.author.id)] + win10v + bcoinv + scoinv + gcoinv + dboxv + dailyboxv
            embed = discord.Embed(title=f"{ctx.message.author.display_name}'s Balance", color=discord.Colour.random())
            embed.add_field(name="Wallet", value=str(wallet[str(ctx.message.author.id)]))
            embed.add_field(name="Bank", value=str(bank[str(ctx.message.author.id)]))
            embed.add_field(name="Networth", value=str(networth))
            embed.add_field(name="Invested coins", value=str(invest[str(ctx.message.author.id)]))
            embed.set_footer(text=f'Currency api made by {owner}')
            await ctx.send(embed=embed)
        else:
            if str(user.id) not in wallet:
                wallet[str(user.id)] = 0
            if str(user.id) not in bank:
                bank[str(user.id)] = 0
            if str(user.id) not in windows10:
                windows10[str(user.id)] = 0
            if str(user.id) not in bronzecoin:
                bronzecoin[str(user.id)] = 0
            if str(user.id) not in silvercoin:
                silvercoin[str(user.id)] = 0
            if str(user.id) not in goldcoin:
                goldcoin[str(user.id)] = 0
            self.save()
            win10v = windows10[str(user.id)] * 69420
            bcoinv = bronzecoin[str(user.id)] * 50000
            scoinv = silvercoin[str(user.id)] * 250000
            gcoinv = goldcoin[str(user.id)] * 1000000
            networth = wallet[str(user.id)] + bank[str(user.id)] + win10v + bcoinv + scoinv + gcoinv
            embed = discord.Embed(title=f"{user.display_name}'s Balance", color=discord.Colour.random())
            embed.add_field(name="Wallet", value=str(wallet[str(user.id)]))
            embed.add_field(name="Bank", value=str(bank[str(user.id)]))
            embed.add_field(name="Networth", value=str(networth))
            embed.set_footer(text=f'Currency api made by {owner}')
            await ctx.send(embed=embed)

    @commands.command(aliases=["lm"])
    async def linuxmeme(self, ctx):
        colors = [
            0x000000,
            0xff0000,
            0x00ff00,
            0x0000ff,
            0x800080,
            0x00ffff,
            0xbfff00
    ]
        def rndcol():
            rnd = random.choice(colors)
            return hex(rnd)
        async with ctx.typing():
            memes_submissions = reddit.subreddit('linuxmemes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title, color=discord.Colour.random())
            embed.set_image(url=submission.url)
        await ctx.send(embed = embed)
        
    @commands.command(aliases=["wm"])
    async def windowsmeme(self, ctx):
        colors = [
            0x000000,
            0xff0000,
            0x00ff00,
            0x0000ff,
            0x800080,
            0x00ffff,
            0xbfff00
    ]
        def rndcol():
            rnd = random.choice(colors)
            return hex(rnd)
        async with ctx.typing():
            re = ['windowshatememes', 'antiwindowsmemes']
            memes_submissions = reddit.subreddit(random.choice(re)).hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title, color=discord.Colour.random())
            embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

    key = '7afe43ee-bfb5-494e-9506-b92a914e39f8'
    @commands.command(aliases=["nw"])
    async def networth(self, ctx, *, arg1, arg2=None):
        if arg2 == None:
            url = f'https://nariah-dev.com/api/networth/total/{arg1}/?key={key}'
            r = requests.get(url)
            if r.status_code == 200:
                r.raise_for_status()
                jsonr = r.json()
                total = jsonr["total"]
                e = discord.Embed(title=f'{arg1}\'s Hypixel Skyblock networth', description=f'{total} coins')
                await ctx.send(embed=e)
            elif r.status_code == 500:
                await ctx.reply('An internal error occured')
            elif r.status_code == 404:
                jsonr = r.json()
                cause = jsonr["cause"]
                await ctx.reply(f'Error\nStatus code: {r.status_code}\nCause: {cause}')
            else:
                await ctx.reply(f'Undefined status code: {r.status_code}\ndm this to {owner}')
        else:
            url = f'https://nariah-dev.com/api/networth/total/{arg1}/{arg2}?key={key}'
            r = requests.get(url)
            if r.status_code == 200:
                r.raise_for_status()
                jsonr = r.json()
                total = jsonr["total"]
                e = discord.Embed(title=f'{arg1}\'s Hypixel Skyblock networth', description=f'{total} coins')
                e.set_footer(text=f'Profile: {arg2}')
                await ctx.send(embed=e)
            elif r.status_code == 500:
                await ctx.reply('An internal error occured')
            elif r.status_code == 404:
                await ctx.reply('Invalid username or profile')
            else:
                await ctx.reply(f'Undefined status code: {r.status_code}\ndm this to {owner}')

    @commands.command(aliases=['ah'])
    async def auctionhouse(self, ctx, *, arg1):
        url = f'https://nariah-dev.com/api/auctions/statistics/{arg1}'
        r = requests.get(url)
        if r.status_code == 200:
            r.raise_for_status()
            jsonr = r.json()
            data = jsonr["data"]
            # data of jsonr["data"]
            average = data["average"] #average price of an item
            minimum = data["min"] #minimum price of an item
            maximum = data["max"] #maximum price of an item
            item = arg1.replace("_", " ")
            e = discord.Embed(title=f'Auction house stats for {item}', description=f'Average price: {average}\nLowest price: {minimum}\nHighest price: {maximum}')
            await ctx.send(embed=e)
        elif r.status_code == 404:
            await ctx.reply(f'No such item ({arg1})')
        elif r.status_code == 500:
            await ctx.reply('An internal error occured')
        else:
            await ctx.reply(f'Undefined status code: {r.status_code}\nsend this to {owner}') #possible status codes: 400, bad request

    @commands.command()
    async def lbin(self, ctx, *, arg1):
        url = f'https://nariah-dev.com/api/auctions/statistics/{arg1}'
        r = requests.get(url)
        if r.status_code == 200:
            r.raise_for_status()
            jsonr = r.json()
            data = jsonr["data"]
            lbin = data["min"]
            item = arg1.replace("_", " ")
            e = discord.Embed(title=f'Lowest BIN for {item}', description=f'{lbin} coins')
            await ctx.send(embed=e)
        elif r.status_code == 404:
            await ctx.reply(f'No such item ({arg1})')
        elif r.status_code == 500:
            await ctx.reply('An internal error occured')
        else:
            await ctx.reply(f'Undefined status code: {r.status_code}\nsend this to {owner}')
### Commands end ###

### Command exceptions ###
    @giveaway.error
    async def giveaway_error(self, error, ctx):
        if isinstance(error, commands.MissingRole):
            await ctx.reply("You need a role named \"Giveaways\" to run this command")

    @use.error
    async def use_error(self, error, ctx):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Usage of this command: `.use <item> [amount]`")

    @add.error
    async def add_error(self, error, ctx):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Usage of this command: `.add <user> <amount>`")

    @add_item.error
    async def add_item_error(self, error, ctx):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Usage of this command: `.add_item <user> <item/all> [amount]`")
### Command exceptions end ###

def setup(client):
    client.add_cog(MainCog(client))
