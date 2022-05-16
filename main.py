import requests
import discord
from discord.ext import commands

# "Settings"
api = "https://api.bunkercoin.xyz"
token = ''

# Prefix
bot = commands.Bot(command_prefix='>')

# Get blockcount from the api
def bkcblockcount():
    url = requests.get(api + '/blockcount')
    parsedblockcount = url.json()
    return parsedblockcount['result']['blockcount']

# ping command, used to see how sucky my internet is 
@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is: {round (bot.latency * 1000)} ms')

# bunkerinfo commnand, used to see information about bunkercoin, fancy embed!!
@bot.command()
async def bunkerinfo(ctx):
    embed=discord.Embed(title="Bunkercoin info")
    embed.add_field(name="Blockcount:", value=bkcblockcount(), inline=False)
    await ctx.send(embed=embed)

# Start the bot
bot.run(token)