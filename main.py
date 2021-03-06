import logging
import requests
import discord
from discord.ext import commands

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# 'Settings'
api = "https://api.bunkercoin.xyz"
token = '' # Message to self: DELETE THIS WHEN COMMITING!!

bot = commands.Bot(command_prefix='>')

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found. Type `>help` for a list of commands.')
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send('If you got this error it probably means that there is nothing to snipe. Try again later.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to use this command.')

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

# >music command, play "troll.mp3" in a voice channel
@bot.command()
async def music(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send("You need to be in a voice channel to use this command")
    else:
        voice_client = await voice_channel.connect()
        voice_client.play(discord.FFmpegPCMAudio("troll.mp3"))

# Make the bot leave the voice channel
@bot.command()
async def leave(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send("You need to be in a voice channel to use this command")
    else:
        server = ctx.message.guild.voice_client
        await server.disconnect()

# ban command, allows only administrators to ban users
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

# Start the bot
bot.run(token)
