import discord
from discord.ext import commands
from discord.utils import get

import json
import os
import random

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
  print("The church has opened...")
  
@bot.event
async def on_resume():
  print("Tom is back from lunch break")
  
@bot.event
async def on_message(message):
  pass
  
@bot.event
async def on_member_join(member):
  pass
  
@bot.event
async def on_member_leave(member):
  pass
  
  
@bot.command()
async def verse(ctx):
  pass



bot.run("TOKEN")
