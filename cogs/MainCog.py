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
import traceback
import youtube_dl
from time import sleep
from random import randint
from discord.utils import get
from discord.ext import tasks
from discord import TextChannel
from discord.ext import commands
from async_timeout import timeout
from discord.ext.commands import *
### Modules end ###
ids = [
    738290097170153472,
    705462972415213588
]
beta = [
    706697300872921088,
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

class colors: 
    cyan = '\033[96m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

### Commands ###
class MainCog(commands.Cog):
    def __init__(self, client : commands.Bot):
        self.client = client

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
    
    # def load_data(self):
    #     if os.path.isfile(data_filename):                     
    #         if os.path.getsize(data_filename) > 0: 
    #             with open(data_filename, "rb") as file:
    #                 pickle.load(file)
    #     else:
    #         return dict()

    # def load_member_data(self, user_id:int):
    #     data = self.load_data()

    #     if user_id not in data:
    #         return Data(0, 0, 0, 0, 0, 0, 0, 0)
    #     return data[user_id]

    # def save_member_data(self, user_id, member_data):
    #     data = self.load_data()

    #     data[user_id] = member_data

    #     with open(data_filename, "wb") as file:
    #         pickle.dump(data, file)

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
            if message.guild.id not in swearfilter:
                swearfilter[message.guild.id] = 0
            #member_data = self.load_member_data(message.author.id)
            #member_data.xp += 1
            if message.author.id not in xp:
                xp[message.author.id] = 1
            else:
                xp[message.author.id] += 1
            if message.author.id not in levels:
                levels[message.author.id] = 1
            if message.author.id not in wallet:
                wallet[message.author.id] = 0
            if message.author.id not in bank:
                bank[message.author.id] = 0
            if message.author.id not in passiveUsers:
                passiveUsers[message.author.id] = 0
            if message.author.id not in windows10:
                windows10[message.author.id] = 0
            if message.author.id not in bronzecoin:
                bronzecoin[message.author.id] = 0
            if message.author.id not in silvercoin:
                silvercoin[message.author.id] = 0
            if message.author.id not in goldcoin:
                goldcoin[message.author.id] = 0
            xpreq = 0
            if levels[message.author.id] == 1:
                xpreq = 25
            else:             
                for level in range(int(levels[message.author.id])):
                    xpreq += 25
                    if xpreq >= 5000:
                        break
                    else:
                        pass
            if int(xp[message.author.id]) >= xpreq:
                xp[message.author.id] -= xp[message.author.id]
                levels[message.author.id] += 1
                await message.channel.send(f"{message.author.mention} You just leveled up to level **{levels[message.author.id]}**!")
            else:
                pass
            xpreq = 0
            self.save()
            if any(x in message.content.lower() for x in bad):     
                if message.author.id not in warnings:
                    warnings[message.author.id] = 0
                if message.guild.id not in swearfilter:
                    swearfilter[message.guild.id] = 0
                if swearfilter[message.guild.id] == 1:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} Watch your language")
                    warnings[message.author.id] += 1
                    self.save()                                                             
                else:
                    pass
            else:   
                pass
        #await self.client.process_commands(message)

    @commands.command()
    async def shop(self, ctx):
        em = discord.Embed(title=f"Arch bot shop", description=f"Windows 10 key\nDescription: Windows 10 lisence key, too expensive for an os\nCost: 69420\nId: `windows10`\n\nBronze coin\nCost: 50000 coins\nId: `bronzecoin`\n\nSilver coin\nCost: 250000 coins\nId: `silvercoin`\n\nGold coin\nCost: 1000000 coins\nId: `goldcoin`", color=0xff0000)
        em.set_footer(text="Tip: type .buy <item_id> [amount] to buy an item")
        await ctx.reply(embed=em, mention_author=False)
             
    @commands.command(aliases=['inv'])
    async def inventory(self, ctx, user : discord.User=None):
        if user == None:
            em = discord.Embed(title=f"{ctx.message.author.display_name}'s inventory", description=f"Windows 10 keys: {windows10[ctx.message.author.id]}\nBronze coins: {bronzecoin[ctx.message.author.id]}\nSilver coins: {silvercoin[ctx.message.author.id]}\nGold coins: {goldcoin[ctx.message.author.id]}", color=0xff0000)
            await ctx.reply(embed=em, mention_author=False)
        else:
            em = discord.Embed(title=f"{user.display_name}'s inventory", description=f"Windows 10 keys: {windows10[user.id]}\nBronze coins: {bronzecoin[user.id]}\nSilver coins: {silvercoin[user.id]}\nGold coins: {goldcoin[user.id]}", color=0xff0000)
            await ctx.reply(embed=em, mention_author=False)
                  
    @commands.command()
    async def buy(self, ctx, item:str, amount:int=None):
        if str(item) == "windows10":
            if amount == None or int(amount) == 1:
                if wallet[ctx.message.author.id] < 69420:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {round(69420 - wallet[ctx.message.author.id])} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a windows 10 key! Now you have {round(wallet[ctx.message.author.id] - 69420)} coins in your wallet.", mention_author=False)
                    wallet[ctx.message.author.id] -= 69420
                    windows10[ctx.message.author.id] += 1
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
                if wallet[ctx.message.author.id] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - wallet[ctx.message.author.id]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} windows 10 keys for {a} coins. Now you have {wallet[ctx.message.author.id] - a} coins in your wallet")
                    wallet[ctx.message.author.id] -= a
                    windows10[ctx.message.author.id] += amount
                    self.save()
                    return
        if str(item) == "bronzecoin":
            if amount == None or int(amount) == 1:
                if wallet[ctx.message.author.id] < 50000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {50000 - wallet[ctx.message.author.id]} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a bronze coin! Now you have {wallet[ctx.message.author.id] - 50000} coins in your wallet.", mention_author=False)
                    wallet[ctx.message.author.id] -= 50000
                    bronzecoin[ctx.message.author.id] += 1
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
                if wallet[ctx.message.author.id] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - wallet[ctx.message.author.id]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} bronze coins for {a} coins. Now you have {wallet[ctx.message.author.id] - a} coins in your wallet")
                    wallet[ctx.message.author.id] -= a
                    bronzecoin[ctx.message.author.id] += amount
                    self.save()
                    return
        if str(item) == "silvercoin":
            if amount == None or int(amount) == 1:
                if wallet[ctx.message.author.id] < 250000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {250000 - wallet[ctx.message.author.id]} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a silver coin! Now you have {wallet[ctx.message.author.id] - 250000} coins in your wallet.", mention_author=False)
                    wallet[ctx.message.author.id] -= 250000
                    bronzecoin[ctx.message.author.id] += 1
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
                if wallet[ctx.message.author.id] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - wallet[ctx.message.author.id]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} silver coins for {a} coins. Now you have {wallet[ctx.message.author.id] - a} coins in your wallet")
                    wallet[ctx.message.author.id] -= a
                    silvercoin[ctx.message.author.id] += amount
                    self.save()
                    return
        if str(item) == "goldcoin":
            if amount == None or int(amount) == 1:
                if wallet[ctx.message.author.id] < 1000000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {1000000 - wallet[ctx.message.author.id]} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought gold coin! Now you have {wallet[ctx.message.author.id] - 1000000} coins in your wallet.", mention_author=False)
                    wallet[ctx.message.author.id] -= 1000000
                    goldcoin[ctx.message.author.id] += 1
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
                if wallet[ctx.message.author.id] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - wallet[ctx.message.author.id]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} gold coins for {a} coins. Now you have {wallet[ctx.message.author.id] - a} coins in your wallet")
                    wallet[ctx.message.author.id] -= a
                    goldcoin[ctx.message.author.id] += amount
                    self.save()
                    return
        else:
            await ctx.reply(f"No item {item} found. Type `.shop` to get the list of items")
            return
                  
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sweartoggle(self, ctx):
        if int(swearfilter[ctx.message.guild.id]) == 0:
            swearfilter[ctx.message.guild.id] = 1
            self.save()
            await ctx.reply("Enabled swear filter for this server")
        elif int(swearfilter[ctx.message.guild.id]) == 1:
            swearfilter[ctx.message.guild.id] = 0
            self.save()
            await ctx.reply("Disabled swear filter for this server")

    @commands.command(aliases=['goldfish'])
    async def fstab(self, ctx):    
        await ctx.reply('https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg')

    blRank = True
    @commands.command(aliases=['xp'])
    async def rank(self, ctx, user : discord.User=None):
        if user == None:
            xpreq = 0
            if levels[ctx.message.author.id] == 0:
                xpreq = 50
            else:
                for level in range(int(levels[ctx.message.author.id])):
                    xpreq += 50
                    if xpreq >= 5000:
                        break
                    else:
                        pass
            embed = discord.Embed(title=f"{ctx.message.author.display_name}'s Rank", color=0xff0000)
            embed.add_field(name="Level", value=str(levels[ctx.message.author.id]))
            xpv = f"{xp[ctx.message.author.id]}/{xpreq}"
            embed.add_field(name="Exp", value=str(xpv))
            embed.set_footer(text=f'Leveling api made by {owner}')
            await ctx.send(embed=embed)
        else:
            xpreq = 0
            if user.id not in levels:
                levels[user.id] = 1
            if user.id not in xp:
                xp[user.id] = 0
            if levels[user.id] == 1:
                xpreq = 50
            else:
                for level in range(int(levels[user.id])):
                    xpreq += 50
                    if xpreq >= 5000:
                        break
                    else:
                        pass
            embed = discord.Embed(title=f"{user.display_name}'s Rank", color=0xff0000)
            embed.add_field(name="Level", value=str(levels[user.id]))
            xpv = f"{xp[user.id]}/{xpreq}"
            embed.add_field(name="Exp", value=str(xpv))
            embed.set_footer(text=f'Leveling api made by {owner}')
            await ctx.send(embed=embed)

    blAdd_xp = True
    @commands.command()
    async def add_xp(self, ctx, user : discord.User, *, arg1):
        if ctx.message.author.id not in ids:
            await ctx.reply(f'101% sure that this command doesn\'t exist :eyes:')
        else:
            if arg1.isdigit:
                if user.id not in xp:
                    xp[user.id] = 0
                xp[user.id] += int(arg1)
                self.save()
                await ctx.reply(f'Added {arg1} xp to {user.display_name}')
            else:
                await ctx.reply(f'{arg1} is not a number')

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def passive(self, ctx):
        if passiveUsers[ctx.message.author.id] == 1:
            passiveUsers[ctx.message.author.id] = 0
            self.save()
            await ctx.reply(f"Disabled passive mode")
        else:
            passiveUsers[ctx.message.author.id] = 1
            self.save()
            await ctx.reply(f"Enabled passive mode")

    blEdit_snipe = True
    @commands.command()
    async def edit_snipe(self, ctx): 
        try:
            if any(x in after.lower() for x in bad):
                r = lambda: random.randint(0,255)
                col = '#%02X%02X%02X' % (r(),r(),r())
                em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:||{after}||', color=0xff0000)
                em.set_footer(text=f'This message was edited by {author}\nWARNING: this message contains banned text')
            else:
                em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:{after}')
                em.set_footer(text=f'This message was edited by {author}')
            await ctx.send(embed = em)
        except:
            await ctx.reply('No recent edited messages here :eyes:')

    blAdd_lvl = True
    @commands.command()
    async def add_lvl(self, ctx, user : discord.User, *, arg1):
        if ctx.message.author.id not in ids:
            pass
        else:
            if arg1.isdigit:
                if user.id not in levels:
                    levels[user.id] = 1
                levels[user.id] += int(arg1)
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
        rndcol = 0xff0000
        if arg1 == None:
            helpMain = discord.Embed(title='**COMMAND LIST**', description='Economy\nbeg, balance, daily, weekly, monthly, postmeme, work, guess, give, deposit, withdraw, shop, buy, inventory, passive\n\nModeration\nban, kick, purge, nuke, snipe, warns, sweartoggle\n\nMisc\nmeme, linuxmeme, softwaregore, ihadastroke, stroke, say, edit_snipe, 8ball')
            helpMain.set_footer(text='*type .help [command] to get more info about a command*')
            await ctx.reply(embed = helpMain)
        elif arg1 == 'beg':
            em1 = discord.Embed(title='\'Beg\' command use', description='Gives an amount of coins to the user.\nCooldown: 30 seconds\nUsage: `.beg`', color=rndcol)
            await ctx.reply(embed=em1)
        elif arg1 == 'balance' or arg1 == 'bal':
            em2 = discord.Embed(title='\'Balance\' command use', description='Shows the amount of a user\nAliases: bal\nUsage `.balance|.bal` [@user]', color=rndcol)
            em2.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em2)
        elif arg1 == 'hunt':
            em3 = discord.Embed(title='\'Hunt\' command use', description='Goes for hunting to get moneu\nCooldown: 30 seconds\nUsage: `.hunt`', color=rndcol)
            await ctx.reply(embed=em3)
        elif arg1 == 'daily':
            em4 = discord.Embed(title='\'Daily\' command use', description='Gives an amount of coins\nCooldown: 1 day\nUsage: `.daily`', color=rndcol)
            await ctx.reply(embed=em4)
        elif arg1 == 'weekly':
            em5 = discord.Embed(title='\'Weekly\' command use', description='Gives an amount of coins\nCooldown: 1 week\nUsage: `.weekly`', color=rndcol)
            await ctx.reply(embed=em5)
        elif arg1 == 'monthly':
            em6 = discord.Embed(title='\'Monthly\' command use', description='Gives an amount of coins\nCooldown: 1 month\nUsage: `.monthly`', color=rndcol)
            await ctx.reply(embed=em6)
        elif arg1 == 'postmeme' or arg1 == 'pm':
            em7 = discord.Embed(title='\'Post meme\' command use', description='Posts a meme and gets money\nCooldown: 40 seconds\nUsage: `.postmeme|.pm`', color=rndcol)
            await ctx.reply(embed=em7)
        elif arg1 == 'ban':
            em8 = discord.Embed(title='\'Ban\' command use', description='Bans a user from the server\nUsage: `.ban <@user>`\nPermissions needed: ban members', color=rndcol)
            em8.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em8)
        elif arg1 == 'kick':
            em9 = discord.Embed(title='\'Kick\' command use', description='Kicks a user from the server\nUsage: `.kick <@user>`\nPermissions needed: kick members', color=rndcol)
            em9.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em9)
        elif arg1 == 'nuke':
            em10 = discord.Embed(title='\'Nuke\' command use', description='Deletes all the messages from a channel\nUsage: `.nuke <#channel>`\nPermissions needed: manage channels', color=rndcol)
            em10.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em10)
        elif arg1 == 'purge':
            em11 = discord.Embed(title='\'Purge\' command use', description='Deletes an amount of messages in the channel\nUsage: `.purge <amount>`\nPermissions needed: manage messages or manage channels')
            em11.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em11)
        elif arg1 == '8ball':
            em12 = discord.Embed(title='\'8ball\' command use', description='Asks a qustion to the bot and responds with a random answer\nUsage: `.8ball <question>', color=rndcol)
            em12.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em12)
        elif arg1 == 'meme':
            em13 = discord.Embed(title='\'Meme\' command use', description='Sends a random meme from r/memes\nUsage: `.meme`', color=rndcol)
            await ctx.reply(embed=em13)
        elif arg1 == 'ihadastroke':
            em14 = discord.Embed(title='\'Ihadastroke\' command use', description='Sends a random image from r/ihadastroke\nUsage: `.ihadastroke`', color=rndcol)
            await ctx.reply(embed=em14)
        elif arg1 == 'softwaregore' or arg1 == 'sg':
            em15 = discord.Embed(title='\'Softwaregore\' command use', description='Sends a random image from r/softwaregore\nUsage: `.softwaregore|.sg`', color=rndcol)
            await ctx.reply(embed=em15)
        elif arg1 == 'linuxmeme' or arg1 == 'lm':
            em16 = discord.Embed(title='\'Linuxmeme\' command use', description='Sends a random meme from r/linuxmemes\nUsage: `.linuxmeme|.lm`', color=rndcol)
            await ctx.reply(embed=em16)
        elif arg1 == 'work':
            em17 = discord.Embed(title='\'Work\' command use', description='Gets a big amount of money\nCooldown: 30 minutes\nUsage: `.work`', color=rndcol)
            await ctx.reply(embed=em17)
        elif arg1 == 'stroke':
            em18 = discord.Embed(title='\'Stroke\' command use', description='Sends a stroke (not irl stroke)\nUsage: `.stroke <amount>`\nAmount limit: 750', color=rndcol)
            em18.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em18)
        elif arg1 == 'invites':
            em19 = discord.Embed(title='\'Invites\' command use', description='Shows the amount of people the user invited\nUsage: `.invites [user]`', color=rndcol)
            em19.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em19)
        elif arg1 == 'snipe':
            em20 = discord.Embed(title='\'Snipe\' command use', description='Shows the last deleted message in the channel\nUsage: `.snipe`', color=rndcol)
            await ctx.reply(embed=em20)
        elif arg1 == 'edit_snipe' or arg1 == 'edit-snipe' or arg1 == 'edit':
            em21 = discord.Embed(title='\'Edit snipe\' command use', description='Shows the last edited message in the channel\nUsage: `.edit_snipe|.edit`\nAvailability: beta only', color=rndcol)
            await ctx.reply(embed=em21)
        elif arg1 == 'highlow' or arg1 == 'hl':
            em22 = discord.Embed(title='\'Highlow\' command use', description='The bot generates 2 random numbers. The first one doesn\'t send it and the second one does. You have to guess if the hidden number is lower, higher or equal to the sent one\nCooldown: 40 seconds\nUsage: `.highlow|.hl`\nResponses: higher, lower, jackpot', color=rndcol)
            await ctx.reply(embed=em22)
        elif arg1 == 'kill':
            em23 = discord.Embed(title='\'Kill\' command use', description='*kills* a user\nUsage: `.kill <@user>`', color=rndcol)
            em23.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em23)
        elif arg1 == 'fstab' or arg1 == 'fstab.goldfish':
            em24 = discord.Embed(title='\'Fstab\' command use', description='Sends the meme fstab.goldfish\nUsage: `.fstab`', color=rndcol)
            await ctx.reply(embed=em24)
        elif arg1 == 'slap':
            em25 = discord.Embed(title='\'Slap\' command use', description='*slaps* a user\nUsage: `.slap <@user>', color=rndcol)
            await ctx.reply(embed=em25)
        elif arg1 == 'guess':
            em26 = discord.Embed(title='\'Guess\' command use', description='You have to gues a number from 1 to 10. If you find it you get some coins\nCooldown: 30 seconds\nUsage: `.guess <number>`', color=rndcol)
            em26.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em26)
        elif arg1 == 'give' or arg1 == 'gift':
            em27 = discord.Embed(title='\'Give\' command use', description='Gives coins to a user mentioned\nUsage: `.give|.gift <@user> <amount>', color=rndcol)
            em27.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em27)
        elif arg1 == 'isSus' or arg1 == 'sus':
            em28 = discord.Embed(title='\'Sus\' command use', description='Checks if a user is sus\nUsage: `.isSus|.sus <@user>`', color=rndcol)
            em28.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em28)
        elif arg1 == 'add':
            em29 = discord.Embed(title='\'Add\' command use', description='Adds coins to a user\nAvailability: __developer only__\nUsage: `.add <@user> <amount:int/hex/bin>`', color=rndcol)
            em29.set_footer(text=f'This command can be only used by {owner}')
            await ctx.reply(embed=em29)
        elif arg1 == 'add_xp':
            em30 = discord.Embed(title='\'Add xp\' command use', description='Adds xp to a user\nAvailability: __developer only__\nUsage: `.add_xp <@user> <amount:int/hex/bin>`', color=rndcol)
            em30.set_footer(text=f'This command can be only used by {owner}')
            await ctx.reply(embed=em30)
        elif arg1 == 'add_lvl':
            em31 = discord.Embed(title='\'Add levels\' command use', description='Adds levels to a user\nAvailability: __developer only__\nUsage: `.add_lvl <@user> <amount:int/hex/bin>', color=rndcol)
            em31.set_footer(text=f'This command can be only used by {owner}')
            await ctx.reply(embed=em31)
        elif arg1 == 'fish':
            em32 = discord.Embed(title='\'Fish\' command use', description='Fishes stuff\nCooldown: 30 seconds\nUsage `.fish`', color=rndcol)
            await ctx.reply(embed=em32)
        elif arg1 == 'deposit' or arg1 == 'dep':
            em33 = discord.Embed(title='\'Deposit\' command use', description='Deposits coins and puts them in the bank\nUsage: `.deposit|.dep <max/all/amount:int>`', color=rndcol)
            em33.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em33)
        elif arg1 == 'withdraw' or arg1 == 'with':
            em34 = discord.Embed(title='\'Withdraw\' command use', description='Withdraws coins and puts them in the wallet\nUsage: `.withdraw|.with <max/all/amount:int>', color=rndcol)
            em34.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em34)
        elif arg1 == 'shop':
            em35 = discord.Embed(title='\'Shop\' command use', description='Shows the items in shop\nUsage: `.shop`', color=rndcol)
            await ctx.reply(embed=em35)
        elif arg1 == 'inventory' or arg1 == 'inv':
            em36 = discord.Embed(title='\'Inventory\' command use', description='Shows a user\'s inventory\nUsage: `.inventory|.inv [@user]', color=rndcol)
            em36.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em36)
        elif arg1 == 'rob':
            em37 = discord.Embed(title='\'Rob\' command use', description='Robs a user\nUsage: `.rob <@user>`', color=rndcol)
            em37.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em37)
        elif arg1 == 'networth' or arg1 == 'nw':
            em38 = discord.Embed(title='\'Networth\' command use', description='Shows the networth of a player in hypixel skyblock\nUsage: `.networth|.nw <playername> [profile]', color=rndcol)
            em38.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em38)
        elif arg1 == 'auctionhouse' or arg1 == 'ah' or arg1 == 'auction_house':
            em39 = discord.Embed(title='\'Auction house\' command use', description='Shows the auction stats of an item in hypixel skyblock\nUsage: `.auctionhouse|.ah <item_id>`', color=rndcol)
            em39.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em39)
        elif arg1 == 'lbin':
            em40 = discord.Embed(title='\'Lowest BIN\' command use', description='Shows the lowest price of an item in hypixel skyblock\nUsage: `.lbin <item_id>`', color=rndcol)
            em40.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em40)
        elif arg1 == 'say':
            em41 = discord.Embed(title='\'Say\' command use', description='Says stuff\nUsage: `.say <text>', color=rndcol)
            em41.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em41)
        elif arg1 == 'play':
            em42 = discord.Embed(title='\'Play\' command use', description='Plays a song in a voice channel\nUsage: `.play|.p <song_name/url>`\n**This command is under development**', color=rndcol)
            em42.set_footer(text='<> is required and [] is optional argument')
            await ctx.reply(embed=em42)
        elif arg1 == 'join':
            em43 = discord.Embed(title='\'Join\' command use', description='Joins a voice channel\nUsage `.join [#channel]`', color=rndcol)
            await ctx.reply(embed=em43)
        elif arg1 == 'leave':
            em44 = discord.Embed(title='\'Leave\' command use', description='Leaves the current connected voice channel\nUsage: `.leave`', color=rndcol)
            await ctx.reply(embed=em44)
        elif arg1 == 'stop':
            em45 = discord.Embed(title='\'Stop\' command use', description='Stops the current playing song\nUsage: `.stop`', color=rndcol)
            await ctx.reply(embed=em45)
        elif arg1 == 'pause':
            em46 = discord.Embed(title='\'Pause\' command use', description='Pauses the current playing song\nUsage: `.pause`', color=rndcol)
            await ctx.reply(embed=em46)
        elif arg1 == 'resume':
            em47 = discord.Embed(title='\'Resume\' command use', description='Resumes a paused song\nUsage: `.resume`', color=rndcol)
            await ctx.reply(embed=em47)
        elif arg1 == 'masterhacker':
            em48 = discord.Embed(title='\'Masterhacker\' command use', description='Sends a random image from r/masterhacker\nUsage: `.masterhacker`', color=rndcol)
            await ctx.reply(embed=em48)
        elif arg1 == 'passive':
            em49 = discord.Embed(title='\'Passive\' command use', description='Toggles passive mode. If it is turned on people\ncan\'t rob you but you can\'t rob people too\nCooldown: 1 hour\nUsage `.passive`', color=rndcol)
            await ctx.reply(embed=em49)
        elif arg1 == 'sweartoggle':
            em50 = discord.Embed(title='\'Sweartoggle\' command use', description='Toggles swear filter for a server. If enabled, when someone sends\na banned word, i will delete it and give the user a warn\nPermissions required: Administrator\nUsage: `.sweartoggle`', color=rndcol)
            await ctx.reply(embed=em50)
        elif arg1 == 'summon':
            em51 = discord.Embed(title='\'Summon\' command use', description='Joins in the channel where the message author is\nUsage: `.summon`')
            await ctx.reply(embed=em51)
        elif arg1 == 'now':
            em52 = discord.Embed(title='\'Now\' command use', description='Shows the current playing song')
            await ctx.reply(embed=em52)
        elif arg1 == 'queue':
            em53 = discord.Embed(title='\'Queue\' command use', description='Shows songs in queue')
            await ctx.reply(embed=em53)
        elif arg1 == 'buy':
            em54 = discord.Embed(title='\'Buy\' command use', description='Buys an item from the shop (`.shop`)\nUsage: `.buy <item> [amount]`')
            await ctx.reply(embed=em54)
        elif arg1 == 'help':
            await ctx.reply('You want help for help command?')
            def check(msg):
                return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

            msg = await self.client.wait_for("message", check=check)
            if msg.content == 'yes':
                await ctx.send('ok gimme a sec')
                async with ctx.typing():
                    await asyncio.sleep(2)
                h = discord.Embed(title='\'Help\' command use', description='helps\nusage: .help [command]', color=rndcol)
                h.set_footer(text='why the fk do u need help with this command')
                await ctx.send(embed=h)
            elif msg.content == 'no':
                await ctx.send("ok")
            else:
                pass
        else:
            await ctx.reply(f"No command \"{arg1}\" found")

    @commands.command()
    async def warns(self, ctx, *, user : discord.User=None):
        if user == None:
            await ctx.reply(f"You have {warnings[ctx.message.author.id]} warnings")
        else:
            await ctx.reply(f"{user.display_name} has {warnings[user.id]} warnings")

    blStroke = True
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
        e = discord.Embed(title=f'{question}', description=f'{random.choice(responses)}')
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
        totalInvites = 0
        if user == None:
            for i in await ctx.guild.invites():
                if i.inviter == ctx.author:
                    totalInvites += i.uses
            e = discord.Embed(title=f'{ctx.message.author.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}")
            await ctx.reply(embed=e)
        elif user.bot:
            await ctx.reply('This is a bot not a user')
            return
        else:
            for i in await ctx.guild.invites():
                if i.inviter == user:
                    totalInvites += i.uses
            e = discord.Embed(title=f'{user.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}")
            await ctx.reply(embed=e)

    blPurge = True
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def purge(self, ctx, amount:int):
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
        embedSuccessPurge = discord.Embed(title=':Purge Successful', description=f'Purged {amount} messages from this channel.')
        await ctx.send(embed = embedSuccessPurge)

    blMeme = True
    @commands.command()
    async def meme(self, ctx):
        async with ctx.typing():
            memes_submissions = reddit.subreddit('memes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title)
            embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

    blRstroke = True
    @commands.command()
    async def ihadastroke(self, ctx):
        async with ctx.typing():
            memes_submissions = reddit.subreddit('ihadastroke').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title)
            embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

    @commands.command(aliases=['mh'])
    async def masterhacker(self, ctx):
        async with ctx.typing():
            memes_submissions = reddit.subreddit('masterhacker').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title)
            embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

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
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        numb = randint(1, 100)
        numb2 = randint(1, 100)
        id = ctx.message.author.id
        coins = randint(300, 1000)

        def check(msg):
            return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

        await ctx.send(f'Your number is {numb} choose if the other is lower, higher or jackpot')
        msg = await self.client.wait_for("message", check=check)
        if msg.content == 'low':
            if numb > numb2:
                await ctx.send(f'Congrats, your number was {numb2} and you earned {coins} coins')
                wallet[ctx.message.author.id] += coins
                self.save()
                if bool(log) == True:
                    print(f'[{current_time}]{ctx.message.author.display_name} earned {coins} coins')
                else:
                    pass
            elif numb < numb2:
                await ctx.send(f'Incorrect the number was {numb2}')
            elif numb == numb2:
                await ctx.send(f'You stupid you could won 1 mil coins if you choose jackpot')
        if msg.content == 'jackpot':
            if numb == numb2:
                coins2 = randint(1000000, 5000000)
                await ctx.send(f'Congrats, your number was {numb2} and you earned {coins2} coins gg!')
                wallet[ctx.message.author.id] += coins2
                self.save()
                if bool(log) == True:
                    print(f'[{current_time}]{ctx.message.author.display_name} earned {coins2} coins')
                else:
                    pass
            else:
                await ctx.send(f'Incorrect the number was {numb2}')
        if msg.content == 'high':
            if numb < numb2:
                await ctx.send(f'Congrats, your number was {numb2} and you earned {coins} coins')
                wallet[ctx.message.author.id] += coins
                self.save_member_data(id, member_data)
                if bool(log) == True:
                    print(f'[{current_time}]{ctx.message.author.display_name} earned {coins} coins')
                else:
                    pass
            else:
                await ctx.send(f'Incorrect your number was {numb2}')
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
                f"<@{user.id}> died from a dang baguette",
                f"<@{ctx.message.author.id}> strikes <@{user.id}> with the killing curse... *Avada Kedavra!*",
                f"<@{user.id}> dies from dabbing too hard",
                f"<@{user.id}> ripped their own heart out to show their love for <@{ctx.message.author.id}>"
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
        e = discord.Embed(title=f'{ctx.message.author} slaps {user}')
        e.set_image(url=f'{random.choice(responses3)}')
        await ctx.send(embed = e)

    @commands.command(aliases=['sg'])
    async def softwaregore(self, ctx):
        sg_submissions = reddit.subreddit('softwaregore').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in sg_submissions if not x.stickied)
        embed = discord.Embed(title = submission.title)
        embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def guess(self, ctx, num:int):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        x = randint(1, 10)
        if num == x:
            coins = randint(100, 1000)
            await ctx.reply(f'Correct! You got {coins} coins')
            wallet[ctx.message.author.id] += coins
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
            wallet[ctx.message.author.id] += x
            self.save()
            if bool(log) == True:
                print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} has earned {colors.green}{x}{colors.end} coins')
            else:
                pass

    @commands.command()
    async def null(self, ctx):
        await ctx.reply('You got **null** coins dood.')

    @commands.command(aliases=['gift'])
    async def give(self, ctx, user : discord.User, *, arg1):
        if user.id == ctx.message.author.id:
            await ctx.reply('You can\'t give coins to yourself')
            return
        else:
            if arg1.isdigit:
                if passiveUsers[ctx.message.author.id] == 1:
                    await ctx.reply("You have passive mode enabled, you can\'t give momey to other users", mention_author=False)
                    return
                if passiveUsers[user.id] == 1:
                    await ctx.reply("This user has passive mode enabled. Leave them alone!", mention_author=False)
                    return
                if wallet[ctx.message.author.id] < int(arg1):
                    await ctx.reply('You don\'t have that many coins in your wallet')
                    return
                elif int(arg1) < 0:
                    await ctx.reply('Don\'t try to break me **dood**')
                elif int(arg1) == 0:
                    await ctx.reply('You can\'t gift 0 coins')
                else:
                    wallet[ctx.message.author.id] -= int(arg1)
                    self.save()
                    wallet[user.id] += int(arg1)
                    self.save()
                    await ctx.reply(f'You gave {arg1} coins to {user.display_name}')
            else:
                await ctx.reply(f'{arg1} is not a digit **dood**')

    @commands.command()
    async def add(self, ctx, user : discord.User, *, arg1=None):
        if ctx.message.author.id not in ids:
            await ctx.reply(f'101% sure that this command doesn\'t exist :eyes:')
            return
        else:
            if user.id not in wallet:
                wallet[user.id] = 0
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            if arg1.startswith('0x') or arg1.startswith('-0x'):
                try:
                    hexv = int(f'{arg1}', 16)
                    wallet[user.id] += int(hexv)
                    self.save()
                    await ctx.send(f'Added {hexv} coins to {user.display_name}\'s account')
                    print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} added {colors.green}{hexv}{colors.end} coins to {colors.cyan}{user.display_name}\'s{colors.end} account')
                except ValueError:
                    await ctx.send(f'Invalid hex value')
            elif arg1.startswith('0b') or arg1.startswith('-0b'):
                try:
                    binv = int(f'{arg1}', 2)
                    wallet[user.id] += int(binv)
                    self.save()
                    await ctx.send(f'Added {binv} coins to {user.display_name}\'s account')
                    print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} added {colors.green}{binv}{colors.end} coins to {colors.cyan}{user.display_name}\'s{colors.end} account')
                except ValueError:
                    await ctx.send('Invalid binary value')
            elif arg1.isdigit:
                wallet[user.id] += int(arg1)
                self.save()
                await ctx.send(f'Added {arg1} coins to {user.display_name}\'s account')
                if bool(log) == True:
                    print(f"[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} added {colors.green}{arg1}{colors.end} coins to {colors.cyan}{user.display_name}{colors.end}\'s account")
                else:
                    pass
            elif arg1 == None:
                await ctx.reply('Usage: `;add <user> binary\\hex\\decimal`')
                return
            else:
                await ctx.send('Invalid value.')
            

    @commands.command()
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def work(self, ctx):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        coins = randint(1000, 50000)
        wallet[ctx.message.author.id] += coins
        await ctx.send(f"You earned {coins} coins.")
        self.save()
        if bool(log) == True:
            print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} earned {colors.green}{coins}{colors.end} coins')
        else:
            pass

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def beg(self, ctx):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        coins = randint(1, 500)
        wallet[ctx.message.author.id] += coins
        await ctx.send(f'You earned {coins} coins.')
        self.save()

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        if bool(currency) == False:
            await ctx.reply('Currency is disabled')
            return
        else:
            pass
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S") 
        wallet[ctx.message.author.id] += 10000
        await ctx.send('You claimed 10,000 coins')
        self.save()
        if bool(log) == True:
            print(f'[{current_time}]{ctx.message.author.display_name} claimed 10k coins from daily command')
        else:
            pass

    @commands.command(aliases=['dep'])
    async def deposit(self, ctx, *, arg1):
        if bool(currency) == False:
            await ctx.send('Currency is disabled')
            return
        else:
            if arg1 == 'all' or arg1 == 'max':
                if wallet[ctx.message.author.id] == 0:
                    await ctx.send('You don\'t have any coins in your wallet')
                    return
                else:
                    if wallet[ctx.message.author.id] == 1:
                        await ctx.reply(f'You deposited 1 coin')
                    else:
                        await ctx.reply(f'You deposited {wallet[ctx.message.author.id]} coins')    
                    bank[ctx.message.author.id] += int(wallet[ctx.message.author.id])
                    wallet[ctx.message.author.id] -= int(wallet[ctx.message.author.id])
                    self.save()
                    return
            elif arg1.isdigit:
                if int(arg1) > wallet[ctx.message.author.id]:
                    await ctx.reply('You don\'t have that many coins in your wallet')
                    return
                elif int(arg1) < 0:
                    await ctx.reply('Don\'t try to break me dood')
                    return
                else:
                    await ctx.send(f'You deposited {arg1} coins')
                    wallet[ctx.message.author.id] -= int(arg1)
                    bank[ctx.message.author.id] += int(arg1)
                    self.save()
                    return
            else:
                raise BadArgument

    @commands.command(aliases=['with'])
    async def withdraw(self, ctx, *, arg1):
        if bool(currency) == False:
            await ctx.send('Currency is disabled')
            return
        else:
            if arg1 == 'all' or arg1 == 'max':
                if bank[ctx.message.author.id] == 0:
                    await ctx.send('You don\'t have any coins in your bank')
                    return
                else:
                    if member_data.bank == 1:
                        await ctx.reply(f'You withdrawn {bank[ctx.message.author.id]} coin')
                    else:
                        await ctx.reply(f'You withdrawn {bank[ctx.message.author.id]} coins')    
                    wallet[ctx.message.author.id] += int(bank[ctx.message.author.id])
                    bank[ctx.message.author.id] -= int(bank[ctx.message.author.id])
                    self.save()
                    return
            elif arg1.isdigit:
                if int(arg1) > bank[ctx.message.author.id]:
                    await ctx.reply('You don\'t have that many coins in your bank')
                    return
                elif int(arg1) < 0:
                    await ctx.reply('Don\'t try to break me dood')
                    return
                else:
                    await ctx.send(f'You withdrawn {arg1} coins')
                    wallet[ctx.message.author.id] += int(arg1)
                    bank[ctx.message.author.id] -= int(arg1)
                    self.save()
                    return
            else:
                raise BadArgument

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def rob(self, ctx, *, user : discord.User):
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
            if user.id not in wallet:
                wallet[user.id] = 0
            if user.id not in passiveUsers:
                passiveUsers[user.id] = 0
            if passiveUsers[ctx.message.author.id] == 1:
                await ctx.reply(f"You are on passive mode. You can\'t rob other people")
                return
            if passiveUsers[user.id] == 1:
                await ctx.reply(f"{user.display_name} has passive mode turned on. You can\'t rob them")
                return
            if wallet[user.id] < 500:
                await ctx.send('This user has less than 500 coins')
            elif wallet[user.id] >= 500:
                coins = randint(500, wallet[user.id])
                if bool(log) == True:
                    print(f'[{current_time}]{ctx.message.author.display_name} stole {coins} coins from {user.display_name}')
                else:
                    pass
                wallet[user.id] -= coins
                self.save()
                wallet[ctx.message.author.id] += coins
                self.save()
                await ctx.send(f'You stole {coins} coins from **{user.display_name}**')

    @commands.command()
    @commands.cooldown(1, 604800, commands.BucketType.user)
    async def weekly(self, ctx):
        if bool(currency) == False:
            await ctx.send('Currency is disabled')
            return
        else:
            pass
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        wallet[ctx.message.author.id] += 50000
        await ctx.reply('You claimed 50,000 coins')
        self.save()
        if bool(log) == True:
            print(f'[{current_time}]{ctx.message.author.display_name} claimed 50k coins from weekly command')
        else:
            pass

    @commands.command()
    @commands.cooldown(1, 2592000, commands.BucketType.user)
    async def monthly(self, ctx):
        if bool(currency) == False:
            await ctx.send('Currency is disabled')
            return
        else:
            pass
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        wallet[ctx.message.author.id] += 100000
        await ctx.send('You claimed 100,000 coins')
        self.save()
        if bool(log) == True:
            print(f'[{current_time}]{ctx.message.author.display_name} claimed 100k coins from monthly command')
        else:
            pass

    @commands.command(aliases=['bal'])
    async def balance(self, ctx, user : discord.User=None):
        if bool(currency) == False:
            await ctx.send('Currency is disabled')
            return
        else:
            pass
        if user == None:
            embed = discord.Embed(title=f"{ctx.message.author.display_name}'s Balance")
            embed.add_field(name="Wallet", value=str(wallet[ctx.message.author.id]))
            embed.add_field(name="Bank", value=str(bank[ctx.message.author.id]))
            embed.set_footer(text=f'Currency api made by {owner}')
            await ctx.send(embed=embed)
        else:
            if user.id not in wallet:
                wallet[user.id] = 0
            if user.id not in bank:
                bank[user.id] = 0
            embed = discord.Embed(title=f"{user.display_name}'s Balance")
            embed.add_field(name="Wallet", value=str(wallet[user.id]))
            embed.add_field(name="Bank", value=str(bank[user.id]))
            embed.set_footer(text=f'Currency api made by {owner}')
            await ctx.send(embed=embed)

    @commands.command(aliases=["lm"])
    async def linuxmeme(self, ctx):
        async with ctx.typing():
            memes_submissions = reddit.subreddit('linuxmemes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title)
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
def setup(client):
    client.add_cog(MainCog(client))
