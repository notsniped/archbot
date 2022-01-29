### Modules ###
import os
import sys
import time
import praw
import math
import random
import string
import os.path
import discord
import asyncio
import datetime
import json
import requests
import threading
from html.parser import HTMLParser
import prawcore
import functools
import itertools
import translate
import youtube_dl
import traceback
import pyduktape
from time import sleep
from contextlib import redirect_stdout
import base64
import traceback
import io
import inspect
import textwrap
import subprocess
from random import randint
from discord.utils import get
from discord.ext import tasks
from discord import TextChannel
from discord.ext import commands
from discord.ext.commands import *
from interpreter.interpreter.interpreter import Interpreter
### Modules end ###
on_cooldown = {}
cd = {}
work_cooldown = 1700
invest_time = 3600
no_cooldowns = [
    705462972415213588,
    884765170184896562,
    706697300872921088
]
ids = [
    705462972415213588,
    695640751933096027,
    706697300872921088,
    884765170184896562
]
beta = [
    778241840562044960
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
###database values
##user
#0: wallet
#1: bank
#2: invest
#3: rng
#4: xp
#5: level
#6: isPassive
#7: job
#8: warnings
#9: windows10
#10: bronzecoin
#11: silvercoin
#12: goldcoin
#13: normalbox
#14: dailybox
#15: devbox
#16: prestige
#17: commands used
#18: banknotes
#19: bank space
##guild
#0: swearfilter
#1: level up channel
#2: bannedwords
#3: link blocker
#4: whitelist
#5: welcome
#6: countconfig
with open(f'{cwd}/database/users.json', 'r') as f:
    global userdat
    userdat = json.load(f)
with open(f"{cwd}/database/guild.json", "r") as f:
    global gdata
    gdata = json.load(f)

userlen = 20
for user in userdat.keys():
    if len(userdat[user]) != userlen:
        var = userlen - len(userdat[user])
        for i in range(var):
            userdat[user].append(0)

glen = 7
for guild in gdata.keys():
    if len(gdata[guild]) != glen:
        var = glen - len(gdata[guild])
        for i in range(var):
            gdata[guild].append(0)

class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    def gettime(self):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        return f"[{st}]"

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'): return
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None: return
        ignored = (commands.CommandNotFound)
        error = getattr(error, 'original', error)
        if isinstance(error, ignored): return
        if isinstance(error, commands.DisabledCommand): await ctx.send(f'{ctx.command} has been disabled.')
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass       
        if isinstance(error, commands.CommandOnCooldown):
            print(f"{self.gettime()}CommandOnCooldown triggered by {ctx.author} in {ctx.command}")
            if math.ceil(error.retry_after) < 60:
                await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(error.retry_after)} seconds')
            elif math.ceil(error.retry_after) < 3600:
                ret = math.ceil(error.retry_after) / 60
                await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(ret)} minutes')
            elif math.ceil(error.retry_after) >= 3600:
                ret = math.ceil(error.retry_after) / 3600
                if ret >= 24:
                    r = math.ceil(ret) / 24
                    await ctx.reply(f"This command is on cooldown. Please try after {r} days")
                else:
                    await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(ret)} hours')
        elif isinstance(error, commands.BadArgument):
            print(f"{self.gettime()}BadArgument triggered by {ctx.author} in {ctx.command}")
            if ctx.command.qualified_name == 'tag list':
                await ctx.send('I could not find that member. Please try again.')
            else:
                await ctx.send("Invalid argument")
        elif isinstance(error, commands.MissingRequiredArgument): await ctx.send("Missing required argument")
        elif isinstance(error, commands.MissingPermissions): await ctx.reply("You can\'t use this")
        elif isinstance(error, commands.BotMissingPermissions): await ctx.reply("I don\'t have permissions to use this")
        elif isinstance(error, commands.errors.NSFWChannelRequired): await ctx.reply("This command only works in a nsfw channel")
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

youtube_dl.utils.bug_reports_message = lambda: ''


class VoiceError(Exception):
    pass

class YTDLError(Exception):
    pass

class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)
        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data
        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**{0.title}** by **{0.uploader}**'.format(self)

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()

        partial = functools.partial(cls.ytdl.extract_info, search, download=False, process=False)
        data = await loop.run_in_executor(None, partial)

        if data is None:
            raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        if 'entries' not in data:
            process_info = data
        else:
            process_info = None
            for entry in data['entries']:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        webpage_url = process_info['webpage_url']
        partial = functools.partial(cls.ytdl.extract_info, webpage_url, download=False)
        processed_info = await loop.run_in_executor(None, partial)

        if processed_info is None:
            raise YTDLError('Couldn\'t fetch `{}`'.format(webpage_url))

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    raise YTDLError('Couldn\'t retrieve any matches for `{}`'.format(webpage_url))

        return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} seconds'.format(seconds))

        return ', '.join(duration)


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        embed = (discord.Embed(title='Now playing',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=discord.Color.blurple())
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))

        return embed


class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def shuffle(self):
        random.shuffle(self._queue)

    def remove(self, index: int):
        del self._queue[index]


