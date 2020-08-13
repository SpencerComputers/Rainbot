import discord
import random
import os, json
from discord.ext import commands

client = commands.Bot(command_prefix = '-')

@client.event #on ready
async def on_ready():
    print('Bot is ready!')

@client.command() #load cog
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'): #load cogs auto
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command() #unload cog
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

client.run("nice one dickhead")
