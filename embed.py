# An embed command that allows you to create custom and rich embeds    
import discord
from discord.ext import commands

class Fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.cog.listener()
    async def on_ready(self):
        print('Embed module has been loaded.')
        
# =================
    @commands.command(pass_context=True)
    async def embed(self, ctx, *, a_sMessage):
        color = None
        thumb = None
        embed_colour = discord.Embed(Title='🌈 Colours!', description='Would you like your embed to display with a **custom colour**? If so, __say the colour in chat__, if not say, __no__', color=0xf76d23)
        embed_color.set_footer(text="RainBot")
        embed_thumbnail = discord.Embed(Title='🖼️ Thumbnail!', description='Would you like your embed to have a custom thumbnail? If so, __send the link to the image here__, if not, just say __no__', color=0xf76d23)
        embed_thumbnail.set_footer(text="Rainbot")
        await ctx.message.delete(ctx.message)
        ques1 = await ctx.send(embed=embed_color)
        ques1
        def check(message):
            return message.author == original_author
        msg = await bot.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == "green":
            await ctx.message.delete(ques1)
            await ctx.message.delete(msg)
            color = 0x00ff00
            ques2 = await ctx.send(embed=embed_thumb)
            ques2
        elif msg.content.lower() == "yellow"
            await ctx.message.delete(ques1)
            await ctx.message.delete(msg)
            color = 0xFFFF00
            ques2 = await ctx.send(embed=embed_thumb)
            ques2
        elif msg.content.lower() == "blue"
            await ctx.message.delete(ques1)
            await ctx.message.delete(msg)
            color = 0x0000ff
            ques2 = await ctx.send(embed=embed_thumb)
            ques2
        elif msg.content.lower() == "red"
            await ctx.message.delete(ques1)
            await ctx.message.delete(msg)
            color = 0xff0000
            ques2 = await ctx.send(embed=embed_thumb)
            ques2
        else:
            await ctx.message.delete(ques1)
            await ctx.message.delete(msg)
            color = 0xf76d23
            ques2 = await ctx.send(embed=embed_thumb)
            ques2
            def check(message):
            return message.author == original_author
        if msg.content.lower() == "no":
            await ctx.message.delete(ques2)
            await ctx.message.delete(msg)
            thumb = https://i.imgur.com/S6Rl8xL.png
        else:
            await ctx.message.delete(ques2)
            await ctx.message.delete(msg)
            thumb = msg.content
        embed = discord.Embed(description=a_sMessage, color=color)
        embed.set_thumbnail(url=thumb)
        embed.set_author(name=ctx.message.author)
        embed.set_footer(text='RainBot!')
        await ctx.message.delete(ctx.message)
        await ctx.send(embed=embed)
        print(f'{ctx.message.author} has just embedded a message.'
# =================   

def setup(client):
    client.add_cog(Fun(client))