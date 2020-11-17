import discord
from discord import client
from discord import message
from discord.ext import commands
from discord.ext.commands.core import command



class Handler(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_command_error(self, ctx, e):
        if isinstance(e, commands.MissingRequiredArgument):
            await ctx.message.delete()
            await ctx.message.author.send("Missing required arguements!")
        elif isinstance(e, commands.BotMissingPermissions):
            await ctx.send("I am missing permissions!")
        elif isinstance(e, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.message.author.send("You do not have permissions!")
        elif isinstance(e, commands.MissingAnyRole):
            await ctx.send("Missing Required Role")
        elif isinstance(e, commands.MemberNotFound):
            await ctx.send("Member not Found")
        elif isinstance(e, commands.BadArgument):
            await ctx.send("Bad Arguement")
        elif isinstance(e, commands.ConversionError):
            await ctx.send("Please enter a number")
        elif isinstance(e, commands.CommandNotFound):
            await ctx.send(e)        
        else:
            await ctx.send(f'Unexpected error, {e}')

def setup(client):
    client.add_cog(Handler(client))