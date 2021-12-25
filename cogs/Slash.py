import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord.ext.commands import Cog
from discord_slash import SlashContext

client = commands.Bot

class Slash(Cog):
    def __init__(self, client : commands.Bot):
        self.client = client
    
    @cog_ext.cog_slash(
        name="test",
        description="amogus"
    )
    async def _test(self, ctx: SlashContext):
        await ctx.send(ctx.message.author_id)


def setup(client):
    client.add_cog(Slash(client))
