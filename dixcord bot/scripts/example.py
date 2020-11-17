import discord
from discord.ext import commands
from main import client

class Handler(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Handler(client))