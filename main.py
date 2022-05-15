import discord
from discord.ext import commands

token = ''
bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is: {round (bot.latency * 1000)} ms')

# Start the bot
bot.run(token)