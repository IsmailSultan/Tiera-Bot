from os import terminal_size
import discord
from discord.ext import commands
import TenGiphPy
from discord.ext.commands.core import command
import json

f = open('/home/mysteri0us/Documents/Some-work-i-guess/testbot/config.json')
data = json.load(f)
# print(data)
botName = "Tiere"

tenorToken = data['tenorToken']
class Emotional(commands.Cog):
    """
    Emotional Gif Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='repeat', aliases=['copy', 'mimic'], description="A simple command which repeats your input.")
    async def do_repeat(self, ctx, *, our_input: str):
        """A simple command which repeats our input."""

        await ctx.send(our_input)

    @commands.command(name='hug', aliases=['cuddle'], description="Hug your friend.")
    async def hug(self, ctx, *, member: discord.member=None):
        """Hug a friend, and if you dont have any, i will hug you"""
        t = TenGiphPy.Tenor(token=tenorToken)
        tenorGif = t.random("animehug")
        GIF = tenorGif
        authot = str(ctx.author).split("#",1)

        if member is not None:
            mention = member
            name = str(mention).split("#",1)
            name = name[0]
            embedVar = discord.Embed(title=f"{authot[0]} hugs {name}.", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)
            
        elif member is None:
            name = "you"
            embedVar = discord.Embed(title=f"{authot[0]} hugs {botName}.", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)

    @commands.command(name='cry', aliases=['weep'])
    async def cry(self, ctx, *, member: discord.Member=None):
        """cry for someone"""
        t = TenGiphPy.Tenor(token=tenorToken)
        tenorGif = t.random("animecry")
        GIF = tenorGif
        authot = str(ctx.author).split("#",1)

        if member is not None:
            mention = member
            name = str(mention).split("#",1)
            name = name[0]
            embedVar = discord.Embed(title=f"{authot[0]} cries for {name}.", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)
            
        elif member is None:
            name = "you"
            embedVar = discord.Embed(title=f"{authot[0]} cries.", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)

    @commands.command(name='slap')
    async def slap(self, ctx, *, member: discord.Member=None):
        """slap someone you hate"""
        t = TenGiphPy.Tenor(token=tenorToken)
        tenorGif = t.random("animeslap")
        GIF = tenorGif
        authot = str(ctx.author).split("#",1)

        if member is not None:
            mention = member
            name = str(mention).split("#",1)
            name = name[0]
            embedVar = discord.Embed(title=f"{authot[0]} slapped {name}.", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)
            
        elif member is None:
            name = "you"
            embedVar = discord.Embed(title=f"{authot[0]} was slapped by {botName}", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)

    @commands.command(name='smile')
    async def smile(self, ctx, *, member: discord.Member=None):
        """wanna look attractive, say cheese!"""

        t = TenGiphPy.Tenor(token=tenorToken)
        tenorGif = t.random("animesmile")
        GIF = tenorGif
        authot = str(ctx.author).split("#",1)

        if member is not None:
            mention = member
            name = str(mention).split("#",1)
            name = name[0]
            embedVar = discord.Embed(title=f"{authot[0]} smiled at {name}.", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)
            
        elif member is None:
            name = "you"
            embedVar = discord.Embed(title=f"{authot[0]} smiles", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)


    @commands.command(name="kill", aliases=["murder", "obliterate"])
    async def kill(self, ctx, *, member: discord.Member=None):
        """It had to be DONE!"""

        t = TenGiphPy.Tenor(token=tenorToken)
        tenorGif = t.random("animekill")
        GIF = tenorGif
        authot = str(ctx.author).split("#",1)

        if member is not None:
            mention = member
            name = str(mention).split("#",1)
            name = name[0]
            embedVar = discord.Embed(title=f"{authot[0]} killed {name}.", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)
            
        elif member is None:
            name = "you"
            embedVar = discord.Embed(title=f"{authot[0]} was killed by {botName}", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)
    
    @commands.command(name="punch")
    async def punch(self, ctx, *, member: discord.Member=None):
        """Urusai!"""

        t = TenGiphPy.Tenor(token=tenorToken)
        tenorGif = t.random("animepunch")
        GIF = tenorGif
        authot = str(ctx.author).split("#",1)

        if member is not None:
            mention = member
            name = str(mention).split("#",1)
            name = name[0]
            embedVar = discord.Embed(title=f"{authot[0]} punched {name}.", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)
            
        elif member is None:
            name = "you"
            embedVar = discord.Embed(title=f"{authot[0]} was punched by {botName}", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)
    
    @commands.command(name="kck")
    async def kick(self, ctx, *, member: discord.Member=None):
        """Valyrian KICK!"""

        t = TenGiphPy.Tenor(token=tenorToken)
        tenorGif = t.random("animekick")
        GIF = tenorGif
        authot = str(ctx.author).split("#",1)

        if member is not None:
            mention = member
            name = str(mention).split("#",1)
            name = name[0]
            embedVar = discord.Embed(title=f"{authot[0]} kicked {name}.", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)
            
        elif member is None:
            name = "you"
            embedVar = discord.Embed(title=f"{authot[0]} was kicked by {botName}", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)

    @commands.command(name="blush")
    async def blush(self, ctx, *, member: discord.Member=None):
        """b-baka!"""

        t = TenGiphPy.Tenor(token=tenorToken)
        tenorGif = t.random("animeblush")
        GIF = tenorGif
        authot = str(ctx.author).split("#",1)

        if member is not None:
            mention = member
            name = str(mention).split("#",1)
            name = name[0]
            embedVar = discord.Embed(title=f"{authot[0]} started blushing because of {name}.", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)
            
        elif member is None:
            name = "you"
            embedVar = discord.Embed(title=f"{authot[0]} is blushing", description=f"", color=0x00ff00)
            embedVar.set_image(url=GIF)
            await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(Emotional(bot))