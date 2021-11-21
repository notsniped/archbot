import discord
from discord.ext import *
from discord.ext.commands import *

snipe_message_author = {}
snipe_message_content = {}

class Events(commands.Cog):
    def __init__(self, client : commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
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

def setup(client):
    clent.add_cog(Events(client))
