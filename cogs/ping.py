import discord
from discord.ext import commands

# Cogs - Ignore
class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
# ================================

    @commands.command()
    async def ping(self, ctx):
        ping = client.latency
        ping_ = round(ping * 1000)
        embed = discord.Embed(title='Ping Pong 🏓', description=f'My ping came back as {ping}ms', color=0xf5a12c)
        await ctx.send(embed=embed)

# Cogs - Ignore
def setup(client):
    client.add_cog(Example(client))
# ================================