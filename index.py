import discord
from discord.ext import commands
import logging
import json
f = open("/home/mysteri0us/Documents/Some-work-i-guess/testbot/config.json")
data = json.load(f)
Prefix = data['prefix']
from discord.ext.commands.errors import MissingRequiredArgument


intents = discord.Intents.all()
client = discord.Client()
bot = commands.Bot(command_prefix=Prefix, intents=intents)
bot.remove_command('help')
bot.remove_command('kick')

# cogs
initialExtension = ['cogs.general',
                    'cogs.Help',
                    'cogs.mod',
                    'cogs.meme']
if __name__ == '__main__':
    for extension in initialExtension:
        bot.load_extension(extension)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@client.event
async def on_ready():
    print ("Booting up your system")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command()
async def test(ctx,*, arg=None):
    """Test command, repeats what you say"""
    if arg is None:
        await ctx.send("You missed a important argument!")
    else:
        await ctx.channel.send(arg)

def to_upper(argument):
    return argument.upper()

@bot.command()
async def up(ctx, *, content: to_upper=None):
    """Converts your message to uppercase"""
    if content is None:
        await ctx.send("You missed a important argument!")
    else:  
        await ctx.send(to_upper(content))

@bot.command()
async def whoami(ctx):
    """Preaches your name!"""
    author = ctx.author
    send_text = "You are " + str(author)
    await ctx.send(send_text)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

bot.run(data['token'])
