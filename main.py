from discord.ext import commands
import discord

bot = commands.Bot(command_prefix=",", status=discord.Status.idle, activity=discord.Game(name="Starting.."))

bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot has successfully booted with 0 errors!")
    print(f"Connected to {len(bot.guilds)} guilds.")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Ready to go!"))

@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send(f"I have a ping of {ping}ms 🏓")

@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "That user"
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joined_at
    role = member.top_role
    await ctx.channel.send(f"{pronoun} name is **{name}** and {pronoun} status is {status}. They joined at {joined}. They have the role {role}")

@bot.command()
async def ban(ctx, member:discord.User = None, reason = None):
    if member == ctx.message.author:
        await ctx.channel.send("**You cannot ban yourself 🚫**")
        return
    if member == None:
        await ctx.channel.send("**You must declare who you want to ban 🚫**")
        return 
    if reason == None:
        reason = "No reason provided"
    message = f"You've been banned from {ctx.guild.name} for {reason} 🔨"
    await member.send(message)
    await member.ban()
    await ctx.channel.send(f"{member} has been banned from the {ctx.guild.name} 🔨")

bot.run("NTMwODk5MDE1ODk4NzU5MTk5.Xn10BA.4RII2WlgE7-G2AS4TRcYFMeX028")