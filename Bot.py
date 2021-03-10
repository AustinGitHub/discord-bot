import discord
import os
import requests
import shutil
from discord.ext import commands

async def install_emotes(ctx, emoji_json,success_message: str = None, uploaded_by: discord.Member = None):
	# response = requests.get(emoji_json["filename"], stream = True)
	# print(response)
	# print(emoji_json)
	# if response.status_code == 200:
	# 	with open(f"/{emoji_json['filename']}","wb") as img:
	# 		response.raw.decode_content = True
	# 		shutil.copyfileobj(response.raw, img)
	# else:
	# 	raise Exception(f"Error")
	print(emoji_json)
	with open(f"{emoji_json['filename']}","rb") as image:
		if isinstance(ctx, discord.Guild):
			new_emoji = await ctx.create_custom_emoji(name=emoji_json['title'],image= image.read())
		else:
			new_emoji = await ctx.message.guild.create_custom_emoji(name=emoji_json['title'], image = image.read())

	return new_emoji
