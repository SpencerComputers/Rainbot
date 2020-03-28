import discord
import os
import json
from discord.ext import commands

dclient = commands.Bot(command_prefix="-", status=discord.Status.idle, activity=discord.Game(name="Starting.."))

# ==== vvv you were working on this vvv
config = json.load(
    open("./config.json", "r")
)
# ==== ^^^ you were working on this ^^^

@dclient.event
async def on_ready():
    print("Loading modules..")
    print(f"Now serving {len(bot.guilds)} guilds.")

@dclient.command
async def load(ctx, extension)
    client.load_extension(f'cogs.{extension}')
    ctx.send(f'**{extension}** has been loaded.')
    print(f'{ctx.message.author} has loaded {extension}.')
    
@dclient.command
async def unload(ctx, extension)
    client.unload_extension(f'cogs.{extension}')
    ctx.send(f'**{extension}** has been unloaded.')
    print(f'{ctx.message.author} has unloaded {extension}.')
    
for filename in os.listdir('./plugins'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
client.run("TOKEN")