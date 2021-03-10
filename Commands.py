# bot.py
import os
import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
from googlesearch import search
from Bot import install_emotes
import urllib.request
import requests

class MyCommands(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member):
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')


    @commands.command(name="Age")
    async def age(self,ctx):
        await ctx.send("22")

    #  Join VC and Leave VC
    @commands.command(name="Join")
    async def JoinVC(self,ctx):
        connected = ctx.author.voice
        if connected:
            await connected.channel.connect()

    @commands.command(name="Leave")
    async def LeaveVC(self,ctx):
        await ctx.voice_client.disconnect();


    # Adding and Removing Roles
    @commands.command(pass_context=True)
    async def giverole(self,ctx, user: discord.Member, role: discord.Role):
        await user.add_roles(role)

    @commands.command(pass_context=True)
    async def removerole(self,ctx, user:discord.Member, role:discord.Role):
        await user.remove_roles(role)

    # Purge Command
    @commands.command(name="Purge")
    @commands.has_permissions(manage_messages=True)
    async def Purge(self,ctx,amount:int):
        await ctx.channel.purge(limit = amount)
        await ctx.send('Done!')


    # Google Search 
    @commands.command(name="Search")
    async def Search(self,ctx,*,query):
        for x in search(query,tld="co.in", num=1, stop=1, pause=1):
            await ctx.send(x)


    # To take an emoji
    @commands.command(name="Steal")
    @commands.has_permissions(manage_emojis=True)
    async def Steal(self,ctx,message,name):
        from urllib.request import urlopen, Request
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        req = Request(url=message,headers=headers)
        response = urlopen(req)
        filename = message.split('/')[-1]
        with open(filename,"wb") as f:
            f.write(response.read())
            await install_emotes(ctx, {
            "title": name,
            "image": message,
            "filename":filename
            }, success_message ="Uploaded!")
        os.remove(filename)
        

def setup(bot):
    bot.add_cog(MyCommands(bot))