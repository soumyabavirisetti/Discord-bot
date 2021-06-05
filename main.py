import os
import discord
from discord.ext import commands
import youtube_dl
import infowiki as iw
import calc
import datentime as dt
import asciiimg as ai
import qcode
import getytlink
import random

client = commands.Bot(command_prefix="^")

greeting_input = ["hello","hi","hey","Hello","Hi","Hey"]

greeting_words = ["Hey there!","Hello there! How may I help you?","Hi","Hello there! What would you like me to do?","Hello"]

thankyou_input = ["thanks","thank you","thank you very much","thank you so much","thank you very very much","thank"]

thankyou_words = ["My pleasure 😊","I aim to please 😌","You're welcome","I'm here to help,please let me know if you need anything else 😀✨"]

@client.command()
async def info(ctx, *text):
  msg = " ".join(list(text))
  x = iw.send_summary(msg)
  await ctx.channel.send(x)

@client.command()
async def qrcode(ctx, url):
  qcode.retqr(url)
  await ctx.channel.send(file=discord.File('qrcode.png'))
  os.remove('qrcode.png')

@client.command()
async def draw(ctx, url):
  y = ai.asmain(url)
  file1 = open("ascii_img.txt", "w")
  file1.write(y)
  file1.close()
  await ctx.channel.send(file=discord.File('ascii_img.txt'))
  os.remove('ascii_img.txt')

@client.command()
async def calculate(ctx, text):
  y = calc.compute(text)
  await ctx.channel.send(y)

@client.command()
async def date(ctx):
  y = dt.find_date()
  await ctx.channel.send("Today's date is "+y)

@client.command()
async def time(ctx):
  y = dt.find_time()
  await ctx.channel.send("Current time is " + y)

@client.command()
async def year(ctx):
  y = dt.find_year()
  await ctx.channel.send("Present year is " + y)

@client.command()
async def month(ctx):
  y = dt.find_month()
  await ctx.channel.send("Present month is " + y)

@client.command()
async def day(ctx):
  y = dt.find_day()
  await ctx.channel.send("Today is " + y)

@client.command()
async def connect(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def play(ctx, *name : str):
    url = getytlink.geturl(list(name))
    print(url)
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.channel.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.channel.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.channel.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

@client.command(pass_context = True, aliases = greeting_input)
async def greet(ctx):
    await ctx.channel.send(random.choice(greeting_words) + " " + str(ctx.author.mention))

@client.command(pass_context = True, aliases = thankyou_input)
async def thankyou(ctx):
    await ctx.channel.send(random.choice(thankyou_words))





client.run("TOKEN")
