import discord
from discord.ext import commands
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("The Bot Is Ready")

@client.event
async def on_member_join(member):
    print("A member has joined a server")

@client.event
async def on_member_remove(member):
    print("A member has left a server")

client.run("TOKEN HERE")