# A ping command that allows you to see the bot's latency.       
import discord
from discord.ext import commands

class Basic(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.cog.listener()
    async def on_ready(self):
        print('Ping module has been loaded.')

# =================         
    @commands.command()
    async def ping(self, ctx):
        ping_ = bot.latency
        ping = round(ping_ * 1000)
        embed_ping = discord.Embed(title='Ping Pong 🏓', description=f'My current ping is {ping}ms', color=0xf76d23)
        await ctx.send(embed=embed_ping)
# =================    
                       
def setup(client):
    client.add_cog(Basic(client))
