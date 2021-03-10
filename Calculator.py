# bot.py
import os
import discord
from discord.ext import commands

class MyCalculator(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="Add")
    async def Add(self,ctx,input1:int,input2:int):
            result = input1 + input2
            await ctx.send(result)
    
    @Add.error
    async def add_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please use the correct inputs. Usage: $Add <number> <number>')


def setup(bot):
    bot.add_cog(MyCalculator(bot))