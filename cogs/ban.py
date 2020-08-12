import discord
from discord.ext import commands

# Cogs - Ignore
class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
# ================================

    @commands.command()
    async def ban(ctx, member : discord.Member, *, reason='No reason specified'):
        await member.kick(reason=reason)
        embed = discord.Embed(title='Banned 🚫', description=f'Successfully banned **{member}**!', color=0xf5a12c)
        await ctx.send(embed=embed)

# Cogs - Ignore
def setup(client):
    client.add_cog(Example(client))
# ================================