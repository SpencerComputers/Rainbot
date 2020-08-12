import discord
from discord.ext import commands

# Cogs - Ignore
class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
# ================================

    @commands.command()
    async def on_member_remove(self, member):
        print(f'{member} has been removed from server')
        embed = discord.Embed(title='Goodbye 😢', description=f'{member} has just left the server', color=0xf5a12c)
        await ctx.send(embed=embed)

# Cogs - Ignore
def setup(client):
    client.add_cog(Example(client))
# ================================