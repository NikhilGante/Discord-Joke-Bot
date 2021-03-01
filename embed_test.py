import discord
from discord.ext import commands
import csv
from User_ID import User_ID, bot_Token
import random

client = commands.Bot(command_prefix = "--")

bot_testing_channel = client.get_channel(802791468279398411)
myDict = [{"yo": "ayy", "pog": "moshup", "shorty": "bom"}, 
{"yo": "toronto", "pog": "man", "shorty": "eh"}, 
{"yo": "more", "pog": "life", "shorty": "drake"},
]

async def pp():
    Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    for row in myDict:
        Embed.add_field(name = "ayo ", value = f"{row['yo']}\t\t\t\t {row['pog']}\t{row['shorty']}", inline = False)

    await bot_testing_channel.send(embed = Embed)        

await pp()

client.run(bot_Token)   # botID is privatized