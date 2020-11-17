import discord
from discord.ext import commands
import json
import os


config = json.load(open("config.json"))

client = commands.Bot(command_prefix=config["prefix"], intents=discord.Intents.all())
for i in os.listdir('./scripts'):
    if i.endswith('.py'):
        client.load_extension(f'scripts.{i[:-3]}')






client.run(config["token"])
