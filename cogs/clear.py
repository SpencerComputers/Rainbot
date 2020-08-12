import discord
from discord.ext import commands

# Cogs - Ignore
class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
# ================================

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title='Boom 💥', description=f'Successfully cleared **{amount}** messages.', color=0xf5a12c)
        await ctx.send(embed=embed)

# Cogs - Ignore
def setup(client):
    client.add_cog(Example(client))
# ================================