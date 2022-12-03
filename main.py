import discord, json
from colorama import init, Fore, Back, Style
from discord import app_commands
from discord.ext import commands

init(autoreset=True)
client = commands.Bot(intents = discord.Intents.all())

@client.event
async def on_ready():
    print(Fore.GREEN + "  Logged in!")
    print(Fore.CYAN + f"• Name:" + Fore.WHITE + f"{client.user.name}")
    print(Fore.CYAN + f"• User ID:" + Fore.WHITE + f"{client.user.id}")
    synced = await client.tree.sync()
    print(Fore.CYAN + "• Synced " + Fore.WHITE + f"{len(synced)}" + Fore.CYAN + " command(s)")
    print(Fore.GREEN + 'Bot is ready ')
    print(Fore.YELLOW +'------')

client.run("NTMwODk5MDE1ODk4NzU5MTk5.GObcqh.xgxuJdH609ObccK5MAM8l69LLYaNHgg2cQLD5c")