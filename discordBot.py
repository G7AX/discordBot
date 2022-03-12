import discord
from discord.ext import commands
from random import choice
from os import listdir
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])# символ после которого бот будет реагировать на команду

@bot.event
async def on_ready():# проверка включился ли бот
    print('Bot connected')

@bot.command()# включает prefix для бота
async def repeat(ctx, arg):# !repeat повтор введённого сообщения
    await ctx.message.delete()
    author = ctx.message.author
    await ctx.send(f" { author.mention } " + arg)

@bot.command()
async def img(ctx):
    await ctx.message.delete()
    path = open('pathToPictures.txt', 'r').readline()
    files = listdir(path)
    author = ctx.message.author
    randomizer = choice(files)
    await ctx.channel.send(f'{author.mention}Держи', file=discord.File(f'{path}{randomizer}', spoiler=False))# Если хочешь, чтобы не было на пикче "спойлер. Удали ", spoiler=True"

@bot.command()
async def clear(ctx, amountOfMessages = 100):
    await ctx.channel.purge(limit=amountOfMessages)


#-------------------------------------------------------------------------------------------------------------
bot.run(settings['token']) #токен бота
# 856526851450339331 id "общее"