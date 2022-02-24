### Modules ###
import os
import time
import os.path
import discord
import json
import datetime
import threading
from discord_slash import SlashCommand
from keep_alive import keep_alive
from discord.ext import commands
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

def get_prefix(client, message):
    with open(f"{cwd}/database/prefixes.json", 'r') as f:
        prefixes = json.load(f)
    
    if str(message.guild.id) not in prefixes:
        prefixes[str(message.guild.id)] = "."   
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=commands.when_mentioned_or(get_prefix), intents=intents)
slash = SlashCommand(client)
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

def foo():
    v = 1
    while True:
        time.sleep(300)
        print(f"hit {v}")
        v += 1

b = threading.Thread(target=foo)
b.daemon = True
b.start()

## Events ###
@client.event
async def on_ready():
    count = 0
    for guild in client.guilds:
        count += guild.member_count
    await client.change_presence(status="idle", activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} guilds, {count} users | .help"))
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            if filename == "Events.py":
                pass
            else:
                client.load_extension(f'cogs.{filename[:-3]}')
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
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
async def on_message_edit(message_before, message_after):
        global author
        author = message_before.author
        guild = message_before.guild.id
        channel = message_before.channel
        global before
        before = message_before.content
        global after
        after = message_after.content

snipe_message_author = {}
snipe_message_content = {}

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

@client.event
async def on_guild_join(guild):
    count = 0
    for guild in client.guilds:
        count += guild.member_count
    prefix[str(guild.id)] = "."
    await client.change_presence(status="idle", activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} guilds, {count} users | .help"))

@client.event
async def on_guild_remove(guild):
    count = 0
    for guild in client.guilds:
        count += guild.member_count
    await client.change_presence(status="idle", activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} guilds, {count} users | .help"))

@client.event
async def on_member_join(member):
    count = 0
    for guild in client.guilds:
        count += guild.member_count
    with open(f"{os.getcwd()}/database/welcome.json", "r") as f:
        welcome = json.load(f)
    if str(guild.id) not in welcome:
        pass
    else:
        await member.send(f"{welcome[str(guild.id)]}")
    await client.change_presence(status="idle", activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} guilds, {count} users | .help"))

@client.event
async def on_member_remove(member):
    count = 0
    for guild in client.guilds:
        count += guild.member_count
    await client.change_presence(status="idle", activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} guilds, {count} users | .help"))

@client.event
async def on_message(message):
    try:
        if message.mentions[0] == client.user:
            with open(f"{cwd}/database/prefixes.json", 'r') as f:
                prefixes = json.load(f)
            if str(message.guild.id) not in prefixes:
                prefix = "."
            else:
                prefix = prefixes[str(message.guild.id)]
            await message.channel.send(f"My prefix for this guild is {prefix}")
    except:
        pass

    await client.process_commands(message)
### Events end ###

@client.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix:str):
    with open(f"{cwd}/database/prefixes.json", "r") as f:
        prefixes = json.load(f)
    
    prefixes[str(ctx.guild.id)] = prefix
    await ctx.reply(f"Set server prefix to {prefix}")
    with open(f"{cwd}/database/prefixes.json", "w+") as f:
        json.dump(prefixes, f)

@client.command()
@commands.has_permissions(administrator=True)
async def resetprefix(ctx):
    with open(f"{cwd}/database/prefixes.json", "r") as f:
        prefixes = json.load(f)
    
    prefixes[str(ctx.guild.id)] = "."
    await ctx.reply("The prefix has been reset")
    with open(f"{cwd}/database/prefixes.json", "w+") as f:
        json.dump(prefixes, f)
        
@client.command()
async def snipe(ctx):
    with open(f"{os.getcwd()}/database/bannedwords.json", "r"):
        bannedwords = json.load(f)
    try:
        bad = bannedwords[str(ctx.guild.id)]
    except KeyError:
        bad = list()
    channel = ctx.channel
    try:
        if any(x in snipe_message_content[channel.id].lower() for x in bad):
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description =f"||{snipe_message_content[channel.id]}||", color=discord.Colour.random())
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}\nWarning: this message contains banned words")
            await ctx.send(embed = em)
        else:
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=discord.Colour.random())
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
    except:
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")


@client.command()
async def load(ctx, *, arg1):
    if ctx.message.author.id == 705462972415213588:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        return
    try:
        client.load_extension(f'cogs.{arg1}')
        await ctx.send("Loaded Cog")
        return
    except Exception as e:
        await ctx.send(e)

@client.command()
async def unload(ctx, *, arg1):
    if ctx.message.author.id == 705462972415213588:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        return
    try:
        client.unload_extension(f'cogs.{arg1}')
        await ctx.send("Unloaded Cog")
        return
    except Exception as e:
        await ctx.send(e)


@client.command()
async def reload(ctx, *, arg1):
    if ctx.message.author.id == 705462972415213588:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        return
    try:
        client.unload_extension(f'cogs.{arg1}')
        client.load_extension(f'cogs.{arg1}')
        await ctx.send("Reloaded Cog")
        return
    except Exception as e:
        await ctx.send(e)

keep_alive()
client.run("")
