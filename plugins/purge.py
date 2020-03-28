# A purge command that allows you to quickly remove a specified amount of messages       
import discord
from discord.ext import commands

class Moderation(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.cog.listener()
    async def on_ready(self):
        print('Purge module has been loaded.')
        
# =================
    @commands.command(pass_context=True)
    async def purge(self, ctx, amount=100):
        channel = ctx.message.channel
        messages = []
        async for message in client.logs_from(channel, limit=int(amount)):
            messages.append(message)
        await client.delete_messages(messages)
        embed_purge = discord.Embed(Title='Boom 💥', description=f'{ctx.message.author} has purged {amount} message(s).', color=0xf76d23)
        await ctx.send(embed_purge)
# =================   

def setup(client):
    client.add_cog(Moderation(client))
