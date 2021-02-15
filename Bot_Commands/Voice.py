import discord
from discord.ext import commands
import youtube_dl
import os
from Bot_Commands.Miscellaneous import client


@client.command(aliases = ["j"])
async def join(context):
    voiceChannel = discord.utils.get(context.guild.voice_channels, name = 'Memers')
    await voiceChannel.connect()

@client.command(aliases = ["l"])
async def leave(context):
    voice = discord.utils.get(client.voice_clients, guild = context.guild)
    if voice.connected():
        voice.disconnect()
    else:
        await context.send("Innovirus.exe is not currently connected to a voice channel.")

@client.command()
async def pause(context):
    voice = discord.utils.get(client.voice_clients, guild = context.guild)
    if voice.is_playing:
        voice.pause()
    else:
        await context.send("Innovirus.exe is not currently playing audio.")

@client.command()
async def resume(context):
    voice = discord.utils.get(client.voice_clients, guild = context.guild)
    if voice.is_paused:
        voice.resume()
    else:
        await context.send("Innovirus.exe audio is not paused.")

@client.command()
async def stop(context):
    voice = discord.utils.get(client.voice_clients, guild = context.guild)
    voice.stop()

@client.command(aliases = ["p"])
async def play(context, url : str):

    try:
        if os.path.isfile("song.mp3"):  # if song file exists
            os.remove("song.mp3")
    except PermissionError:
        await context.send("Wait for the current playing music to end or use the 'stop' command")
        return

    await join(context)
    voice = discord.utils.get(client.voice_clients, guild = context.guild)

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
async def Insult_Innovire(context, url : str):
    join(context)
    voiceChannel = discord.utils.get(context.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild = context.guild)
    voice.play(discord.FFmpegPCMAudio("Insult_Innovire.mp3"))
