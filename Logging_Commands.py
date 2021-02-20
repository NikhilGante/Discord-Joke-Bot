import discord
from discord.ext import commands
from Database import Insults, PP_Length, Jokes, Quotes, max_len
import Database
import random
import csv
from User_ID import User_ID
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
    final_msg = "**Ranking:\t\t\tLength:\t\t\tOwner of PP:**" # adds header to message
    amount = int(amount)
    data_rank = PP_Length.data

    # if no user input, or input is more than what discord allows, send as many rows as discord allows
    if amount == 0:
        if len(PP_Length.data) > max_len:
            amount = max_len
        elif len(PP_Length.data) <= max_len:
            amount = len(PP_Length.data)
    elif amount > len(PP_Length.data):
        await context.send(f"You requested more than the available in database."\
        f" There are {len(PP_Length.data)} available rankings in database.")
        return
    elif amount > max_len:
        amount = max_len
    for row in range(amount):    # add rows to message
        final_msg += f"\n{data_rank[row][PP_Length.fn[0]]}\t\t\t\t\t\t"\
        f" {data_rank[row][PP_Length.fn[2]]}\t\t\t\t{data_rank[row][PP_Length.fn[1]]}"

    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Insults.data)
    # print(final_msg)

    await context.send(final_msg)

@client.command(aliases = ["r"])
async def rank(context, user: discord.Member = None, amount = 0):
    PP_Length.sort_data()
    amount = int(amount)
    final_msg = "**Ranking:\t\t\tLength:**" # adds header to message

    user_sorted_rankings = [row for row in PP_Length.data if row[PP_Length.fn[1]] == str(user)]
    print(len(user_sorted_rankings))
    print(amount)
    if amount == 0: # if no user input, send all available rows for requested user in database
        if len(user_sorted_rankings) > max_len:    # if discord can't send all rows, send as many as possible
            amount = max_len
        elif len(user_sorted_rankings) <= max_len:
            amount = len(user_sorted_rankings)
    elif amount > len(user_sorted_rankings):
        await context.send(f"You requested more than the available rankings for {user}."\
        f" There are {len(user_sorted_rankings)} available rankings for {user}.")
    elif amount > max_len:    # if discord can't send all rows, send as many as possible
        amount = max_len
    else:
        print("yooo")
    for row in range(amount):    # add rows to message
        final_msg += f"\n{user_sorted_rankings[row][PP_Length.fn[0]]}\t\t\t\t\t\t"\
        f" {user_sorted_rankings[row][PP_Length.fn[2]]}"

    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Insults.data)

    await context.send(final_msg)