import discord
from discord.ext import commands
import os
import dotenv
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='/', intents=intents)

load_dotenv()
TOKEN = os.getenv("TOKEN")


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def slash(ctx):
    await ctx.respond("hello father")
    print("worked")

@bot.command()
async def hellotest(ctx):
    await ctx.send("hiii")
    print("worked")

@bot.command()
async def guh(ctx):
    await ctx.send("kys")
    print("worked")

bot.run(TOKEN)