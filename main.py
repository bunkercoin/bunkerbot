import requests
import discord
from discord.ext import commands

# 'Settings'
api = "https://api.bunkercoin.xyz"
token = '' # Message to self: DELETE THIS WHEN COMMITING!!

bot = commands.Bot(command_prefix='>')

# Get blockcount from the api
def bkcblockcount():
    url = requests.get(api + '/blockcount')
    parsedblockcount = url.json()
    return parsedblockcount['result']['blockcount']

# Get network hashrate from the api
def bkcnetworkhashrate():
    url = requests.get(api + '/hashrate')
    parsedblockcount = url.json()
    return parsedblockcount['result']['hashrate']

# Get difficulty from the api
def bkcdifficulty():
    url = requests.get(api + '/diff')
    parsedblockcount = url.json()
    return parsedblockcount['result']['difficulty']
    
# ping command, used to see how sucky my internet is 
@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is: {round (bot.latency * 1000)} ms')

# bunkerinfo commnand, used to see information about bunkercoin, fancy embed!!
@bot.command()
async def bunkerinfo(ctx):
    embed=discord.Embed(title="Bunkercoin chain info", color=0x99c1f1)
    embed.add_field(name="Bunkercoin blockcount", value=bkcblockcount(), inline=False)
    embed.add_field(name="Bunkercoin network hashrate", value=bkcnetworkhashrate() + " H/s", inline=False)
    embed.add_field(name="Bunkercoin difficulty", value=bkcdifficulty(), inline=False)
    await ctx.send(embed=embed)

# snipe comamnd, used to see the last deleted message
@bot.event
async def on_message_delete(message):
    global author
    author = str(message.author)
    global channel 
    channel = str(message.channel)
    global msg
    msg = str(message.content)
    
@bot.command()
async def snipe(ctx):
    embed=discord.Embed(title="Sniped message", description="from " + channel, color=0x99c1f1)
    embed.add_field(name=msg, value="Message from " + author, inline=False)
    embed.set_footer(text="cry about it")
    await ctx.send(embed=embed)



# Start the bot
bot.run(token)
