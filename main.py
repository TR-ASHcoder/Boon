import discord 
from discord.ext import commands
from discord import option
from typing import Union
import os 
import time 


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='t.', intents=intents)
bot = commands.Bot()



@bot.slash_command()
@option("testtt", description="Enter your name")
async def slash(ctx):
    
    await ctx.respond("hello father ")
    print("worked")

@bot.command()
async def hellotest(ctx):
    await ctx.send("hiii")
    print("worked")
    
    
@bot.command()
async def guh(ctx):
    await ctx.send("kys")
    print("worked")

bot.run('MTA3Mjk4MTQyNzUwNDgxMjA1Mg.Gzi7Mt.A3BsTBbU0gF9uhVsDtN_pPxSsx53jLUHj2eCOk')