class VoiceState:
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        self.bot = bot
        self._ctx = ctx
        self.current = None
        self.voice = None
        self.next = asyncio.Event()
        self.songs = SongQueue()
        self._loop = False
        self._volume = 0.5
        self.skip_votes = set()
        self.audio_player = bot.loop.create_task(self.audio_player_task())

    def __del__(self):
        self.audio_player.cancel()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        self._loop = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def is_playing(self):
        return self.voice and self.current

    async def audio_player_task(self):
        while True:
            self.next.clear()

            if not self.loop:
                try:
                    async with timeout(180):  # 3 minutes
                        self.current = await self.songs.get()
                except asyncio.TimeoutError:
                    self.bot.loop.create_task(self.stop())
                    return

            self.current.source.volume = self._volume
            self.voice.play(self.current.source, after=self.play_next_song)
            await self.current.source.channel.send(embed=self.current.create_embed())

            await self.next.wait()

    def play_next_song(self, error=None):
        if error:
            raise VoiceError(str(error))

        self.next.set()

    def skip(self):
        self.skip_votes.clear()

        if self.is_playing:
            self.voice.stop()

    async def stop(self):
        self.songs.clear()

        if self.voice:
            await self.voice.disconnect()
            self.voice = None


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.bot, ctx)
            self.voice_states[ctx.guild.id] = state
        return state

    def cog_unload(self):
        for state in self.voice_states.values():
            self.bot.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')
        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))

    @commands.command(name='join', invoke_without_subcommand=True)
    async def _join(self, ctx: commands.Context):
        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='summon')
    @commands.has_permissions(manage_guild=True)
    async def _summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        if not channel and not ctx.author.voice:
            raise VoiceError('You are neither connected to a voice channel nor specified a channel to join.')
        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return
        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='leave', aliases=['disconnect'])
    @commands.has_permissions(manage_guild=True)
    async def _leave(self, ctx: commands.Context):
        if not ctx.voice_state.voice:
            return await ctx.send('Not connected to any voice channel.')
        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]

    @commands.command(name='volume')
    async def _volume(self, ctx: commands.Context, *, volume: int):
        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')
        if 0 > volume > 100:
            return await ctx.send('Volume must be between 0 and 100')
        ctx.voice_state.volume = volume / 100
        await ctx.send('Volume of the player set to {}%'.format(volume))

    @commands.command(name='now', aliases=['current', 'playing'])
    async def _now(self, ctx: commands.Context):
        await ctx.send(embed=ctx.voice_state.current.create_embed())

    @commands.command(name='pause')
    @commands.has_permissions(manage_guild=True)
    async def _pause(self, ctx: commands.Context):
        if not ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='resume')
    @commands.has_permissions(manage_guild=True)
    async def _resume(self, ctx: commands.Context):
        if not ctx.voice_state.is_playing and ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='stop')
    @commands.has_permissions(manage_guild=True)
    async def _stop(self, ctx: commands.Context):
        ctx.voice_state.songs.clear()
        if not ctx.voice_state.is_playing:
            ctx.voice_state.voice.stop()
            await ctx.message.add_reaction('⏹')

    @commands.command(name='skip')
    async def _skip(self, ctx: commands.Context):
        if not ctx.voice_state.is_playing:
            return await ctx.send('Not playing any music right now...')
        voter = ctx.message.author
        if voter == ctx.voice_state.current.requester:
            await ctx.message.add_reaction('⏭')
            ctx.voice_state.skip()
        elif voter.id not in ctx.voice_state.skip_votes:
            ctx.voice_state.skip_votes.add(voter.id)
            total_votes = len(ctx.voice_state.skip_votes)
            if total_votes >= 3:
                await ctx.message.add_reaction('⏭')
                ctx.voice_state.skip()
            else:
                await ctx.send('Skip vote added, currently at **{}/3**'.format(total_votes))
        else:
            await ctx.send('You have already voted to skip this song.')

    @commands.command(name='queue')
    async def _queue(self, ctx: commands.Context, *, page: int = 1):
        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')
        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.songs) / items_per_page)
        start = (page - 1) * items_per_page
        end = start + items_per_page
        queue = ''
        for i, song in enumerate(ctx.voice_state.songs[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)
        embed = (discord.Embed(description='**{} tracks:**\n\n{}'.format(len(ctx.voice_state.songs), queue))
                 .set_footer(text='Viewing page {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='shuffle')
    async def _shuffle(self, ctx: commands.Context):
        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')
        ctx.voice_state.songs.shuffle()
        await ctx.message.add_reaction('✅')

    @commands.command(name='remove')
    async def _remove(self, ctx: commands.Context, index: int):
        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')
        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('✅')

    @commands.command(name='loop')
    async def _loop(self, ctx: commands.Context):
        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')
        ctx.voice_state.loop = not ctx.voice_state.loop
        await ctx.message.add_reaction('✅')

    @commands.command(name='play')
    async def _play(self, ctx: commands.Context, *, search: str):
        if not ctx.voice_state.voice:
            await ctx.invoke(self._join)
        async with ctx.typing():
            try:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop)
            except YTDLError as e:
                await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
            else:
                song = Song(source)
                await ctx.voice_state.songs.put(song)
                await ctx.send('Enqueued {}'.format(str(source)))

    @_join.before_invoke
    @_play.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('You are not connected to any voice channel.')
        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError('Bot is already in a voice channel.')

class MainCog(commands.Cog):
    def __init__(self, client : commands.Bot):
        self.client = client

    def load(self):
        return

    def save(self):
        with open(f'{cwd}/database/users.json', 'w+') as f:
            json.dump(userdat, f)
        with open(f'{cwd}/database/guild.json', 'w+') as f:
            json.dump(gdata, f)

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

    def addv(self, dic, key, valarr):
        if key not in dic:
            dic[key] = list()
        dic[key].extend(valarr)

    def get_change(self, current, previous):
        if current == previous:
            return 100.0
        try:
            var = (abs(current - previous) / previous) * 100.0
            return 100.0 - var
        except ZeroDivisionError:
            return 0

    def gettime(self):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        return f"[{st}]"

    def log(self, *content, file="logs.txt", _print:bool=True):
        c = list(content)
        if _print:
            print(''.join(c))
        f = open(file, "a")
        f.write(f"{''.join(c)}\n")
        f.close()

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            to_append = list()
            for i in range(glen):
                to_append.append(0)
            if str(message.guild.id) not in gdata: self.addv(gdata, str(message.guild.id), list(to_append))
            to_append1 = list()
            for i in range(userlen):
                to_append1.append(0)
            if str(message.author.id) not in userdat:
                self.addv(userdat, str(message.author.id), list(to_append1))
                userdat[str(message.author.id)][16] = 1
            if userdat[str(message.author.id)][16] == 0: userdat[str(message.author.id)][16] = 1
            userdat[str(message.author.id)][4] += 1
            xpreq = 0
            if userdat[str(message.author.id)][5] == 1:
                xpreq = 25
            else:
                for level in range(int(userdat[str(message.author.id)][5])):
                    xpreq += 25
                    if xpreq >= 5000: break
            if int(userdat[str(message.author.id)][4]) >= xpreq:
                userdat[str(message.author.id)][4] -= userdat[str(message.author.id)][4]
                userdat[str(message.author.id)][5] += 1
                if gdata[str(message.guild.id)][1] == 0: await message.channel.send(f"{message.author.mention} You just leveled up to level **{userdat[str(message.author.id)][5]}**!")
                else:
                    channel = self.client.get_channel(int(gdata[str(message.author.id)][1]))
                    await channel.send(f"{message.author.mention} You just leveled up to level **{userdat[str(message.author.id)][5]}**!")
            xpreq = 0
            self.save()
            if gdata[str(message.guild.id)][0] == 0: pass
            else:
                if any(x in message.content.lower() for x in gdata[str(message.guild.id)][2]):
                    if message.channel.id == gdata[str(message.guild.id)][4]: pass
                    else:
                        await message.delete()
                        await message.channel.send(f"{message.author.mention} Watch your language")
                        userdat[str(message.author.id)][8] += 1
                        self.save()
            if gdata[str(message.guild.id)][3] == 0: pass
            else:
                if any(x in message.content.lower() for x in links):
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} No links")
                    userdat[str(message.author.id)][8] += 1
                    self.save()
            try:
                if int(gdata[str(message.guild.id)][6]) == 0:
                    gdata[str(message.guild.id)][6] = list()
                    gdata[str(message.guild.id)][6].append(0)
                    gdata[str(message.guild.id)][6].append(0)
                    self.save()
            except TypeError: pass
            if int(gdata[str(message.guild.id)][6][0]) == 0: pass
            else:
                try: channel = self.client.get_channel(int(gdata[str(message.guild.id)][6][0]))
                except: return
                channel = self.client.get_channel(int(gdata[str(message.guild.id)][6][0]))
                if message.channel == channel:
                    try:
                        int(message.content)
                    except ValueError:
                        return await message.delete()
                    var = int(message.content) - 1
                    if var == int(gdata[str(message.guild.id)][6][1]):
                        await message.add_reaction("✅")
                        gdata[str(message.guild.id)][6][1] += 1
                        self.save()
                    else:
                        await message.delete()
                        await message.channel.send(f"{message.author.mention} the next number is `{countconf[str(message.guild.id)][1] + 1}`", delete_after=5)
          
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def profile(self, ctx, user:discord.User=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if user == None: user = ctx.author
        win10v = userdat[str(user.id)][9] * 69420
        bcoinv = userdat[str(user.id)][10] * 50000
        scoinv = userdat[str(user.id)][11] * 250000
        gcoinv = userdat[str(user.id)][12] * 1000000
        dboxv = userdat[str(user.id)][15] * 69000000000000
        dailyboxv = userdat[str(user.id)][14] * 10000
        banknotev = userdat[str(user.id)][18] * 50000
        networth = userdat[str(user.id)][0] + userdat[str(user.id)][1] + win10v + bcoinv + scoinv + gcoinv + dboxv + dailyboxv
        embed = discord.Embed(title=f"{user}\'s profile", description=f"Networth: {networth}\nPrestige: {userdat[str(user.id)][16]}\nCommands used: {userdat[str(user.id)][17]}", color=discord.Color.random())
        #embed.set_thumbnail(user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def prestige(self, ctx, confirm=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        var = 0
        for i in range(int(userdat[str(ctx.message.author.id)][16])): var += 500000
        if confirm == None:
            var = 0
            for i in range(int(userdat[str(ctx.message.author.id)][16])): var += 500000
            embed = discord.Embed(title="prestige", description=f"Coins needed: `{userdat[str(ctx.message.author.id)][0]}/{var} {get_change(userdat[str(ctx.message.author.id)][0], var}`", color=discord.Color.random())
            await ctx.reply(embed=embed)
        elif confirm.lower() == "confirm":
            if int(userdat[str(ctx.message.author.id)][0]) >= var:
                    userdat[str(ctx.message.author.id)][16] += 1
                    for i in range(4): userdat[str(ctx.message.author.id)][i-1] = 0
                    v = 10
                    for i in range(7):
                        userdat[str(ctx.message.author.id)][v-1] = 0
                        i += 1
                    coins = 0
                    v = 1
                    for i in range(userdat[str(ctx.message.author.id)][16]): coins += 50000
                    userdat[str(ctx.message.author.id)][18] = 0
                    userdat[str(ctx.message.author.id)][0] += coins
                    self.save()
                    await ctx.reply(f"You are now prestige {userdat[str(ctx.message.author.id)][16]}!\nYou earned {coins} coins")
            else: return await ctx.reply("You don\'t have enough coins to prestige", mention_author=False)
        else:
            return await ctx.send(".")

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bannedwords(self, ctx, *wordlist:str):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if len(list(wordlist)) == 1 and wordlist[0] == "default":
            with open(f"{cwd}/database/default.json", "r") as f: words = json.load(f)
            gdata[str(ctx.guild.id)][2] = list()
            self.save()
            for key in words.keys(): gdata[str(ctx.guild.id)][2].append(key)
        else:
            gdata[str(ctx.guild.id)][2] = list()
            self.save()
            for word in wordlist: gdata[str(ctx.guild.id)][2].append(word)
        self.save()
        await ctx.reply("Updated banned word list")

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def welcomemsg(self, ctx, *, message:str):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        gdata[str(ctx.guild.id)][5] = message
        await ctx.reply("Updated the welcome message.")
        self.save()

    @commands.command(aliases=["vs"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def viewsettings(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        em = discord.Embed(description=f"Passive mode: {userdat[str(ctx.message.author.id)][6]}\nSwear filter: {swearfilter[str(ctx.message.guild.id)]}\nLink blocker: {link[str(ctx.message.guild.id)]}", color=discord.Colour.random())
        await ctx.reply(embed=em, mention_author=False)

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def linktoggle(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if gdata[str(ctx.guild.id)][3] == 0:
            await ctx.reply("Enabled link blocker.")
            gdata[str(ctx.guild.id)][3] = 1
            self.save()
        elif gdata[str(ctx.guild.id)][3] == 1:
            await ctx.reply("Disabled link blocker")
            gdata[str(ctx.guild.id)][3] = 0
            self.save()

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def shop(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        color = discord.Colour.random()
        page1 = discord.Embed(
            title=f"thatOneArchBot shop",
            description=f"Windows 10 key\nDescription: Windows 10 lisence key, too expensive for an os\nCost: 69420\nId: `windows10`\n\nBronze coin\nCost: 50000 coins\nId: `bronzecoin`\n\nSilver coin\nCost: 250000 coins\nId: `silvercoin`",
            color=color
        )
        page2 = discord.Embed(
            title=f"thatOneArchBot shop",
            description=f"Gold coin\nCost: 1000000 coins\nId: `goldcoin`\n\nDeveloper box\nCost: 69000000000000 coins\nId: `devbox`\n\nNormal box\nCost: 5000 coins\nId: `normalbox`\n\nBank note\nCost: 50000 coins\nId: `banknote`",
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

    @commands.command()
    async def cexec(self, ctx, *, body):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        if ctx.message.author.id not in ids: return
        if body.startswith("```c") and body.endswith("```"):
            body = body.replace("```c", "")
            body = body.replace("```", "")
        elif body.startswith("```") and body.endswith("```"):
            body = body.replace("```", "")
        def _cexec(code):
            oldstd = sys.stdout
            sys.stdout = open("out.txt", "w")
            Interpreter.run(code)
            sys.stdout.close()
            sys.stdout = oldstd
            with open("out.txt", "r") as f: data = f.read()
            return data
        await ctx.send(f"{_cexec(body)}")
  
    @commands.command(aliases=['inv'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def inventory(self, ctx, user : discord.User=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if user == None:
            em = discord.Embed(title=f"{ctx.message.author.display_name}'s inventory", description=f"Windows 10 keys: {userdat[str(ctx.message.author.id)][9]}\nBronze coins: {userdat[str(ctx.message.author.id)][10]}\nSilver coins: {userdat[str(ctx.message.author.id)][11]}\nGold coins: {userdat[str(ctx.message.author.id)][12]}\nDaily boxes: {userdat[str(ctx.message.author.id)][14]}\nDeveloper boxes: {userdat[str(ctx.message.author.id)][15]}\nNormal boxes: {userdat[str(ctx.message.author.id)][13]}", color=discord.Colour.random())
            await ctx.reply(embed=em, mention_author=False)
        else:
            to_append1 = list()
            for i in range(userlen):
                to_append1.append(0)
            if str(message.author.id) not in userdat: self.addv(userdat, str(message.author.id), list(to_append1))
            em = discord.Embed(title=f"{user.display_name}'s inventory", description=f"Windows 10 keys: {userdat[str(user.id)][9]}\nBronze coins: {userdat[str(user.id)][10]}\nSilver coins: {userdat[str(user.id)][11]}\nGold coins: {userdat[str(user.id)][12]}\nDaily boxes: {userdat[str(user.id)][14]}\nDeveloper boxes: {userdat[str(user.id)][15]}\nNormal boxes: {userdat[str(user.id)][13]}", color=discord.Colour.random())
            await ctx.reply(embed=em, mention_author=False)

    @commands.command()
    async def setbank(self, ctx, user:discord.User, amount):
        if ctx.message.author.id not in ids: return
        try: int(amount)
        except ValueError: await ctx.send(".")
        userdat[str(user.id)][19] = int(amount)
        self.save()
        await ctx.reply(".")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def use(self, ctx, item:str, amount:int=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if isinstance(amount, int):
            if int(amount) > 65535: return await ctx.reply("no more than unsigned int16 (65,535)")
        if str(item) == "developer" or str(item) == "devbox":
            if amount == None or int(amount) == 1:
                if int(userdat[str(ctx.message.author.id)][15]) < 1: return await ctx.reply("You don\'t own this item")
                else:
                    items = [
                        "coins",
                        "windows10",
                        "goldcoin"
                    ]
                    rnd = random.choice(items)
                    msg = await ctx.reply("Opening developer box...")
                    userdat[str(ctx.message.author.id)][3] += round(random.random(), 2)
                    async with ctx.typing():
                        await asyncio.sleep(2)
                    userdat[str(ctx.message.author.id)][15] -= 1
                    if rnd == "coins":
                        rand = ''.join(map(str, random.choices([1, 2], weights=[50, float(userdat[str(ctx.message.author.id)][3])], k=1)))
                        if rand == str(1): c = random.randint(100000, 69696969696969)
                        elif rand == str(2):
                            c = random.randint(69696969696969, 6969696969696969696969696969)
                            await msg.edit(content=f"You earned {c} coins from a developer box (RNG drop)")
                            userdat[str(ctx.message.author.id)][3] = 0
                            userdat[str(ctx.message.author.id)][0] += c
                            self.save()
                            return
                        userdat[str(ctx.message.author.id)][0] += c
                        await msg.edit(content=f"You earned {c} coins from a developer box!")
                        self.save()
                        return
                    elif rnd == "windows10":
                        w = random.randint(69, 69420)
                        userdat[str(ctx.message.author.id)][9] += w
                        await msg.edit(content=f"You earned {w} windows 10 keys from a developer box!")
                        self.save()
                        return
                    elif rnd == "goldcoin":
                        g = random.randint(6969, 6969420)
                        userdat[str(ctx.message.author.id)][12] += g
                        await msg.edit(content=f"You earned {g} golden coins from a developer box!")
                        self.save()
                        return
            elif int(amount) == 0: return await ctx.reply(f"Oppened 0 developer boxes and got......................\nNOTHING!!!")
            elif int(amount) < 0: return await ctx.reply("Don\'t try to break me")
            else:
                if int(userdat[str(ctx.message.author.id)][15]) < int(amount): return await ctx.reply("You don\'t have that many developer boxes")
                else:
                    rand = ''.join(map(str, random.choices([1, 2], weights=[50, float(userdat[str(ctx.message.author.id)][3])], k=1)))
                    items = [
                        "coins",
                        "windows10",
                        "goldcoin"
                    ]
                    c = 0
                    w = 0
                    g = 0
                    rng = 0
                    for i in range(int(amount)):
                        rnd = random.choice(items)
                        if rnd == "coins": c += 1
                        elif rnd == "windows10": w += 1
                        elif rnd == "goldcoin": g += 1
                        rng += 0.25
                    if c != 0:
                        if rand == str(2): coin0 = random.randint(69696969696969, 6969696969696969696969696969)
                        else: coin0 = random.randint(100000, 69696969696969)
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
                    userdat[str(ctx.message.author.id)][9] += int(win1)
                    userdat[str(ctx.message.author.id)][0] += int(coin1)
                    userdat[str(ctx.message.author.id)][12] += int(gold1)
                    userdat[str(ctx.message.author.id)][15] -= int(amount)
                    self.save()
                    embed = discord.Embed(description="You earned:", color=discord.Colour.random())
                    if rand == str(2):
                        if c != 0: embed.add_field(name="Coins (RNG)", value=str(coin1))
                        if rand == str(2): userdat[str(ctx.message.author.id)][3] = 0
                    else:
                        if c != 0: embed.add_field(name="Coins", value=str(coin1))
                        userdat[str(ctx.message.author.id)][3] += rng
                    self.save()
                    if w != 0: embed.add_field(name="Windows 10 keys", value=str(win1))
                    if g != 0: embed.add_field(name="Golden coins", value=str(gold1))
                    embed.set_footer(text=f"These rewards are from {amount} developer boxes")
                    return await msg.edit(embed=embed)
        elif str(item) == "daily" or str(item) == "dailybox":
            if amount == None or int(amount) == 1:
                if int(userdat[str(ctx.message.author.id)][14]) < 1: return await ctx.reply("You don\'t own this item")
                else:
                    items = [
                        "coins",
                        "windows10",
                        "bronzecoin",
                        "silvercoin",
                        "goldcoin"
                    ]
                    rnd = ''.join(map(str, random.choices(items, weights=[40, 5, 3, 1, 0.5], k=1)))
                    msg = await ctx.reply("Opening daily box...")
                    rand = ''.join(map(str, random.choices([1, 2], weights=[50, float(userdat[str(ctx.message.author.id)][3])], k=1)))
                    if rand == str(1): c = random.randint(1000, 100000)
                    elif rand == str(2):
                        c = random.randint(100000, 10000000000)
                        await msg.edit(content=f"You earned {c} coins from a daily box (RNG drop)")
                        userdat[str(ctx.message.author.id)][3] = 0
                        userdat[str(ctx.message.author.id)][0] += c
                        self.save()
                        return
                    userdat[str(ctx.message.author.id)][3] += round(random.random(), 2)
                    async with ctx.typing():
                        await asyncio.sleep(2)
                    userdat[str(ctx.message.author.id)][14] -= 1
                    if rnd == "coins":
                        c = random.randint(1000, 100000)
                        userdat[str(ctx.message.author.id)][0] += c
                        await msg.edit(content=f"You earned {c} coins from a daily box!")
                        self.save()
                        return
                    elif rnd == "windows10":
                        w = random.randint(1, 2)
                        userdat[str(ctx.message.author.id)][9] += w
                        await msg.edit(content=f"You earned {w} windows 10 keys from a daily box!")
                        self.save()
                        return
                    elif rnd == "bronzecoin":
                        b = random.randint(1, 2)
                        userdat[str(ctx.message.author.id)][10] += b
                        await msg.edit(content=f"You earned {b} bronze coins from a daily box!")
                        self.save()
                        return
                    elif rnd == "silvercoin":
                        s = random.randint(1, 2)
                        userdat[str(ctx.message.author.id)][11] += s
                        await msg.edit(content=f"You earned {s} silver coins from a daily box!")
                        self.save()
                        return
                    elif rnd == "goldcoin":
                        g = random.randint(1, 2)
                        userdat[str(ctx.message.author.id)][12] += g
                        await msg.edit(content=f"You earned {g} golden coins from a daily box!")
                        self.save()
                        return
            elif int(amount) == 0: return await ctx.reply(f"Oppened 0 daily boxes and got......................\nNOTHING!!!")
            elif int(amount) < 0: return await ctx.reply("Don\'t try to break me")
            else:
                if int(userdat[str(ctx.message.author.id)][14]) < int(amount): return await ctx.reply("You don\'t have that many daily boxes")
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
                    rng = 0
                    rand = ''.join(map(str, random.choices([1, 2], weights=[50, float(userdat[str(ctx.message.author.id)][3])], k=1)))
                    for i in range(int(amount)):
                        rnd = ''.join(map(str, random.choices(items, weights=[40, 5, 3, 1, 0.5], k=1)))
                        if rnd == "coins": c += 1
                        elif rnd == "windows10": w += 1
                        elif rnd == "goldcoin": g += 1
                        elif rnd == "silvercoin": s += 1
                        elif rnd == "bronzecoin": b += 1
                        rng += 0.25
                    if c != 0:
                        if rand == str(2): coin0 = random.randint(100000, 10000000000)
                        else: coin0 = random.randint(1000, 100000)
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
                    userdat[str(ctx.message.author.id)][9] += int(win1)
                    userdat[str(ctx.message.author.id)][0] += int(coin1)
                    userdat[str(ctx.message.author.id)][12] += int(gold1)
                    userdat[str(ctx.message.author.id)][14] -= int(amount)
                    self.save()
                    embed = discord.Embed(description="You earned:", color=discord.Colour.random())
                    if rand == str(1):
                        if c != 0: embed.add_field(name="Coins", value=str(coin1))
                        userdat[str(ctx.message.author.id)][3] += rng
                    else:
                        if c != 0: embed.add_field(name="Coins (RNG)", value=str(coin1))
                        userdat[str(ctx.message.author.id)][3] = 0
                    self.save()
                    if w != 0: embed.add_field(name="Windows 10 keys", value=str(win1))
                    if g != 0: embed.add_field(name="Golden coins", value=str(gold1))
                    embed.set_footer(text=f"These rewards are from {amount} daily boxes")
                    return await msg.edit(embed=embed)
        elif str(item) == "normal" or str(item) == "normalbox":
            if amount == None or int(amount) == 1:
                if int(userdat[str(ctx.message.author.id)][13]) < 1: return await ctx.reply("You don\'t own this item")
                else:
                    items = [
                        "coins",
                        "windows10",
                        "bronzecoin",
                        "silvercoin",
                        "goldcoin"
                    ]
                    rnd = ''.join(map(str, random.choices(items, weights=[40, 2.5, 1.5, 0.5, 0.01], k=1)))
                    msg = await ctx.reply("Opening normal box...")
                    rand = ''.join(map(str, random.choices([1, 2], weights=[50, float(userdat[str(ctx.message.author.id)][3])], k=1)))
                    if rand == str(1): c = random.randint(1000, 10000)
                    elif rand == str(2):
                        c = random.randint(10000, 10000000)
                        await msg.edit(content=f"You earned {c} coins from a normal box (RNG drop)")
                        userdat[str(ctx.message.author.id)][3] = 0
                        userdat[str(ctx.message.author.id)][0] += c
                        self.save()
                        return
                    userdat[str(ctx.message.author.id)][3] += round(random.random(), 2)
                    async with ctx.typing():
                        await asyncio.sleep(2)
                    userdat[str(ctx.message.author.id)][13] -= 1
                    if rnd == "coins":
                        c = random.randint(1000, 10000)
                        userdat[str(ctx.message.author.id)][0] += c
                        await msg.edit(content=f"You earned {c} coins from a normal box!")
                        self.save()
                        return
                    elif rnd == "windows10":
                        userdat[str(ctx.message.author.id)][9] += 1
                        await msg.edit(content=f"You earned 1 windows 10 key from a normal box!")
                        self.save()
                        return
                    elif rnd == "bronzecoin":
                        userdat[str(ctx.message.author.id)][10] += 1
                        await msg.edit(content=f"You earned 1 bronze coin from a daily box!")
                        self.save()
                        return
                    elif rnd == "silvercoin":
                        userdat[str(ctx.message.author.id)][11] += 1
                        await msg.edit(content=f"You earned silver coin from a daily box!")
                        self.save()
                        return
                    elif rnd == "goldcoin":
                        userdat[str(ctx.message.author.id)][12] += 1
                        await msg.edit(content=f"You earned golden coin from a daily box!")
                        self.save()
                        return
            elif int(amount) == 0: return await ctx.reply(f"Oppened 0 normal boxes and got......................\nNOTHING!!!")
            elif int(amount) < 0: return await ctx.reply("Don\'t try to break me")
            else:
                if int(userdat[str(ctx.message.author.id)][13]) < int(amount): return await ctx.reply("You don\'t have that many normal boxes")
                elif int(userdat[str(ctx.message.author.id)][13]) == 0: return await ctx.reply("You don\'t own this item")
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
                    rng = 0
                    rand = ''.join(map(str, random.choices([1, 2], weights=[50, float(userdat[str(ctx.message.author.id)][3])], k=1)))
                    for i in range(int(amount)):
                        rnd = ''.join(map(str, random.choices(items, weights=[40, 2.5, 1.5, 0.5, 0.01], k=1)))
                        if rnd == "coins": c += 1
                        elif rnd == "windows10": w += 1
                        elif rnd == "goldcoin": g += 1
                        elif rnd == "silvercoin": s += 1
                        elif rnd == "bronzecoin": b += 1
                        rng += 0.05
                    if c != 0:
                        if rand == str(2): coin0 = random.randint(10000, 10000000)
                        else: coin0 = random.randint(1000, 10000)
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
                    userdat[str(ctx.message.author.id)][9] += int(win1)
                    userdat[str(ctx.message.author.id)][0] += int(coin1)
                    userdat[str(ctx.message.author.id)][12] += int(gold1)
                    userdat[str(ctx.message.author.id)][13] -= int(amount)
                    self.save()
                    embed = discord.Embed(description="You earned:", color=discord.Colour.random())
                    if rand == str(2):
                        if c != 0: embed.add_field(name="Coins (RNG)", value=str(coin1))
                        userdat[str(ctx.message.author.id)][3] = 0
                    else:
                        if c != 0: embed.add_field(name="Coins", value=str(coin1))
                        userdat[str(ctx.message.author.id)][3] += rng
                    self.save()
                    if w != 0: embed.add_field(name="Windows 10 keys", value=str(win1))
                    if g != 0: embed.add_field(name="Golden coins", value=str(gold1))
                    embed.set_footer(text=f"These rewards are from {amount} normal boxes")
                    return await msg.edit(embed=embed)
        elif str(item) == "banknote":
            if amount == None or int(amount) == 1:
                if userdat[str(ctx.message.author.id)][18] <= 0: return await ctx.send("You don't own this item")
                userdat[str(ctx.message.author.id)][18] -= 1
                space = random.randint(20000, 100000)
                userdat[str(ctx.message.author.id)][19] += space
                self.save()
                return await ctx.send(f"You used 1 bank note and increased the bank space by {space} coins")
            else:
                if userdat[str(ctx.message.author.id)] < int(amount) or int(amount) <= 0: return await ctx.send("dont try to break me dood")
                space = 0
                for i in range(int(amount)):
                    space += random.randint(20000, 100000)
                userdat[str(ctx.message.author.id)][18] -= int(amount)
                userdat[str(ctx.message.author.id)][19] += space
                self.save()
                return await ctx.send(f"You used {amount} bank note and increased the bank space by {space} coins")
        else: return await ctx.reply(f"No such item: {item}")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def add_item(self, ctx, user : discord.User, item:str, amount:int=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if ctx.message.author.id not in ids:
            await ctx.reply("You cant use this")
            return
        else:
            if str(user.id) not in userdat:
                to_append1 = list()
                for i in range(userlen):
                    to_append1.append(0)
                self.addv(userdat, str(user.id), list(to_append1))
                self.save()
            if str(item) == "windows10":
                if amount == None or int(amount) == 1:
                    userdat[str(user.id)][9] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `windows10` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    userdat[str(user.id)][9] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} windows 10 keys to {user.display_name}")
                    return
            elif str(item) == "normalbox":
                if amount == None or int(amount) == 1:
                    userdat[str(user.id)][13] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `normalbox` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    userdat[str(user.id)][13] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} normal boxes to {user.display_name}")
                    return
            elif str(item) == "bronzecoin":
                if amount == None or int(amount) == 1:
                    userdat[str(user.id)][10] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `bronzecoin` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    userdat[str(user.id)][10] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} bronze coins to {user.display_name}")
                    return
            elif str(item) == "silvercoin":
                if amount == None or int(amount) == 1:
                    userdat[str(user.id)][11] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `silvercoin` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    userdat[str(user.id)][11] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} silver coins to {user.display_name}")
                    return
            elif str(item) == "goldcoin":
                if amount == None or int(amount) == 1:
                    userdat[str(user.id)][12] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `goldcoin` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    userdat[str(user.id)][12] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} gold coins to {user.display_name}")
                    return
            elif str(item) == "devbox":
                if amount == None or int(amount) == 1:
                    userdat[str(user.id)][15] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `developer box` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    userdat[str(user.id)][15] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} developer boxes to {user.display_name}")
                    return
            elif str(item) == "dailybox":
                if amount == None or int(amount) == 1:
                    userdat[str(user.id)][14] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `daily box` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    userdat[str(user.id)][14] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} daily boxes to {user.display_name}")
                    return
            elif str(item) == "banknote":
                if amount == None or int(amount) == 1:
                    userdat[str(user.id)][18] += 1
                    self.save()
                    await ctx.reply(f"Added 1 `banknote` to {user.display_name}", mention_author=False)
                    return
                elif int(amount) == 0:
                    await ctx.reply(f"You don\'t need to run the command to give 0 items", mention_author=False)
                    return
                else:
                    userdat[str(user.id)][18] += int(amount)
                    self.save()
                    await ctx.reply(f"Added {amount} bank notes to {user.display_name}")
                    return
            elif str(item) == "all":
                if amount == None or int(amount) == 1:
                    userdat[str(user.id)][9] += 1
                    userdat[str(user.id)][10] += 1
                    userdat[str(user.id)][11] += 1
                    userdat[str(user.id)][12] += 1
                    userdat[str(user.id)][15] += 1
                    userdat[str(user.id)][14] += 1
                    userdat[str(user.id)][13] += 1
                    userdat[str(user.id)][18] += 1
                    self.save()
                    await ctx.reply(f"Added all items once in {user.display_name}\'s profile", mention_author=False)
                    return
                else:
                    userdat[str(user.id)][9] += int(amount)
                    userdat[str(user.id)][10] += int(amount)
                    userdat[str(user.id)][11] += int(amount)
                    userdat[str(user.id)][12] += int(amount)
                    userdat[str(user.id)][15] += int(amount)
                    userdat[str(user.id)][14] += int(amount)
                    userdat[str(user.id)][13] += int(amount)
                    userdat[str(user.id)][18] += int(amount)
                    self.save()
                    await ctx.reply(f"Added all items {amount} times in {user.display_name}\'s profile", mention_author=False)
                    return
            else:
                await ctx.reply("No such item")

    @commands.command()
    @commands.has_role("Giveaways")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def giveaway(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def reroll(self, ctx, channel: discord.TextChannel, id_: int):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poll(self, ctx, question, *options: str):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def buy(self, ctx, item:str, amount:int=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if str(item) == "windows10":
            if amount == None or int(amount) == 1:
                if userdat[str(ctx.message.author.id)][0] < 69420:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {round(69420 - userdat[str(ctx.message.author.id)][0])} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a windows 10 key! Now you have {round(userdat[str(ctx.message.author.id)][0] - 69420)} coins in your wallet.", mention_author=False)
                    userdat[str(ctx.message.author.id)][0] -= 69420
                    userdat[str(ctx.message.author.id)][9] += 1
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
                if userdat[str(ctx.message.author.id)][0] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - userdat[str(ctx.message.author.id)][0]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} windows 10 keys for {a} coins. Now you have {userdat[str(ctx.message.author.id)][0] - a} coins in your wallet")
                    userdat[str(ctx.message.author.id)][0] -= a
                    userdat[str(ctx.message.author.id)][9] += amount
                    self.save()
                    return
        elif str(item) == "bronzecoin":
            if amount == None or int(amount) == 1:
                if userdat[str(ctx.message.author.id)][0] < 50000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {50000 - userdat[str(ctx.message.author.id)][0]} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a bronze coin! Now you have {userdat[str(ctx.message.author.id)][0] - 50000} coins in your wallet.", mention_author=False)
                    userdat[str(ctx.message.author.id)][0] -= 50000
                    userdat[str(ctx.message.author.id)][10] += 1
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
                if userdat[str(ctx.message.author.id)][0] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - userdat[str(ctx.message.author.id)][0]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} bronze coins for {a} coins. Now you have {userdat[str(ctx.message.author.id)][0] - a} coins in your wallet")
                    userdat[str(ctx.message.author.id)][0] -= a
                    userdat[str(ctx.message.author.id)][10] += amount
                    self.save()
                    return
        elif str(item) == "silvercoin":
            if amount == None or int(amount) == 1:
                if userdat[str(ctx.message.author.id)][0] < 250000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {250000 - userdat[str(ctx.message.author.id)][0]} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a silver coin! Now you have {userdat[str(ctx.message.author.id)][0] - 250000} coins in your wallet.", mention_author=False)
                    userdat[str(ctx.message.author.id)][0] -= 250000
                    userdat[str(ctx.message.author.id)][10] += 1
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
                if userdat[str(ctx.message.author.id)][0] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - userdat[str(ctx.message.author.id)][0]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} silver coins for {a} coins. Now you have {userdat[str(ctx.message.author.id)][0] - a} coins in your wallet")
                    userdat[str(ctx.message.author.id)][0] -= a
                    userdat[str(ctx.message.author.id)][11] += amount
                    self.save()
                    return
        elif str(item) == "goldcoin":
            if amount == None or int(amount) == 1:
                if userdat[str(ctx.message.author.id)][0] < 1000000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {1000000 - userdat[str(ctx.message.author.id)][0]} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought gold coin! Now you have {userdat[str(ctx.message.author.id)][0] - 1000000} coins in your wallet.", mention_author=False)
                    userdat[str(ctx.message.author.id)][0] -= 1000000
                    userdat[str(ctx.message.author.id)][12] += 1
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
                if userdat[str(ctx.message.author.id)][0] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - userdat[str(ctx.message.author.id)][0]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} gold coins for {a} coins. Now you have {userdat[str(ctx.message.author.id)][0] - a} coins in your wallet")
                    userdat[str(ctx.message.author.id)][0] -= a
                    userdat[str(ctx.message.author.id)][12] += amount
                    self.save()
                    return
        elif str(item) == "devbox":
            if amount == None or int(amount) == 1:
                if userdat[str(ctx.message.author.id)][0] < 69000000000000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {69000000000000 - userdat[str(ctx.message.author.id)][0]} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought gold coin! Now you have {userdat[str(ctx.message.author.id)][0] - 69000000000000} coins in your wallet.", mention_author=False)
                    userdat[str(ctx.message.author.id)][0] -= 69000000000000
                    userdat[str(ctx.message.author.id)][15] += 1
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
                if userdat[str(ctx.message.author.id)][0] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - userdat[str(ctx.message.author.id)][0]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} developer boxes for {a} coins. Now you have {userdat[str(ctx.message.author.id)][0] - a} coins in your wallet")
                    userdat[str(ctx.message.author.id)][0] -= a
                    userdat[str(ctx.message.author.id)][15] += amount
                    self.save()
                    return
        elif str(item) == "normalbox":
            if amount == None or int(amount) == 1:
                if userdat[str(ctx.message.author.id)][0] < 5000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {round(5000 - userdat[str(ctx.message.author.id)][0])} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a normal box! Now you have {round(userdat[str(ctx.message.author.id)][0] - 5000)} coins in your wallet.", mention_author=False)
                    userdat[str(ctx.message.author.id)][0] -= 5000
                    userdat[str(ctx.message.author.id)][13] += 1
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
                if userdat[str(ctx.message.author.id)][0] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - userdat[str(ctx.message.author.id)][0]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} normal boxes for {a} coins. Now you have {userdat[str(ctx.message.author.id)][0] - a} coins in your wallet")
                    userdat[str(ctx.message.author.id)][0] -= a
                    userdat[str(ctx.message.author.id)][13] += amount
                    self.save()
                    return
        elif str(item) == "banknote":
            if amount == None or int(amount) == 1:
                if userdat[str(ctx.message.author.id)][0] < 50000:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {round(50000 - userdat[str(ctx.message.author.id)][0])} more coins to buy this.", mention_author=False)
                    return
                else:
                    await ctx.reply(f"You bought a bank note! Now you have {round(userdat[str(ctx.message.author.id)][0] - 69420)} coins in your wallet.", mention_author=False)
                    userdat[str(ctx.message.author.id)][0] -= 50000
                    userdat[str(ctx.message.author.id)][18] += 1
                    self.save()
                    return
            elif int(amount) < 0:
                await ctx.reply("Don\'t try to break me **dood**")
                return
            elif int(amount) == 0:
                await ctx.reply("Here you go, 0 bank notes for 0 coins!")
                return
            else:
                a = 50000 * amount
                if userdat[str(ctx.message.author.id)][0] < a:
                    await ctx.reply(f"You don\'t have enough coins to buy this. You need {a - userdat[str(ctx.message.author.id)][0]} more coins")
                    return
                else:
                    await ctx.reply(f"You bought {amount} bank notes for {a} coins. Now you have {userdat[str(ctx.message.author.id)][0] - a} coins in your wallet")
                    userdat[str(ctx.message.author.id)][0] -= a
                    userdat[str(ctx.message.author.id)][13] += amount
                    self.save()
                    return
        else:
            await ctx.reply(f"No item {item} found. Type `.shop` to get the list of items")
            return

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def translate(self, ctx, target:str, *, text:str):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        try:
            t = translate.Translator(to_lang=target)
            tr = t.translate(text)
            if "is an invalid target language" not in tr.lower():
                em = discord.Embed(
                    description=f"Translation of {text} to {target}\n\n{tr}",
                    color=discord.Color.random()
                )
                return await ctx.reply(embed=em)
            else:
                return await ctx.reply(f"{target} is an invalid language")
        except Exception as e:
            return await ctx.reply(e)

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def config(self, ctx, setting:str=None, value:str=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        gid = str(ctx.guild.id)
        gname = self.client.get_guild(ctx.guild.id)
        if value == None:
            if setting == None:
                if gdata[gid][0] == 0:
                    swear = "disabled"
                else:
                    swear = "enabled"
                try:
                    if gdata[gid][6][0] == 0:
                        c = None
                    else:
                        v = self.client.get_channel(gdata[gid][6][0])
                        c = f"#{v}"
                except KeyError:
                    c = None
                if gdata[gid][3] == 0:
                    lnk = "disabled"
                else:
                    lnk = "enabled"
                em = discord.Embed(
                    title=f"{gname} config",
                    color=discord.Colour.random()
                )
                em.add_field(name="Swear filter", value=swear)
                em.add_field(name="Link blocker", value=lnk)
                if gdata[gid][5] == 0: pass
                else: em.add_field(name=f"Welcome message", value=gdata[gid][5])
                if gdata[gid][1] == 0:
                    pass
                else:
                    channel = int(gdata[gid][1])
                    cname = self.client.get_channel(channel)
                    em.add_field(name="Level up channel", value=f"#{cname}")
                if gdata[gid][4] == 0:
                    pass
                else:
                    channel = int(gdata[gid][4])
                    cname = self.client.get_channel(channel)
                    em.add_field(name="Whitelisted channel", value=f"#{cname}")
                if c == None:
                    pass
                else:
                    em.add_field(name="Counting channel", value=c)
                await ctx.send(embed=em)
            else:
                if str(setting) == "swearfilter":
                    if gdata[gid][0] == 0:
                        swear = "disabled"
                    else:
                        swear = "enabled"
                    self.save()
                    em = discord.Embed(
                        title=f"Swear filter status for {gname}",
                        description=f"status: {swear}",
                        color=discord.Colour.random()
                    )
                    await ctx.reply(embed=em)
                elif str(setting) == "bannedwords":
                    arr = ''.join(gdata[gid][2])
                    em = discord.Embed(
                        title=f"Banned words list for {gname}",
                        description=f"words: {arr}",
                        color=discord.Colour.random()
                    )
                    await ctx.reply(embed=em)
                elif str(setting) == "linkblocker":
                    if gdata[gid][3] == 0:
                        lnk = "disabled"
                    else:
                        lnk = "enabled"
                    em = discord.Embed(
                        title=f"Link blocker status for {gname}",
                        description=f"status: {lnk}",
                        color=discord.Colour.random()
                    )
                    await ctx.reply(embed=em)
                elif str(setting) == "levelupchannel":
                    if gdata[gid][1] != 0:
                        channel = gdata[gid][1]
                        cid = self.client.get_channel(channel)
                        pass
                    else:
                        await ctx.reply("This server doesn\'t have a level up channel")
                        return
                    em = discord.Embed(
                        title=f"Level up channel for {gname}",
                        description=f"channel: {cid}",
                        color=discord.Colour.random()
                    )
                    await ctx.reply(embed=em)
                elif str(setting) == "whitelist":
                    if gdata[gid][4] != 0:
                        channel = gdata[gid][4]
                        cid = self.client.get_channel(channel)
                        pass
                    else:
                        await ctx.reply("This server doesn\'t have a whitelisted channel")
                        return
                    em = discord.Embed(
                        title=f"Whitelisted for {gname}",
                        description=f"channel: {cid}",
                        color=discord.Colour.random()
                    )
                    await ctx.reply(embed=em)
                elif str(setting) == "counting":
                    if gdata[gid][6][0] != 0:
                        channel = gdata[gid][6][0]
                        cname = self.client.get_channel(channel)
                        pass
                    else:
                        await ctx.reply("This server doesn\'t have a counting channel")
                        return
                    em = discord.Embed(
                        title=f"Counting channel for {gname}",
                        description=f"#{cname}",
                        color=discord.Color.random()
                    )
                    await ctx.reply(embed=em)
                else:
                    await ctx.reply("Invalid setting")
                    return
        else:
            try:
                int(value)
            except Exception as e:
                return await ctx.reply(e)
            if str(setting) == "swearfilter":
                arr = [0, 1]
                if int(value) not in arr:
                    return await ctx.reply("Invalid value. Use:\n1 to enable\n0 to disable")
                if int(value) == 0:
                    gdata[gid][0] = 0
                    self.save()
                    return await ctx.reply(f"Disabled swear filter")
                else:
                    gdata[gid][0] = 1
                    self.save()
                    return await ctx.reply("Enabled swear filter")
            elif str(setting) == "linkblocker":
                arr = [0, 1]
                if int(value) not in arr:
                    return await ctx.reply("Invalid value. Use:\n1 to enable\n0 to disable")
                if int(value) == 0:
                    gdata[gid][3] = 0
                    self.save()
                    return await ctx.reply(f"Disabled link blocker")
                else:
                    gdata[gid][3] = 1
                    self.save()
                    return await ctx.reply("Enabled link blocker")
            elif str(setting) == "levelupchannel":
                if int(value) == 0:
                    gdata[gid][1] = 0
                    self.save()
                    return await ctx.reply("Level up channel has been reset")
                else:
                    try:
                        channel = self.client.get_channel(int(value))
                    except Exception as e:
                        return await ctx.reply(e)
                    gdata[gid][1] = int(value)
                    self.save()
                    return await ctx.reply(f"Set {channel} as level up messages channel")
            elif str(setting) == "whitelist":
                if int(value) == 0:
                    gdata[gid][4] = 0
                    self.save()
                    return await ctx.reply("Removed the whitelisted channel")
                else:
                    try:
                        channel = self.client.get_channel(int(value))
                    except Exception as e:
                        return await ctx.reply(e)
                    gdata[gid][4] = int(value)
                    self.save()
                    return await ctx.reply(f"Set {channel} as swear filter whitelisted channel")
            elif str(setting) == "bannedwords":
                with open(f"{cwd}/database/prefixes.json", "r") as f:
                    prefixes = json.load(f)
                return await ctx.reply(f"Use `{prefixes[gid]}help bannedwords`")
            elif str(setting) == "welcome" or str(setting) == "welcomemsg":
                with open(f"{cwd}/database/prefixes.json", "r") as f:
                    prefixes = json.load(f)
                return await ctx.reply(f"Use `{prefixes[gid]}help welcomemsg`")
            elif str(setting) == "counting" or str(setting) == "countchannel":
                try:
                    channel = self.client.get_channel(int(value))
                except Exception as e:
                    return await ctx.reply(e)
                gdata[gid][6][0] = int(value)
                self.save()
                return await ctx.reply(f"Set {channel} as counting channel")
            else:
                return await ctx.reply(f"Invalid setting: {setting}")

    @commands.command(aliases=["levelup"])
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def levelupchannel(self, ctx, channel:discord.TextChannel):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        lvlupc[str(ctx.guild.id)] = channel.id
        self.save()
        await ctx.reply(f"Updated level up channel")

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def whitelist(self, ctx, channel:discord.TextChannel):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        gdata[str(ctx.guild.id)][4] = channel.id
        self.save()
        await ctx.reply(f"Updated swear filter whitelisted channel")

    @commands.command(aliases=['goldfish'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fstab(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        await ctx.reply('https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg')

    @commands.command(aliases=['xp'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rank(self, ctx, user : discord.User=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if user == None:
            xpreq = 0
            if userdat[str(ctx.message.author.id)][5] == 0:
                xpreq = 25
            else:
                for level in range(int(userdat[str(ctx.message.author.id)][5])):
                    xpreq += 25
                    if xpreq >= 5000:
                        break
                    else:
                        pass
            embed = discord.Embed(title=f"{ctx.message.author.display_name}'s Rank", color=discord.Colour.random())
            embed.add_field(name="Level", value=str(userdat[str(ctx.message.author.id)][5]))
            xpv = f"{userdat[str(ctx.message.author.id)][4]}/{xpreq}"
            embed.add_field(name="Exp", value=str(xpv))
            embed.set_footer(text=f'Leveling api made by {owner}')
            await ctx.send(embed=embed)
        else:
            xpreq = 0
            if userdat[str(user.id)][5] == 1:
                xpreq = 25
            else:
                for level in range(int(userdat[str(user.id)][5])):
                    xpreq += 25
                    if xpreq >= 5000:
                        break
                    else:
                        pass
            embed = discord.Embed(title=f"{user.display_name}'s Rank", color=0xff0000)
            embed.add_field(name="Level", value=str(userdat[str(user.id)][5]))
            xpv = f"{userdat[str(user.id)][4]}/{xpreq}"
            embed.add_field(name="Exp", value=str(xpv))
            embed.set_footer(text=f'Leveling api made by {owner}')
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def add_xp(self, ctx, user : discord.User, amount:str):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if ctx.message.author.id not in ids:
            await ctx.reply(f'101% sure that this command doesn\'t exist :eyes:')
        else:
            try:
                int(amount)
            except Exception as e:
                return await ctx.reply(e)
            if str(user.id) not in userdat:
                to_append1 = list()
                for i in range(userlen):
                    to_append1.append(0)
                self.addv(userdat, str(user.id), list(to_append1))
                self.save()
            userdat[str(user.id)][4] += int(amount)
            self.save()
            await ctx.reply(f'Added {amount} xp to {user.display_name}')

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def passive(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if userdat[str(ctx.message.author.id)][6] == 1:
            userdat[str(ctx.message.author.id)][6] = 0
            self.save()
            await ctx.reply(f"Disabled passive mode")
        else:
            userdat[str(ctx.message.author.id)][6] = 1
            self.save()
            await ctx.reply(f"Enabled passive mode")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def add_lvl(self, ctx, user : discord.User, *, arg1):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if ctx.message.author.id not in ids:
            pass
        else:
            if arg1.isdigit:
                if str(user.id) not in userdat:
                    to_append1 = list()
                    for i in range(userlen):
                        to_append1.append(0)
                    self.addv(userdat, str(user.id), list(to_append1))
                    self.save()
                userdat[str(user.id)][5] += int(arg1)
                self.save()
                await ctx.reply(f"Added {int(arg1)} levels to {user.display_name}")
            else:
                await ctx.reply(f'{arg1} is not a number')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invite(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        await ctx.send("https://top.gg/bot/859869941535997972")

    blSay = True
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def say(self, ctx, *, text):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        await ctx.message.delete()
        r = 0
        for i in range(len(text)):
            r += 0.1
        async with ctx.typing():
            await asyncio.sleep(r)
        await ctx.send(f'{text}')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def uptime(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        await ctx.send(uptime)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        await ctx.send(f'Pong! My ping is {round(self.client.latency * 1000)}ms')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx, *, arg1=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if arg1 == None:
            em = discord.Embed(title='**COMMAND LIST**', description='Economy\nbeg, balance, daily, weekly, monthly, postmeme, work, guess, give, deposit, withdraw, shop, buy, inventory, passive, highlow, rob, invest, use, trivia\n\nModeration\nban, kick, purge, nuke, snipe, warns, config, edit_snipe, warn, bannedwords, welcomemsg\n\nMisc\nmeme, linuxmeme, softwaregore, ihadastroke, windowsmeme, stroke, say, rank, isSus, kill, slap, 8ball, credits, giveaway, reroll, poll, prefix\n\nMusic\nsummon, play, leave, queue, join, volume, now, pause, resume, stop, skip, remove, loop', color=discord.Colour.random())
            em.set_footer(text=f'type .help [command] to get more info about a command')
            return await ctx.reply(embed=em)
        elif arg1 == 'beg': em = discord.Embed(title='\'Beg\' command use', description='Gives an amount of coins to the user.\nCooldown: 30 seconds\nUsage: `.beg`', color=discord.Colour.random())
        elif arg1 == 'balance' or arg1 == 'bal': em = discord.Embed(title='\'Balance\' command use', description='Shows the amount of a user\nAliases: bal\nUsage `.balance|.bal` [@user]', color=discord.Colour.random())
        elif arg1 == 'hunt': em = discord.Embed(title='\'Hunt\' command use', description='Goes for hunting to get money\nCooldown: 30 seconds\nUsage: `.hunt`', color=discord.Colour.random())
        elif arg1 == 'daily': em = discord.Embed(title='\'Daily\' command use', description='Gives an amount of coins\nCooldown: 1 day\nUsage: `.daily`', color=discord.Colour.random())
        elif arg1 == 'weekly': em = discord.Embed(title='\'Weekly\' command use', description='Gives an amount of coins\nCooldown: 1 week\nUsage: `.weekly`', color=discord.Colour.random())
        elif arg1 == 'monthly': em = discord.Embed(title='\'Monthly\' command use', description='Gives an amount of coins\nCooldown: 1 month\nUsage: `.monthly`', color=discord.Colour.random())
        elif arg1 == 'postmeme' or arg1 == 'pm': em = discord.Embed(title='\'Post meme\' command use', description='Posts a meme and gets money\nCooldown: 40 seconds\nUsage: `.postmeme|.pm`', color=discord.Colour.random())
        elif arg1 == 'ban': em = discord.Embed(title='\'Ban\' command use', description='Bans a user from the server\nUsage: `.ban <@user>`\nPermissions needed: ban members', color=discord.Colour.random())
        elif arg1 == 'kick': em = discord.Embed(title='\'Kick\' command use', description='Kicks a user from the server\nUsage: `.kick <@user>`\nPermissions needed: kick members', color=discord.Colour.random())
        elif arg1 == 'nuke': em = discord.Embed(title='\'Nuke\' command use', description='Deletes all the messages from a channel\nUsage: `.nuke <#channel>`\nPermissions needed: manage channels', color=discord.Colour.random())
        elif arg1 == 'purge': em = discord.Embed(title='\'Purge\' command use', description='Deletes an amount of messages in the channel\nUsage: `.purge <amount>`\nPermissions needed: manage messages or manage channels')
        elif arg1 == '8ball': em = discord.Embed(title='\'8ball\' command use', description='Asks a qustion to the bot and responds with a random answer\nUsage: `.8ball <question>', color=discord.Colour.random())
        elif arg1 == 'meme': em = discord.Embed(title='\'Meme\' command use', description='Sends a random meme from r/memes\nUsage: `.meme`', color=discord.Colour.random())
        elif arg1 == 'ihadastroke': em = discord.Embed(title='\'Ihadastroke\' command use', description='Sends a random image from r/ihadastroke\nUsage: `.ihadastroke`', color=discord.Colour.random())
        elif arg1 == 'softwaregore' or arg1 == 'sg': em = discord.Embed(title='\'Softwaregore\' command use', description='Sends a random image from r/softwaregore\nUsage: `.softwaregore|.sg`', color=discord.Colour.random())
        elif arg1 == 'linuxmeme' or arg1 == 'lm': em = discord.Embed(title='\'Linuxmeme\' command use', description='Sends a random meme from r/linuxmemes\nUsage: `.linuxmeme|.lm`', color=discord.Colour.random())
        elif arg1 == 'work': em = discord.Embed(title='\'Work\' command use', description='Gets a big amount of money\nCooldown: 1 hour (except `.work list`)\nUsage: `.work [list/resign/job_id]`', color=discord.Colour.random())
        elif arg1 == 'stroke': em = discord.Embed(title='\'Stroke\' command use', description='Sends a stroke (not irl stroke)\nUsage: `.stroke <amount>`\nAmount limit: 750', color=discord.Colour.random())
        elif arg1 == 'invites': em = discord.Embed(title='\'Invites\' command use', description='Shows the amount of people the user invited\nUsage: `.invites [user]`', color=discord.Colour.random())
        elif arg1 == 'snipe': em = discord.Embed(title='\'Snipe\' command use', description='Shows the last deleted message in the channel\nUsage: `.snipe`', color=discord.Colour.random())
        elif arg1 == 'edit_snipe' or arg1 == 'edit-snipe' or arg1 == 'edit': em = discord.Embed(title='\'Edit snipe\' command use', description='Shows the last edited message in the channel\nUsage: `.edit_snipe|.edit`\nAvailability: beta only', color=discord.Colour.random())
        elif arg1 == 'highlow' or arg1 == 'hl': em = discord.Embed(title='\'Highlow\' command use', description='The bot generates 2 random numbers. The first one doesn\'t send it and the second one does. You have to guess if the hidden number is lower, higher or equal to the sent one\nCooldown: 40 seconds\nUsage: `.highlow|.hl`\nResponses: higher, lower, jackpot', color=discord.Colour.random())
        elif arg1 == 'kill': em = discord.Embed(title='\'Kill\' command use', description='*kills* a user\nUsage: `.kill <@user>`', color=discord.Colour.random())
        elif arg1 == 'fstab' or arg1 == 'fstab.goldfish': em = discord.Embed(title='\'Fstab\' command use', description='Sends the meme fstab.goldfish\nUsage: `.fstab`', color=discord.Colour.random())
        elif arg1 == 'slap': em = discord.Embed(title='\'Slap\' command use', description='*slaps* a user\nUsage: `.slap <@user>', color=discord.Colour.random())
        elif arg1 == 'guess': em = discord.Embed(title='\'Guess\' command use', description='You have to gues a number from 1 to 10. If you find it you get some coins\nCooldown: 30 seconds\nUsage: `.guess <number>`', color=discord.Colour.random())
        elif arg1 == 'give' or arg1 == 'gift': em = discord.Embed(title='\'Give\' command use', description='Gives coins to a user mentioned\nUsage: `.give|.gift <@user> <amount> [item]', color=discord.Colour.random())
        elif arg1 == 'isSus' or arg1 == 'sus': em = discord.Embed(title='\'Sus\' command use', description='Checks if a user is sus\nUsage: `.isSus|.sus <@user>`', color=discord.Colour.random())
        elif arg1 == 'add': em = discord.Embed(title='\'Add\' command use', description='Adds coins to a user\nAvailability: __developer only__\nUsage: `.add <@user> <amount:int/hex/bin>`', color=discord.Colour.random())
        elif arg1 == 'add_xp': em = discord.Embed(title='\'Add xp\' command use', description='Adds xp to a user\nAvailability: __developer only__\nUsage: `.add_xp <@user> <amount:int/hex/bin>`', color=discord.Colour.random())
        elif arg1 == 'add_lvl': em = discord.Embed(title='\'Add levels\' command use', description='Adds levels to a user\nAvailability: __developer only__\nUsage: `.add_lvl <@user> <amount:int/hex/bin>', color=discord.Colour.random())
        elif arg1 == 'fish': em = discord.Embed(title='\'Fish\' command use', description='Fishes stuff\nCooldown: 30 seconds\nUsage `.fish`', color=discord.Colour.random())
        elif arg1 == 'deposit' or arg1 == 'dep': em33 = discord.Embed(title='\'Deposit\' command use', description='Deposits coins and puts them in the bank\nUsage: `.deposit|.dep <max/all/amount:int>`', color=discord.Colour.random())
        elif arg1 == 'withdraw' or arg1 == 'with': em = discord.Embed(title='\'Withdraw\' command use', description='Withdraws coins and puts them in the wallet\nUsage: `.withdraw|.with <max/all/amount:int>', color=discord.Colour.random())
        elif arg1 == 'shop': em = discord.Embed(title='\'Shop\' command use', description='Shows the items in shop\nUsage: `.shop`', color=discord.Colour.random())
        elif arg1 == 'inventory' or arg1 == 'inv': em = discord.Embed(title='\'Inventory\' command use', description='Shows a user\'s inventory\nUsage: `.inventory|.inv [@user]', color=discord.Colour.random())
        elif arg1 == 'rob': em = discord.Embed(title='\'Rob\' command use', description='Robs a user\nUsage: `.rob <@user>`', color=discord.Colour.random())
        elif arg1 == 'networth' or arg1 == 'nw': em = discord.Embed(title='\'Networth\' command use', description='Shows the networth of a player in hypixel skyblock\nUsage: `.networth|.nw <playername> [profile]', color=discord.Colour.random())
        elif arg1 == 'auctionhouse' or arg1 == 'ah' or arg1 == 'auction_house': em = discord.Embed(title='\'Auction house\' command use', description='Shows the auction stats of an item in hypixel skyblock\nUsage: `.auctionhouse|.ah <item_id>`', color=discord.Colour.random())
        elif arg1 == 'lbin': em = discord.Embed(title='\'Lowest BIN\' command use', description='Shows the lowest price of an item in hypixel skyblock\nUsage: `.lbin <item_id>`', color=discord.Colour.random())
        elif arg1 == 'say': em = discord.Embed(title='\'Say\' command use', description='Says stuff\nUsage: `.say <text>', color=discord.Colour.random())
        elif arg1 == 'play': em = discord.Embed(title='\'Play\' command use', description='Plays a song in a voice channel\nUsage: `.play|.p <song_name/url>`\n**This command is under development**', color=discord.Colour.random())
        elif arg1 == 'join': em = discord.Embed(title='\'Join\' command use', description='Joins a voice channel\nUsage `.join [#channel]`', color=discord.Colour.random())
        elif arg1 == 'leave': em = discord.Embed(title='\'Leave\' command use', description='Leaves the current connected voice channel\nUsage: `.leave`', color=discord.Colour.random())
        elif arg1 == 'stop': em = discord.Embed(title='\'Stop\' command use', description='Stops the current playing song\nUsage: `.stop`', color=discord.Colour.random())
        elif arg1 == 'pause': em = discord.Embed(title='\'Pause\' command use', description='Pauses the current playing song\nUsage: `.pause`', color=discord.Colour.random())
        elif arg1 == 'resume': em = discord.Embed(title='\'Resume\' command use', description='Resumes a paused song\nUsage: `.resume`', color=discord.Colour.random())
        elif arg1 == 'masterhacker': em = discord.Embed(title='\'Masterhacker\' command use', description='Sends a random image from r/masterhacker\nUsage: `.masterhacker`', color=discord.Colour.random())
        elif arg1 == 'passive': em = discord.Embed(title='\'Passive\' command use', description='Toggles passive mode. If it is turned on people\ncan\'t rob you but you can\'t rob people too\nCooldown: 1 hour\nUsage `.passive`', color=discord.Colour.random())
        elif arg1 == 'sweartoggle': em = discord.Embed(title='\'Sweartoggle\' command use', description='Toggles swear filter for a server. If enabled, when someone sends\na banned word, i will delete it and give the user a warn\nPermissions required: Administrator\nUsage: `.sweartoggle`', color=discord.Colour.random())
        elif arg1 == 'summon': em = discord.Embed(title='\'Summon\' command use', description='Joins in the channel where the message author is\nUsage: `.summon`', color=discord.Colour.random())
        elif arg1 == 'now': em = discord.Embed(title='\'Now\' command use', description='Shows the current playing song', color=discord.Colour.random())
        elif arg1 == 'queue': em = discord.Embed(title='\'Queue\' command use', description='Shows songs in queue', color=discord.Colour.random())
        elif arg1 == 'buy': em = discord.Embed(title='\'Buy\' command use', description='Buys an item from the shop (`.shop`)\nUsage: `.buy <item> [amount]`', color=discord.Colour.random())
        elif arg1 == 'rank' or arg1 == 'xp': em = discord.Embed(title='\'Rank\' command use', description='Shows user activity with levels and xp\nUsage: `.rank|.xp [user]`', color=discord.Colour.random())
        elif arg1 == 'credits': em == discord.Embed(title='\'Credits\' command use', description='Shows the arch bot developer team\nUsage: `.credits.`', color=discord.Colour.random())
        elif arg1 == 'invest': em = discord.Embed(title='\'Invest\' command use', description='Invests coins and claims them after 5 hours with a random amount of profit\nCooldown: random\nUsage: `.invest <claim/amount/all>`', color=discord.Colour.random())
        elif arg1 == 'windowsmeme' or arg1 == 'windowshatememe' or arg1 == 'wm': em = discord.Embed(title='\'windowsmeme\' command use', description="Shows a windows hate meme cause windows bad\nUsage: `.windowsmeme|.wm`", color=discord.Colour.random())
        elif arg1 == 'use' or arg1 == 'open': em = discord.Embed(title='\'use\' command', description="Opens a box\nUsage: `.use|.open <item> [amount]`", color=discord.Colour.random())
        elif arg1 == 'warn': em = discord.Embed(title="\'warn\' command use", description="Warns a user\nUsage: `.warn <user> <reason>`\nPermissions: manage messages", color=discord.Colour.random())
        elif arg1 == 'giveaway': em = discord.Embed(title='\'giveaway\' command use', description="Starts a giveaway in a mentioned channel a mentioned amount of time\nRoles: `Giveaways`\nUsage: `.giveaway`", color=discord.Colour.random())
        elif arg1 == 'reroll': em = discord.Embed(title='\'reroll\' command use', description="Rerolls a giveaway, picks a different winner\nRoles: `Giveaways`\nUsage: `.reroll <#channel> <message_id>`\nExample: `.reroll #giveaways 919224004345208862", color=discord.Colour.random())
        elif arg1 == 'poll': em = discord.Embed(title='\'poll\'command use', description="Starts a poll with 10 max options\nUsage: `.poll <\"question\"> <option1> <option2> [option3-10]", color=discord.Colour.random())
        elif arg1 == "reddit": em = discord.Embed(title='\'reddit\' command use', description="Gets random image from a selected subreddit.\nUsage: `.reddit <subreddit>`", color=discord.Colour.random())
        elif arg1 == "config": em = discord.Embed(title='\'config\' command use', description="Shows the server config or sets new config.\nUsage: `.config [setting] [value]\nPermissions: Manage server\nArguments:\nsetting: bannedwords, swearfilter, linkblocker, welcomemsg, levelupchannel, whitelist, counting\nvalue: __must be int__. 0 disabled, 1 enabled", color=discord.Colour.random())
        elif arg1 == "bannedwords": em = discord.Embed(title='\'bannedwords\' command use', description="Adds blacklisted words to config. If you have any words set up they will be overwritten\nUsage: `.bannedwords <wordlist>`\nExample: `.bannedwords word1 word2`\nPermissions: manage server", color=discord.Colour.random())
        elif arg1 == "evaluate" or arg1 == "eval" or arg1 == "e": em = discord.Embed(title="\'evaluate\' command use", description="executes python code\nUsage: `.evaluate <code>", color=discord.Colour.random())
        elif arg1 == "prefix": em = discord.Embed(title="\'prefix\' command use", description="Changes server prefix\nUsage: `.prefix <prefix>`\nPermissions: Manage server", color=discord.Colour.random())
        elif arg1 == "trivia": em = discord.Embed(title="\'trivia\' command use", description="does trivia\nUsage: `.trivia [difficulty]`\nCooldown: 10 seconds")
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
            return
        else: return await ctx.reply(f"No command \"{arg1}\" found")
        em.set_footer(text='<> is required and [] is optional argument')
        await ctx.reply(embed=em)

    @commands.command(aliases=['warnings'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def warns(self, ctx, *, user : discord.User=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if user == None:
            if str(ctx.message.author.id) not in warnings: userdat[str(ctx.message.author.id)][8] = 0
            await ctx.reply(f"You have {userdat[str(ctx.message.author.id)][8]} warnings")
        else:
            if str(user.id) not in warnings: userdat[str(user.id)][8] = 0
            await ctx.reply(f"{user.display_name} has {userdat[str(user.id)][8]} warnings")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clearwarns(self, ctx, user : discord.User):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        userdat[str(user.id)][8] = 0
        self.save()
        await ctx.reply(f"Cleared all of **{user.display_name}**")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def warn(self, ctx, user : discord.User, *, reason:str):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        guild = self.client.get_guild(ctx.guild.id)
        if str(user.id) not in warnings: userdat[str(user.id)][8] = 0
        await ctx.reply(f"**{user.display_name}** has been warned with reason: {reason}")
        userdat[str(user.id)][8] += 1
        self.save()
        dm = await user.create_dm()
        em = discord.Embed(title=f"You have been warned in {guild}", description=f"Reason: {reason}", color=discord.Colour.random())
        em.set_footer(text=f"You got warned by {ctx.message.author}")
        await dm.send(embed=em)
        return

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stroke(self, ctx, *, arg1):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if arg1.isdigit:
            if int(arg1) > 750: return
            strok = ('').join(random.choices(string.ascii_lowercase + string.digits, k=int(arg1)))
            await ctx.send(strok)
        else:
            await ctx.reply(f"{arg1} isnt a number dood")
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stroktranslate(self, ctx, strok:str):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        try:
            if len(strok) > 300: return await ctx.reply("Please use no more than 300 length")
            else:
                with open(f"{cwd}/database/words.json", "r") as f:
                    words = json.load(f)
                var = str()
                s = strok.lower()
                for i, c in enumerate(s):
                    var += random.choice(words[c])
                return await ctx.send(f"{var}")
        except Exception as e:
            return await ctx.send(f"{type(e).__name__}: {e}")

    @commands.command(aliases=['8ball'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def _8ball(self, ctx, *, question):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if channel == None:
            await ctx.send("You did not mention a channel!")
            return

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="Has been Nuked!")
            await nuke_channel.delete()
            await new_channel.send("This channel has been nuked!")
            await ctx.send("Nuked the Channel sucessfully!")
        else:
            await ctx.send(f"No channel named {channel.name} was found!")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invites(self, ctx, *, user : discord.User=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def purge(self, ctx, amount:int):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if int(amount) == 0: return await ctx.reply("You can\'t purge 0 messages **dood**")
        elif int(amount) < 0: return await ctx.reply("You can\'t spawn messages")
        elif int(amount) > 500: return await ctx.reply("You can\'t purge more than 500 messages")
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        embedSuccessPurge = discord.Embed(title='Purge Successful', description=f'Purged {amount} messages from this channel.', color=discord.Colour.random())
        await ctx.send(embed = embedSuccessPurge)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nudes(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        async with ctx.typing():
            memes_submissions = reddit.subreddit('Nude_Selfie').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title)
            embed.set_image(url=submission.url)
            embed.set_footer(text="guess who is horny")
        await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ihadastroke(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        async with ctx.typing():
            memes_submissions = reddit.subreddit('ihadastroke').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title, color=discord.Colour.random())
            embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

    @commands.command(aliases=['mh'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def masterhacker(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        async with ctx.typing():
            memes_submissions = reddit.subreddit('masterhacker').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title, color=discord.Colour.random())
            embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def reddit(self, ctx, sub:str):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
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

    @commands.command(aliases=['hl'])
    @commands.cooldown(1, 40, commands.BucketType.user)
    async def highlow(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        numb = random.randint(1, 100)
        numb2 = random.randint(1, 100)
        id = str(ctx.message.author.id)
        rand = ''.join(map(str, random.choices([1, 2], weights=[100, float(userdat[str(ctx.message.author.id)][3])], k=1)))
        if rand == str(1):
            coins = random.randint(300, 1000)
            userdat[str(ctx.message.author.id)][3] += round(random.random(), 2)
        else:
            coins = random.randint(10000, 100000000)
            userdat[str(ctx.message.author.id)][3] = 0
        self.save()

        def check(msg):
            return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

        await ctx.send(f'Your number is {numb} choose if the other is lower, higher or jackpot')
        msg = await self.client.wait_for("message", check=check)
        if msg.content == 'low':
            if numb > numb2:
                await ctx.send(f'Congrats, your number was {numb2} and you earned {coins} coins')
                userdat[str(ctx.message.author.id)][0] += coins
                self.save()
                return
            elif numb < numb2:
                await ctx.send(f'Incorrect the number was {numb2}')
            elif numb == numb2:
                await ctx.send(f'no')
        elif msg.content == 'jackpot':
            if numb == numb2:
                coins2 = randint(1000000, 5000000)
                await ctx.send(f'Congrats, your number was {numb2} and you earned {coins2} coins gg!')
                userdat[str(ctx.message.author.id)][0] += coins2
                self.save()
                return
            else:
                await ctx.send(f'Incorrect the number was {numb2}')
                return
        elif msg.content == 'high':
            if numb < numb2:
                await ctx.send(f'Congrats, your number was {numb2} and you earned {coins} coins')
                userdat[str(ctx.message.author.id)][0] += coins
                self.save()
                return
            else:
                await ctx.send(f'Incorrect your number was {numb2}')
                return
        else:
            await ctx.send(f'{msg.content} is not an option')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kill(self, ctx, user : discord.User=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if user == None:
            await ctx.send('Please tag someone to kill')
        elif user.id == ctx.message.author.id:
            await ctx.send('Ok you are dead, please tag someone else to kill')
        else:
            responses = [
                f"**{user.display_name}** died from a dang baguette",
                f"<@{ctx.message.author.id}> strikes **{user.display_name}** with the killing curse... *Avada Kedavra!*",
                f"**{user.display_name} dies from dabbing too hard",
                f"**{user.display_name}** ripped their own heart out to show their love for <@{ctx.message.author.id}>"
            ]
            await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, *, member : discord.Member):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if member == ctx.message.author:
            raise BadArgument
        else:
            await member.kick()
        await ctx.send(f'{member} has been kicked from the server')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ban(self, ctx, *, member : discord.Member):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if member == ctx.message.author:
            raise BadArgument
        else:
            await member.ban()
        await ctx.send(f'{member} has been banned from the server')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slap(self, ctx, user : discord.User):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def softwaregore(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        x = randint(1, 10)
        if num == x:
            coins = randint(100, 1000)
            await ctx.reply(f'Correct! You got {coins} coins')
            userdat[str(ctx.message.author.id)][0] += coins
            self.save()
        else:
            await ctx.reply(f'Nope it was {x}')

    @commands.command(aliases=['sus'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def isSus(self, ctx, *, user : discord.User):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        await ctx.send(f'{ctx.message.author.mention} What type of meme you want to post?\n`f` Fresh meme\n`d` Dank meme\n`c` Copypasta\n*more comming soon*')

        def check(msg):
            return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content) in ['f', 'd', 'c']

        msg = await self.client.wait_for("message", check=check)

        x = randint(0, 200)
        if x == 0:
            await ctx.send(f'{ctx.message.author.mention} You earned 0 coins xD')
        else:
            await ctx.send(f'You earned {x} coins')
            userdat[str(ctx.message.author.id)][0] += x
            self.save()

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def null(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        await ctx.reply('You got **null** coins dood.')

    @commands.command(aliases=['gift'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def give(self, ctx, user : discord.User, amount:int, item:str=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if user.id == ctx.message.author.id:
            await ctx.reply('You can\'t gift yourself')
            return
        if userdat[str(ctx.message.author.id)][6] == 1:
            await ctx.reply("You have passive mode enabled, you can\'t gigt to other users", mention_author=False)
            return
        if userdat[str(user.id)][6] == 1:
            await ctx.reply("This user has passive mode enabled. Leave them alone!", mention_author=False)
            return
        else:
            if item == None:
                if userdat[str(ctx.message.author.id)][0] < int(amount):
                    await ctx.reply('You don\'t have that many coins in your wallet')
                    return
                elif int(amount) < 0 or int(amount) == 0:
                    await ctx.reply('Don\'t try to break me **dood**')
                    return
                else:
                    userdat[str(ctx.message.author.id)][0] -= int(amount)
                    self.save()
                    userdat[str(user.id)][0] += int(amount)
                    self.save()
                    await ctx.reply(f'You gave {amount} coins to {user.display_name}')
            elif item == "windows10":
                if userdat[str(ctx.message.author.id)][9] < int(amount):
                    await ctx.reply("You don\'t have that many items")
                    return
                elif int(amount) < 0 or int(amount) == 0:
                    await ctx.reply("Don\'t try to break me **dood**")
                    return
                else:
                    if str(user.id) not in windows10:
                        userdat[str(user.id)][9] = 0
                    userdat[str(ctx.message.author.id)][9] -= int(amount)
                    self.save()
                    userdat[str(user.id)][9] += int(amount)
                    self.save()
                    await ctx.reply(f"You gave {amount} windows 10 keys to {user.display_name}")
                    return
            elif item == "bronzecoin":
                if userdat[str(ctx.message.author.id)][10] < int(amount):
                    await ctx.reply("You don\'t have that many items")
                    return
                elif int(amount) < 0 or int(amount) == 0:
                    await ctx.reply("Don\'t try to break me **dood**")
                    return
                else:
                    if str(user.id) not in bronzecoin:
                        userdat[str(user.id)][10] = 0
                    userdat[str(ctx.message.author.id)][10] -= int(amount)
                    self.save()
                    userdat[str(user.id)][10] += int(amount)
                    self.save()
                    await ctx.reply(f"You gave {amount} bronze coins to {user.display_name}")
                    return
            elif item == "silvercoin":
                if userdat[str(ctx.message.author.id)][11] < int(amount):
                    await ctx.reply("You don\'t have that many items")
                    return
                elif int(amount) < 0 or int(amount) == 0:
                    await ctx.reply("Don\'t try to break me **dood**")
                    return
                else:
                    if str(user.id) not in silvercoin:
                        userdat[str(user.id)][11] = 0
                    userdat[str(ctx.message.author.id)][11] -= int(amount)
                    self.save()
                    userdat[str(user.id)][11] += int(amount)
                    self.save()
                    await ctx.reply(f"You gave {amount} silver coins keys to {user.display_name}")
                    return
            elif item == "goldcoin":
                if userdat[str(ctx.message.author.id)][12] < int(amount):
                    await ctx.reply("You don\'t have that many items")
                    return
                elif int(amount) < 0 or int(amount) == 0:
                    await ctx.reply("Don\'t try to break me **dood**")
                    return
                else:
                    if str(user.id) not in goldcoin:
                        userdat[str(user.id)][12] = 0
                    userdat[str(ctx.message.author.id)][12] -= int(amount)
                    self.save()
                    userdat[str(user.id)][12] += int(amount)
                    self.save()
                    await ctx.reply(f"You gave {amount} gold coins keys to {user.display_name}")
                    return
            else:
                await ctx.reply("No such item")
                return

    @commands.command()
    async def add(self, ctx, user:discord.User, amount:int, place:str=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if ctx.message.author.id not in ids:
            return
        else:
            if str(user.id) not in userdat:
                to_append1 = list()
                for i in range(userlen):
                    to_append1.append(0)
                self.addv(userdat, str(user.id), list(to_append1))
                self.save()
            if place == None or str(place) == "wallet":
                userdat[str(user.id)][0] += int(amount)
                await ctx.reply(f"Added {amount} coins to {user.display_name}\'s wallet")
                self.save()
                return
            elif place == "bank":
                userdat[str(user.id)][1] += int(amount)
                self.save()
                await ctx.reply(f"Added {amount} coins in {user.display_name}\'s bank")
                return
            else:
                raise BadArgument

    @commands.command()
    async def setrng(self, ctx, user:discord.User, rate:float):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        userdat[str(user.id)][3] = rate
        self.save()
        return await ctx.reply(f"Set RNG rate of {user.display_name} to {rate}%")

    @commands.command()
    async def rich(self, ctx, isglobal="server"):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        arr = []
        values = list(userdat.values())
        keys = list(userdat.keys())
        for i in range(len(values)):
            arr.append(int(values[i][0]))
        users = []
        if isglobal == "global":
            for i in range(10):
                users.append(keys[arr.index(max(arr))])
                keys.remove(keys[arr.index(max(arr))])
                arr.remove(max(arr))
            embed = discord.Embed(title=f"Global money leaderboard for thatOneArchBot")
            i = 1
            for user in users:
                if userdat[str(user)][0] == 0 and users.index(str(user)) == 0: return await ctx.reply("No rich people here")
                elif userdat[str(user)][0] == 0 and users.index(str(user)) != 0: break
                uname = self.client.get_user(int(user))
                embed.add_field(name=f"#{i} {uname}", value=str(userdat[str(user)][0]))
                i += 1
        elif isglobal == "server":
            guild = self.client.get_guild(int(ctx.guild.id))
            for i in range(10):
                users.append(keys[arr.index(max(arr))])
                keys.remove(keys[arr.index(max(arr))])
                arr.remove(max(arr))
            embed = discord.Embed(title=f"Leaderboard for {ctx.guild}")
            i = 1
            for user in users:
                if userdat[str(user)][0] == 0 and users.index(str(user)) == 0: return await ctx.reply("No rich people here")
                elif userdat[str(user)][0] == 0 and users.index(str(user)) != 0: break
                if guild.get_member(int(user)) is not None:
                    uname = self.client.get_user(int(user))
                    embed.add_field(name=f"#{i} {uname}", value=str(userdat[str(user)][0]))
                    i += 1
                else: pass
        else: raise BadArgument
        embed.set_footer(text="This is wallet worth, not networth")
        await ctx.send(embed=embed)

    @commands.command()
    async def leaderboard(self, ctx, isglobal="server"):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        arr = []
        values = list(userdat.values())
        keys = list(userdat.keys())
        for i in range(len(values)):
            arr.append(int(values[i][5]))
        users = []
        if isglobal == "global":
            for i in range(10):
                users.append(keys[arr.index(max(arr))])
                keys.remove(keys[arr.index(max(arr))])
                arr.remove(max(arr))
            embed = discord.Embed(title=f"Global level leaderboard for thatOneArchBot")
            i = 1
            for user in users:
                uname = self.client.get_user(int(user))
                embed.add_field(name=f"#{i} {uname}", value=str(userdat[str(user)][0]))
                i += 1
        elif isglobal == "server":
            guild = self.client.get_guild(int(ctx.guild.id))
            for i in range(10):
                users.append(keys[arr.index(max(arr))])
                keys.remove(keys[arr.index(max(arr))])
                arr.remove(max(arr))
            embed = discord.Embed(title=f"Ranking leaderboard for {ctx.guild}")
            i = 1
            for user in users:
                if guild.get_member(int(user)) is not None:
                    uname = self.client.get_user(int(user))
                    embed.add_field(name=f"#{i} {uname}", value=str(userdat[str(user)][5]))
                    i += 1
                else: pass
        else: raise BadArgument
        await ctx.send(embed=embed)

    @commands.command(name="invest")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def _invest(self, ctx, action:str):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if ctx.message.author.id not in no_cooldowns: pass
        else:
            if str(action) == "all" or str(action) == "max":
                if userdat[str(ctx.message.author.id)][0] <= 0:
                    return await ctx.reply(f"Don\'t try to break me dood")
                userdat[str(ctx.message.author.id)][2] += userdat[str(ctx.message.author.id)][0]
                userdat[str(ctx.message.author.id)][0] = 0
                self.save()
                rnd = ''.join(map(str, random.choices([3, 5, 10, 25, 50, 100, 1000, 1000000, 1000000000000], weights=[75, 50, 15, 10, 5, 2.5, 1, float(userdat[str(ctx.message.author.id)][3]), round(float(userdat[str(ctx.message.author.id)][3]) / 2)], k=1)))
                if rnd == str(1000000) or rnd == str(1000000000000): 
                    a = round(userdat[str(ctx.message.author.id)][2] * float(rnd))
                    await ctx.reply(f"You claimed {a} coins with {rnd} profit. Your RNG rate was {userdat[str(ctx.message.author.id)][3]}% and now it is reset.")
                    userdat[str(ctx.message.author.id)][0] += a
                    userdat[str(ctx.message.author.id)][2] = 0
                    userdat[str(ctx.message.author.id)][3] = 0
                    return self.save()
                a = round(userdat[str(ctx.message.author.id)][2] * float(rnd))
                userdat[str(ctx.message.author.id)][0] += a 
                userdat[str(ctx.message.author.id)][2] = 0
                userdat[str(ctx.message.author.id)][3] += round(random.random(), 2)
                self.save()
                if float(rnd) < 0.0: return await ctx.reply(f"You claimed {a} coins with a {rnd} loss")
                elif float(rnd) == 0.0: return await ctx.reply(f"You lost all your coins.")
                else: return await ctx.reply(f"You claimed {a} coins with {rnd}x profit")
            try:
                float(action)
            except Exception as e:
                if action.endswith("k"):
                    i = action.replace("k", "")
                    action = int(i) * 1000
                elif action.endswith("m"):
                    i = action.replace("m", "")
                    action = int(i) * 1000000
                elif action.endswith("b"):
                    i = action.replace("b", "")
                    action = int(i) * 1000000000
                else: return await ctx.reply(e)
            if int(float(action)) <= 0 or not float(action).is_integer():
                return await ctx.reply("Don\'t try to break me dood")
            else:
                if int(float(action)) > int(userdat[str(ctx.message.author.id)][0]): return await ctx.reply("you don\'t have that much money in your wallet.")
                userdat[str(ctx.message.author.id)][2] += int(float(action))
                userdat[str(ctx.message.author.id)][0] -= int(float(action))
                self.save()
                rnd = ''.join(map(str, random.choices([3, 5, 10, 25, 50, 100, 1000, 1000000, 1000000000000], weights=[75, 50, 15, 10, 5, 2.5, 1, float(userdat[str(ctx.message.author.id)][3]), round(float(userdat[str(ctx.message.author.id)][3]) / 2)], k=1)))
                if rnd == str(1000000) or rnd == str(1000000000000): 
                    a = round(userdat[str(ctx.message.author.id)][2] * float(rnd))
                    await ctx.reply(f"You claimed {a} coins with {rnd} profit. Your RNG rate was {userdat[str(ctx.message.author.id)][3]}% and now it is reset.")
                    userdat[str(ctx.message.author.id)][0] += a
                    userdat[str(ctx.message.author.id)][2] = 0
                    userdat[str(ctx.message.author.id)][3] = 0
                    return self.save()
                a = round(userdat[str(ctx.message.author.id)][2] * float(rnd))
                userdat[str(ctx.message.author.id)][0] += a
                userdat[str(ctx.message.author.id)][2] = 0
                userdat[str(ctx.message.author.id)][3] += round(random.random(), 2)
                self.save()
                if float(rnd) < 0.0: return await ctx.reply(f"You claimed {a} coins with a {rnd} loss")
                elif float(rnd) == 0.0: return await ctx.reply(f"You lost all your coins.")
                else: return await ctx.reply(f"You claimed {a} coins with {rnd}x profit")
        if str(action) == "claim":
            if str(ctx.message.author.id) not in money or userdat[str(ctx.message.author.id)][2] == 0: return await ctx.reply("You didnt invest any coins. Type `.invest <amount>` to invest some coins")
            if ctx.message.author.id not in no_cooldowns:
                i = datetime.datetime.now() - cd[str(ctx.message.author.id)]
                if i is None or i.seconds > invest_time: cd[str(ctx.message.author.id)] = datetime.datetime.now()
                else: return await ctx.reply("You cant claim your money yet")
            rnd = ''.join(map(str, random.choices([0, 0.5, 0.75, 1.25, 1.5, 1.75, 2, 2.5, 5, 1000000, 1000000000000], weights=[0.5, 3, 5, 75, 45, 5, 3, 1, 0.5, float(userdat[str(ctx.message.author.id)][3]), round(float(userdat[str(ctx.message.author.id)][3]) / 2)], k=1)))
            if rnd == str(1000000) or rnd == str(1000000000000):  
                a = round(userdat[str(ctx.message.author.id)][2] * float(rnd))
                await ctx.reply(f"You claimed {a} coins with {rnd} profit. Your RNG rate was {userdat[str(ctx.message.author.id)][3]}% and now it is reset.")
                userdat[str(ctx.message.author.id)][0] += a
                userdat[str(ctx.message.author.id)][2] = 0
                userdat[str(ctx.message.author.id)][3] = 0
                return self.save()
            userdat[str(ctx.message.author.id)][3] = 0
            a = round(userdat[str(ctx.message.author.id)][2] * float(rnd))
            userdat[str(ctx.message.author.id)][0] += a
            userdat[str(ctx.message.author.id)][2] = 0
            userdat[str(ctx.message.author.id)][3] += round(random.random(), 2)
            self.save()
            return await ctx.reply(f"You claimed {a} coins with {rnd} profit.")
        elif str(action) == "all" or str(action) == "max":
            if userdat[str(ctx.message.author.id)][0] < 10000: return await ctx.reply("You can\'t invest less than 10000 coins")
            else:
                m = round(sys.maxsize / 5)
                maxv = m - 1
                def check(msg):
                    return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

                await ctx.reply(f"Are you sure you want to invest {userdat[str(ctx.message.author.id)][0]} coins? If you invest them you wont have them in your wallet for some time\nYou can claim after the coins after some time using `.invest claim`\nType yes or no")
                msg = await self.client.wait_for("message", check=check)
                if msg.content.lower() == "no": return await ctx.send("Ok guess you are not gonna invest today")
                elif msg.content.lower() == "yes":
                    try:
                        i = datetime.datetime.now() - cd[str(ctx.message.author.id)]
                    except KeyError:
                        i = None
                        cd[str(ctx.message.author.id)] = datetime.datetime.now()
                    if i is None or i.seconds > invest_time: cd[str(ctx.message.author.id)] = datetime.datetime.now()
                    else: return await ctx.reply("You already have invested coins")
                    if userdat[str(ctx.message.author.id)][2] == 0: pass
                    else: return await ctx.send("There are unclaimed coins. Type `.invest claim` to claim them")
                    userdat[str(ctx.message.author.id)][2] += userdat[str(ctx.message.author.id)][0]
                    await ctx.send(f"You invested {userdat[str(ctx.message.author.id)][2]} coins. Come back in {round(invest_time / 3600)} hours to claim your coins")
                    userdat[str(ctx.message.author.id)][0] = 0
                    self.save()
                    return
                else: return await ctx.send(f"You are supposed to type yes or no. Not {msg.content}")
        else:
            try:
                float(action)
            except Exception as e:
                if action.endswith("k"):
                    i = action.replace("k", "")
                    action = int(i) * 1000
                elif action.endswith("m"):
                    i = action.replace("m", "")
                    action = int(i) * 1000000
                elif action.endswith("b"):
                    i = action.replace("b", "")
                    action = int(i) * 1000000000
                else: return await ctx.reply(e)
            if int(float(action)) <= 0 or not float(action).is_integer():
                return await ctx.reply("Don\'t try to break me dood")
            if int(float(action)) < 10000: return await ctx.reply("You can\'t invest less than 10000 coins")
            else:
                if int(float(action)) > userdat[str(ctx.message.author.id)][0]: return await ctx.reply("You dont have that many coins in your wallet")
                else:
                    m = round(sys.maxsize / 5)
                    maxv = m - 1
                    def check(msg):
                        return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

                    await ctx.reply(f"Are you sure you want to invest {int(float(action))} coins? If you invest them you wont have them in your wallet for some time\nYou can claim after the coins after some time using `.invest claim`\nType yes or no")
                    msg = await self.client.wait_for("message", check=check)
                    if msg.content == "no": return await ctx.send("Ok guess you are not gonna invest today")
                    elif msg.content == "yes":
                        try:
                            i = datetime.datetime.now() - cd[str(ctx.message.author.id)]
                        except KeyError:
                            i = None
                            cd[str(ctx.message.author.id)] = datetime.datetime.now()
                        if i is None or i.seconds > invest_time: cd[str(ctx.message.author.id)] = datetime.datetime.now()
                        else: return await ctx.reply("You already have invested coins")
                        if userdat[str(ctx.message.author.id)][2] == 0: pass
                        else: return await ctx.send("There are unclaimed coins. Type `.invest claim` to claim them")
                        userdat[str(ctx.message.author.id)][2] += int(action)
                        userdat[str(ctx.message.author.id)][0] -= int(action)
                        self.save()
                        if ctx.message.author.id not in no_cooldowns:
                            await ctx.send(f"You invested {int(float(action))} coins. Come back in {round(invest_time / 3600)} hours to claim your coins")
                        else:
                            await ctx.send(f"You invested {int(float(action))} coins. You have no cooldown so you can claim your coins now")
                        return
                    else:
                        await ctx.send(f"You are supposed to type yes or no. Not {msg.content}")
                        return

    @commands.command(aliases=["job"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def work(self, ctx, *, arg1=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if arg1 == None:
            if userdat[str(ctx.message.author.id)][7] == 0:
                await ctx.reply("You dont have a job yet. Type `.work list` to see the list of jobs")
                return
            else:
                j = userdat[str(ctx.message.author.id)][7]
                if ctx.message.author.id not in no_cooldowns:
                    try:
                        last_work = datetime.datetime.now() - on_cooldown[str(ctx.message.author.id)]
                    except KeyError:
                        last_work = None
                        on_cooldown[str(ctx.message.author.id)] = datetime.datetime.now()
                    if last_work is None or last_work.seconds > work_cooldown:
                        on_cooldown[str(ctx.message.author.id)] = datetime.datetime.now()
                        pass
                    else:
                        await ctx.reply("This command is on cooldown")
                        return 
                else:
                    pass
                if j == "mod":
                    await ctx.reply("You earned 5000 coins from Discord Moderator job")
                    userdat[str(ctx.message.author.id)][0] += 5000
                    self.save()
                    return
                elif j == "yt":
                    await ctx.reply("You earned 6000 coins from YouTuber job")
                    userdat[str(ctx.message.author.id)][0] += 6000
                    self.save()
                    return
                elif j == "ts":
                    await ctx.reply("You earned 6900 coins from Twitch Streamer job")
                    userdat[str(ctx.message.author.id)][0] += 6900
                    self.save()
                    return
                elif j == "pg":
                    await ctx.reply("You earned 15000 coins from Pro Gamer job")
                    userdat[str(ctx.message.author.id)][0] += 15000
                    self.save()
                    return
                elif j == "dc":
                    await ctx.reply("You earned 20000 coins from Doctor job")
                    userdat[str(ctx.message.author.id)][0] += 20000
                    self.save()
                    return
                elif j == "dev":
                    await ctx.reply("You earned 25000 coins from Developer job")
                    userdat[str(ctx.message.author.id)][0] += 25000
                    self.save()
                    return
                elif j == "sc":
                    await ctx.reply("You earned 75000 coins from Scientist job")
                    userdat[str(ctx.message.author.id)][0] += 75000
                    self.save()
                    return
                elif j == "ab":
                    await ctx.reply("You earned 169420 coins and a **developer box** from thatOneArchBot developer job")
                    userdat[str(ctx.message.author.id)][0] += 169420
                    userdat[str(ctx.message.author.id)][15] += 1
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
            if userdat[str(ctx.message.author.id)][7] == 0:
                await ctx.reply("You dont have a job")
                return
            else:
                userdat[str(ctx.message.author.id)][7] = 0
                await ctx.reply("You resigned from your job.")
                self.save()
                return
        elif str(arg1) == "mod":
            if userdat[str(ctx.message.author.id)][7] == 0:
                userdat[str(ctx.message.author.id)][7] = "mod"
                await ctx.reply("You are working as a **Discord Moderator** now!")
                self.save()
                return
            else:
                await ctx.reply("You already have a job. Type `.work resign` to quit your job.")
                return
        elif str(arg1) == "yt":
            if userdat[str(ctx.message.author.id)][7] == 0:
                if userdat[str(ctx.message.author.id)][5] >= 5:
                    userdat[str(ctx.message.author.id)][7] = "yt"
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
            if userdat[str(ctx.message.author.id)][7] == 0:
                if userdat[str(ctx.message.author.id)][5] >= 5:
                    userdat[str(ctx.message.author.id)][7] = "ts"
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
            if userdat[str(ctx.message.author.id)][7] == 0:
                if userdat[str(ctx.message.author.id)][5] >= 10:
                    userdat[str(ctx.message.author.id)][7] = "pg"
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
            if userdat[str(ctx.message.author.id)][7] == 0:
                if userdat[str(ctx.message.author.id)][5] >= 15:
                    userdat[str(ctx.message.author.id)][7] = "dc"
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
            if userdat[str(ctx.message.author.id)][7] == 0:
                if userdat[str(ctx.message.author.id)][5] >= 20:
                    userdat[str(ctx.message.author.id)][7] = "dev"
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
            if userdat[str(ctx.message.author.id)][7] == 0:
                if userdat[str(ctx.message.author.id)][5] >= 50:
                    userdat[str(ctx.message.author.id)][7] = "sc"
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
            if userdat[str(ctx.message.author.id)][7] == 0:
                if userdat[str(ctx.message.author.id)][5] >= 69:
                    userdat[str(ctx.message.author.id)][7] = "ab"
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
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        rand = ''.join(map(str, random.choices([1, 2], weights=[100, float(userdat[str(ctx.message.author.id)][3])], k=1)))
        if rand == str(1):
            coins = random.randint(100, 5000)
            await ctx.send(f'You earned {coins} coins.')
            userdat[str(ctx.message.author.id)][3] += round(random.random(), 2)
        else:
            coins = random.randint(50000, 69696969696969)
            await ctx.send(f'You earned {coins} coins (RNG).')
            userdat[str(ctx.message.author.id)][3] = 0
        userdat[str(ctx.message.author.id)][0] += coins
        self.save()

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        userdat[str(ctx.message.author.id)][0] += 10000
        userdat[str(ctx.message.author.id)][14] += 1
        await ctx.send('You claimed 10,000 coins and a daily box!')
        self.save()

    @commands.command(aliases=['dep'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def deposit(self, ctx, *, arg1:str):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        bank = userdat[str(ctx.message.author.id)][5] * 10000
        bankspace = userdat[str(ctx.message.author.id)][19] + bank
        if arg1 == 'all' or arg1 == 'max':
            if userdat[str(ctx.message.author.id)][0] == 0: return await ctx.send('You don\'t have any coins in your wallet')
            else:
                if userdat[str(ctx.message.author.id)][0] > bankspace:
                    to_deposit = bankspace - userdat[str(ctx.message.author.id)][1]
                    if to_deposit == 0: return await ctx.reply("You have a full bank")
                    userdat[str(ctx.message.author.id)][1] += to_deposit
                    userdat[str(ctx.message.author.id)][0] -= to_deposit
                    return await ctx.reply(f"You deposited {to_deposit} coins")
                await ctx.reply(f'You deposited {userdat[str(ctx.message.author.id)][0]} coins')
                userdat[str(ctx.message.author.id)][1] += int(userdat[str(ctx.message.author.id)][0])
                userdat[str(ctx.message.author.id)][0] -= int(userdat[str(ctx.message.author.id)][0])
                self.save()
                return
        try:
            float(arg1)
        except Exception as e:
            if arg1.endswith("k"):
                i = arg1.replace("k", "")
                arg1 = int(i) * 1000
            elif arg1.endswith("m"):
                i = arg1.replace("m", "")
                arg1 = int(i) * 1000000
            elif arg1.endswith("b"):
                i = arg1.replace("b", "")
                arg1 = int(i) * 1000000000
            else: return await ctx.reply(e)
        if int(float(arg1)) <= 0 or not float(arg1).is_integer():
            return await ctx.reply("Don\'t try to break me dood")
        if int(float(arg1)) > userdat[str(ctx.message.author.id)][0]: return await ctx.reply('You don\'t have that many coins in your wallet')
        elif int(float(arg1)) < 0: return await ctx.reply('Don\'t try to break me dood')
        elif int(float(arg1)) > bankspace: return await ctx.send("You cant deposit that many coins because of your bank limit")
        else:
            await ctx.send(f'You deposited {int(float(arg1))} coins')
            userdat[str(ctx.message.author.id)][0] -= int(float(arg1))
            userdat[str(ctx.message.author.id)][1] += int(float(arg1))
            self.save()

    @commands.command(aliases=['with'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def withdraw(self, ctx, *, arg1):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if arg1 == 'all' or arg1 == 'max':
            if userdat[str(ctx.message.author.id)][1] == 0: return await ctx.send('You don\'t have any coins in your bank')
            else:
                if userdat[str(ctx.message.author.id)][1] == 1: await ctx.reply(f'You withdrawn {userdat[str(ctx.message.author.id)][1]} coin')
                else: await ctx.reply(f'You withdrawn {userdat[str(ctx.message.author.id)][1]} coins')
                userdat[str(ctx.message.author.id)][0] += int(userdat[str(ctx.message.author.id)][1])
                userdat[str(ctx.message.author.id)][1] -= int(userdat[str(ctx.message.author.id)][1])
                self.save()
                return
        try:
            float(action)
        except Exception as e:
            if action.endswith("k"):
                i = action.replace("k", "")
                action = int(i) * 1000
            elif action.endswith("m"):
                i = action.replace("m", "")
                action = int(i) * 1000000
            elif action.endswith("b"):
                i = action.replace("b", "")
                action = int(i) * 1000000000
            else: return await ctx.reply(e)
        if int(float(arg1)) <= 0 or not float(float(arg1)).is_integer():
            return await ctx.reply("Don\'t try to break me dood")
        if int(float(arg1)) > userdat[str(ctx.message.author.id)][0]: return await ctx.reply('You don\'t have that many coins in your wallet')
        elif int(float(arg1)) < 0: return await ctx.reply('Don\'t try to break me dood')
        else:
            await ctx.send(f'You withdrawn {int(float(arg1))} coins')
            userdat[str(ctx.message.author.id)][0] += int(float(v))
            userdat[str(ctx.message.author.id)][1] -= int(float(v))
            self.save()

    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def rob(self, ctx, user : discord.User):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if ctx.message.author.id == user.id: return await ctx.send('you cant rob yourself xd')
        else:
            if str(user.id) not in wallet:
                userdat[str(user.id)][0] = 0
            if str(user.id) not in passiveUsers:
                userdat[str(user.id)][6] = 0
            if userdat[str(ctx.message.author.id)][6] == 1:
                await ctx.reply(f"You are on passive mode. You can\'t rob other people")
                return
            if userdat[str(user.id)][6] == 1:
                await ctx.reply(f"{user.display_name} has passive mode turned on. You can\'t rob them")
                return
            if userdat[str(user.id)][0] < 500:
                await ctx.send('This user has less than 500 coins')
            elif userdat[str(user.id)][0] >= 500:
                coins = random.randint(500, int(userdat[str(user.id)][0]))
                userdat[str(user.id)][0] -= coins
                self.save()
                userdat[str(ctx.message.author.id)][0] += coins
                self.save()
                await ctx.send(f'You stole {coins} coins from **{user.display_name}**')

    @commands.command()
    @commands.cooldown(1, 604800, commands.BucketType.user)
    async def weekly(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        userdat[str(ctx.message.author.id)][0] += 50000
        await ctx.reply('You claimed 50,000 coins')
        self.save()

    @commands.command()
    @commands.cooldown(1, 2592000, commands.BucketType.user)
    async def monthly(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        userdat[str(ctx.message.author.id)][0] += 100000
        await ctx.send('You claimed 100,000 coins')
        self.save()

    @commands.command(aliases=['bal'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def balance(self, ctx, user : discord.User=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if user == None: user = ctx.author
        else:
            if str(user.id) not in userdat:
                to_append1 = list()
                for i in range(userlen):
                    to_append1.append(0)
                self.addv(userdat, str(user.id), list(to_append1))
                self.save()
        win10v = userdat[str(user.id)][9] * 69420
        bcoinv = userdat[str(user.id)][10] * 50000
        scoinv = userdat[str(user.id)][11] * 250000
        gcoinv = userdat[str(user.id)][12] * 1000000
        dboxv = userdat[str(user.id)][15] * 69000000000000
        dailyboxv = userdat[str(user.id)][14] * 10000
        networth = userdat[str(user.id)][0] + userdat[str(user.id)][1] + win10v + bcoinv + scoinv + gcoinv + dboxv + dailyboxv
        bank = userdat[str(user.id)][5] * 10000
        bankspace = userdat[str(user.id)][19] + bank
        embed = discord.Embed(title=f"{user.display_name}'s Balance", description=f"Wallet: {userdat[str(user.id)][0]}\nBank: {userdat[str(user.id)][1]}/{bankspace} `({round(self.get_change(userdat[str(user.id)][1], bankspace), 2)}%)`\nNetworth: {networth}\nRNG rate: {str(round(userdat[str(user.id)][3], 2))}%", color=discord.Colour.random())
        embed.set_footer(text=f'Currency system made by {owner}')
        await ctx.send(embed=embed)

    @commands.command(aliases=["lm"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def linuxmeme(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        async with ctx.typing():
            memes_submissions = reddit.subreddit('linuxmemes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title = submission.title, color=discord.Colour.random())
            embed.set_image(url=submission.url)
        await ctx.send(embed = embed)

    @commands.command(aliases=["wm"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def windowsmeme(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def networth(self, ctx, *, arg1, arg2=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
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
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def auctionhouse(self, ctx, *, arg1):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
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
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverinfo(self, ctx):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
        gowner = str(ctx.guild.owner)
        gid = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)
    
        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.random()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=gowner, inline=True)
        embed.add_field(name="Server ID", value=gid, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def userinfo(self, ctx, member:discord.Member = None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if member == None:
                member = ctx.message.author

        embed=discord.Embed(
            title="User Information", 
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.random()
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Username:", value=member.name, inline=False)
        embed.add_field(name="Display name:", value=member.nick, inline=False)
        embed.add_field(name="User ID:", value=member.id, inline=False)
        embed.add_field(name="Account Created At:",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined Server At:",value=member.joined_at.strftime("%a %#d %B %Y, %I:%M %p UTC"), inline=False)
        if member.id not in ids: pass
        else: embed.set_footer(text=f"{member.display_name} is a bot admin")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lock(self, ctx, channel : discord.TextChannel=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        em = discord.Embed(title=':white_check_mark: channel locked successfully.', color=discord.Colour.random())
        await ctx.send(embed=em)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unlock(self, ctx, channel : discord.TextChannel=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        em = discord.Embed(title=':white_check_mark: channel unlocked successfully.', color=discord.Colour.random())
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lbin(self, ctx, *, arg1):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
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

    def cleanup_code(self, content):
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        return content.strip('` \n')

    def get_syntax_error(self, e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

    @commands.command(name='evaluate', aliases=['eval', 'e'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def _eval(self, ctx, *, body):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        if ctx.message.author.id not in ids: return
        blocked_words = ['while', 'quit', 'exit', 'SystemExit', 'open', '.delete()', 'os', 'subprocess', 'history()', '("token")', "('token')",
                        'aW1wb3J0IG9zCnJldHVybiBvcy5lbnZpcm9uLmdldCgndG9rZW4nKQ==', 'aW1wb3J0IG9zCnByaW50KG9zLmVudmlyb24uZ2V0KCd0b2tlbicpKQ==']
        if ctx.message.author.id != 705462972415213588:
            for x in blocked_words:
                if x in body:
                    return await ctx.send('Your code contains certain blocked words.')
        env = {
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            'source': inspect.getsource,
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()
        err = out = None

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        def paginate(text: str):
            last = 0
            pages = []
            for curr in range(0, len(text)):
                if curr % 1980 == 0:
                    pages.append(text[last:curr])
                    last = curr
                    appd_index = curr
            if appd_index != len(text)-1:
                pages.append(text[last:curr])
            return list(filter(lambda a: a != '', pages))
        try:
            exec(to_compile, env)
        except Exception as e:
            err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
            return await ctx.message.add_reaction('\u2049')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            if ret is None:
                if value:
                    try: 
                        out = await ctx.send(f'```py\n{value}\n```')
                    except:
                        paginated_text = paginate(value)
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.send(f'```py\n{page}\n```')
                                break
                            await ctx.send(f'```py\n{page}\n```')
            else:
                self.client._last_result = ret
                try:
                    out = await ctx.send(f'```py\n{value}{ret}\n```')
                except:
                    paginated_text = paginate(f"{value}{ret}")
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')

        if out:
            await ctx.message.add_reaction('\u2705')
        elif err:
            await ctx.message.add_reaction('\u2049')
        else:
            await ctx.message.add_reaction('\u2705')

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def trivia(self, ctx, difficulty:str=None):
        self.log(f"{self.gettime()}{ctx.author} executed {ctx.command}")
        userdat[str(ctx.message.author.id)][17] += 1
        self.save()
        p = HTMLParser()
        parser = HTMLParser()
        if difficulty == None: r = requests.get("https://opentdb.com/api.php?amount=50&type=multiple")
        else: r = requests.get(f"https://opentdb.com/api.php?amount=50&type=multiple&difficulty={difficulty}")
        if r.json()["response_code"] != 0: return await ctx.reply(f"{difficulty} is an invalid difficulty")
        rnd = random.choice(r.json()["results"])
        question = p.unescape(rnd["question"])
        rnd["correct_answer"] = parser.unescape(rnd["correct_answer"])

        for i in rnd["incorrect_answers"]:
            rnd["incorrect_answers"][rnd["incorrect_answers"].index(i)] = parser.unescape(rnd["incorrect_answers"][rnd["incorrect_answers"].index(i)])

        arr = list()
        arr.append(rnd["correct_answer"])
        for i in rnd["incorrect_answers"]:
            arr.append(i)
        random.seed(random.randint(1, 256))
        random.shuffle(arr)
        a = arr[0]
        b = arr[1]
        c = arr[2]
        d = arr[3]
        if rnd["difficulty"] == "easy": timeout = 20
        elif rnd["difficulty"] == "medium": timeout = 30
        elif rnd["difficulty"] == "hard": timeout = 40
        embed = discord.Embed(
            title=f'{question}',
            description=f'\nCategory: {rnd["category"]}\nDifficulty: {rnd["difficulty"]}\nAnswers:\nA) {a}\nB) {b}\nC) {c}\nD) {d}\n\nTime: {timeout} seconds',
            color=discord.Color.random()
        )
        embed.set_footer(text=f"Trivia system made by {owner}")
        await ctx.send(embed=embed)
        def check(msg):
            return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)
        try:
            msg = await self.client.wait_for("message", check=check, timeout=timeout)
        except:
            return await ctx.send(f'You ran out of time! The correct answer was {rnd["correct_answer"]}')
        if msg.content.lower() == "a" or msg.content.lower() == a.lower():
            if a == rnd["correct_answer"]:
                if rnd["difficulty"] == "easy": coins = random.randint(100, 1000)
                elif rnd["difficulty"] == "medium": coins = random.randint(2000, 5000)
                elif rnd["difficulty"] == "hard": coins = random.randint(5000, 10000)
                userdat[str(ctx.message.author.id)][0] += coins
                self.save()
                await ctx.send(f"Correct! You earned {coins} coins")
            else:
                return await ctx.send(f'Incorrect! The answer was \"{rnd["correct_answer"]}\"')
        elif msg.content.lower() == "b" or msg.content.lower() == b.lower():
            if b == rnd["correct_answer"]:
                if rnd["difficulty"] == "easy": coins = random.randint(100, 1000)
                elif rnd["difficulty"] == "medium": coins = random.randint(2000, 5000)
                elif rnd["difficulty"] == "hard": coins = random.randint(5000, 10000)
                userdat[str(ctx.message.author.id)][0] += coins
                self.save()
                await ctx.send(f"Correct! You earned {coins} coins")
            else:
                return await ctx.send(f'Incorrect! The answer was \"{rnd["correct_answer"]}\"')
        elif msg.content.lower() == "c" or msg.content.lower() == c.lower():
            if c == rnd["correct_answer"]:
                if rnd["difficulty"] == "easy": coins = random.randint(100, 1000)
                elif rnd["difficulty"] == "medium": coins = random.randint(2000, 5000)
                elif rnd["difficulty"] == "hard": coins = random.randint(5000, 10000)
                userdat[str(ctx.message.author.id)][0] += coins
                self.save()
                await ctx.send(f"Correct! You earned {coins} coins")
            else:
                return await ctx.send(f'Incorrect! The answer was \"{rnd["correct_answer"]}\"')
        elif msg.content.lower() == "d" or msg.content.lower() == d.lower():
            if d == rnd["correct_answer"]:
                if rnd["difficulty"] == "easy": coins = random.randint(100, 1000)
                elif rnd["difficulty"] == "medium": coins = random.randint(2000, 5000)
                elif rnd["difficulty"] == "hard": coins = random.randint(5000, 10000)
                userdat[str(ctx.message.author.id)][0] += coins
                self.save()
                await ctx.send(f"Correct! You earned {coins} coins")
            else:
                return await ctx.send(f'Incorrect! The answer was \"{rnd["correct_answer"]}\"')
        else:
            return await ctx.send(f'What is {msg.content}? Anyway the correct answer was \"{rnd["correct_answer"]}\"')
### Commands end ###

def setup(client):
    client.add_cog(ErrorHandler(client))
    client.add_cog(Music(client))
    client.add_cog(MainCog(client))
