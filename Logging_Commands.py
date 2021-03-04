import discord
from discord.ext import commands
from Database import Insults, PP_Length, Jokes, Quotes, max_len
import Database
import random
import csv
from Miscellaneous import client

# -------------------------- INSULTS SECTION --------------------------  

@client.command()
async def erase_all_insults(context):
    await Insults.erase_all(context)

@client.command(aliases = ["ei"])
async def erase_insult(context, index):
    await Insults.erase(context, index)

@client.command(aliases = ["si", "show insults"])
async def show_insults(context):
    await Insults.show(context)

@client.command(aliases = ["ri", "random insult"])
async def random_insult(context, user: discord.Member = None):
    await Insults.random(context, user)

@client.command(aliases = ["gi", "get insult"])
async def get_insult(context, index, user: discord.Member = None):
    await Insults.get(context, index, user)

# -------------------------- JOKES SECTION --------------------------  

@client.command()
async def erase_all_jokes(context):
    await Jokes.erase_all(context)

@client.command(aliases = ["ej"])
async def erase_joke(context, index):
    await Jokes.erase(context, index)

@client.command(aliases = ["sj", "show jokes"])
async def show_jokes(context):
    await Jokes.show(context)

@client.command(aliases = ["rj", "random joke"])
async def random_joke(context, user: discord.Member = None):
    await Jokes.random(context, user)

@client.command(aliases = ["gj", "get joke"])
async def get_joke(context, index, user: discord.Member = None):
    await Jokes.get(context, index, user) 

# -------------------------- QUOTES SECTION --------------------------  

@client.command()
async def erase_all_quotes(context):
    await Quotes.erase_all(context)

@client.command(aliases = ["eq"])
async def erase_quote(context, index):
    await Quotes.erase(context, index)

@client.command(aliases = ["sq", "show quotes"])
async def show_quotes(context):
    await Quotes.show(context)

@client.command(aliases = ["rq", "random quote"])
async def random_quote(context, user: discord.Member = None):
    await Quotes.random(context, user)

@client.command(aliases = ["gq", "get quote"])
async def get_quote(context, index, user: discord.Member = None):
    await Quotes.get(context, index, user)

# -------------------------- PP_LENGTH SECTION --------------------------  

@client.command(aliases = ["ps", "ppsize", "peepee size"])
async def peepee_size(context):
    size = Database.truncate(random.uniform(0, 10), 2)
    author = str(context.author)
    finalStr = (f"{author}'s peepee is {size} inches long.\n")
    if size > 5:
        finalStr += "What a damn Chad."
    elif size < 3:
        finalStr += "I got some viagra bro, if you ever need it."
    else:
        finalStr += "Ayo same."
    await context.send(finalStr)
    
    PP_Length.download_data()
    PP_Length.upload_data()
    PP_Length.add_entry(author, size)

@client.command(aliases = ["gr", "get rank"])
async def get_rank(context, amount = 0):
    await PP_Length.get_rank(context, amount)

@client.command(aliases = ["r"])
async def rank(context, user: discord.Member = None, amount = 0):
    await PP_Length.rank(context, amount, user) # arguments are ordered differently for a reason
