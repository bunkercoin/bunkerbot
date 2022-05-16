import discord
from discord.ext import commands

token = ''
bot = commands.Bot(command_prefix='>')

# ping command, used to see how sucky my internet is 
@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is: {round (bot.latency * 1000)} ms')

# bunkerinfo commnand, used to see information about bunkercoin, fancy embed!!
@bot.command()
async def bunkerinfo(ctx):
    embed=discord.Embed(title="Bunkercoin info")
    embed.add_field(name="undefined", value="undefined", inline=False)
    await ctx.send(embed=embed)

# Start the bot
bot.run(token)