import discord
from discord.ext import commands
from Bot_Commands.Database import Insults, PP_Length, Jokes, Quotes
from Bot_Commands import Database
import random
import csv
from User_ID import User_ID
from Bot_Commands.Miscellaneous import client


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

    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Insults.data)
    # print(final_msg)

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

    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Jokes.data)
    # print(final_msg)

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
    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Quotes.data)
    # print(final_msg)

@client.command(aliases = ["rq", "random quote"])
async def random_quote(context, user: discord.Member = None):
    await Quotes.random(context, user)

@client.command(aliases = ["gq", "get quote"])
async def get_quote(context, index, user: discord.Member = None):
    await Quotes.get(context, index, user)

# -------------------------- PP_LENGTH SECTION --------------------------  

@client.command(aliases = ["ps", "ppsize", "peepee size"])
async def peepee_size(context):
    size =  Database.truncate(random.uniform(0, 10), 2)
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
    PP_Length.sort_data()
    amount = int(amount)
    data_rank = PP_Length.data
    if amount == 0: # if no user input, send all rows in database
        amount = len(data_rank)
    final_msg = "**Ranking:\t\t\tLength:\t\t\tOwner of PP:**" # adds header to message
    
    for row in range(amount):    # add rows to message
        final_msg += f"\n{data_rank[row][PP_Length.fieldnames[0]]}\t\t\t\t\t\t"\
        f" {data_rank[row][PP_Length.fieldnames[2]]}\t\t\t\t{data_rank[row][PP_Length.fieldnames[1]]}"

    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Insults.data)

    await context.send(final_msg)

@client.command(aliases = ["r"])
async def rank(context, user: discord.Member = None, amount = 0):
    PP_Length.sort_data()
    amount = int(amount)
    data_rank = PP_Length.data
    final_msg = "**Ranking:\t\t\tLength:**" # adds header to message

    user_sorted_rankings = [row for row in data_rank if row[PP_Length.fieldnames[1]] == str(user)]
    if amount == 0: # if no user input, send all rows for requested user in database
        amount = len(user_sorted_rankings)
    if amount > len(user_sorted_rankings):
        await context.send(f"You requested more than the available rankings for {user}."\
        f" There are {len(user_sorted_rankings)} available rankings for {user}.")
        return
    for row in range(amount):    # add rows to message
        final_msg += f"\n{user_sorted_rankings[row][PP_Length.fieldnames[0]]}\t\t\t\t\t\t"\
        f" {user_sorted_rankings[row][PP_Length.fieldnames[2]]}"

    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Insults.data)

    await context.send(final_msg)