import discord
from discord.ext import commands

# Cogs - Ignore
class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
# ================================

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined server.')
        embed = discord.Embed(title='Welcome 👋', description=f'Welcome to the server, {member}', color=0xf5a12c)
        await ctx.send(embed=embed)

# Cogs - Ignore
def setup(client):
    client.add_cog(Example(client))
# ================================