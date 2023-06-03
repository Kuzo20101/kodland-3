import discord
from discord.ext import commands
from bot_mantik1 import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has joined!')

@bot.command()
async def karbonayakizi(ctx):
    await ctx.send(atik())


bot.run('MTEwNjg3MzMyOTc5NDY3ODc5NA.G6DQhj.b_M0O0W0wLUFlrXd5fgjJLQW9BrhyIraB9DbRc')