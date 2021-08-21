import discord
from discord.ext import commands
from discord.ext.commands import bot
import requests
# import urllib
import json
import asyncio

file = open("/home/mysteri0us/Documents/Some-work-i-guess/testbot/cogs/meme.json")
jsonData = json.load(file)

def getMeme(id, text0, text1):
    data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
    images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]
    # List all the memes
    # print('Here is the list of available memes : \n')
    # ctr = 1
    # for img in images:
    #     print(ctr,img['name'])
    #     ctr = ctr+1

    #Fetch the generated meme
    URL = 'https://api.imgflip.com/caption_image'
    params = {
        'username':jsonData['username'],
        'password':jsonData['password'],
        'template_id':images[id-1]['id'],
        'text0':text0,
        'text1':text1
    }
    response = requests.request('POST',URL,params=params).json()
    Rdata = response['data']
    imgURL = Rdata['url']
    return imgURL

class Meme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="drakeBetter")
    async def drakeBetter(self, ctx, text0, text1):

        jpgURL = getMeme(1, text0, text1)
        await ctx.send(jpgURL)
        # getMeme(1, )
        # await ctx.send()

def setup(bot):
    bot.add_cog(Meme(bot))