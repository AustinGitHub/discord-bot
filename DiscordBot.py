# bot.py
import os
import discord
import dotenv
from dotenv import load_dotenv
from discord.ext import commands, tasks
import traceback

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$',intents = intents)

extensions = ['Commands','Calculator']

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):
        channel = bot.get_channel(815639899365572671)
        await channel.send('Welcome! ' +member.mention)
        role = discord.utils.get(member.guild.roles,name="test")
        await member.add_roles(role)




bot.run(TOKEN)