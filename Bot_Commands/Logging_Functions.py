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
    if(context.author.id == User_ID["Nikhil"]):
        Insults.write_header()        
        await context.send("All insults successfully deleted.")
    else:
        await context.send("Only supreme memer CodingBoy56 has access to this command.")

@client.command(aliases = ["ei"])
async def erase_insult(context, index):
    index = int(index)
    Insults.download_data()

    if index > len(Insults.data) or index < 1:
        await context.send("Index out of range")
    else:
        Insults.data.pop(index - 1)
        for row in Insults.data[index - 1: len(Insults.data)]:
            row[Insults.fieldnames[0]] = int(row[Insults.fieldnames[0]])
            row[Insults.fieldnames[0]] -= 1
        Insults.upload_data()
        await context.send(f"Insult {index} succesfully deleted.")

@client.command(aliases = ["si", "show insults"])
async def show_insults(context):
    Insults.download_data()
    final_msg = "**Index:\t\tAuthor:\t\t\t\t\t\t Insult:**" # adds header to message
    for row in Insults.data:    # add rows to message
        final_msg += f"\n{row[Insults.fieldnames[0]]}\t\t\t\t {row[Insults.fieldnames[1]]}\t{row[Insults.fieldnames[2]]}"

    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Insults.data)
    # print(final_msg)
    await context.send(final_msg)

@client.command(aliases = ["ri", "rand insult"])
async def rand_insult(context, user: discord.Member = None):
    Insults.download_data()
    await get_insult(context, random.randint(0, len(Insults.data)), user)

@client.command(aliases = ["gi", "get insult"])
async def get_insult(context, index, user: discord.Member = None):
    Insults.download_data()
    index = int(index)
    if index > len(Insults.data):
        await context.send(f"You requested Insult #{index}. There are only {len(Insults.data)} insults available.")
        return

    if user == None:     mention = ""

    else:
        user = user.id
        mention = f"<@{user}>"

    await context.send(f"{mention} {Insults.data[index - 1]['Insult:']}")  

# -------------------------- JOKES SECTION --------------------------  

@client.command()
async def erase_all_jokes(context):
    if(context.author.id == User_ID["Nikhil"]):
        Jokes.write_header()
        await context.send("All jokes successfully deleted.")
    else:
        await context.send("Only supreme memer CodingBoy56 has access to this command.")

@client.command(aliases = ["ej"])
async def erase_joke(context, index):
    index = int(index)
    Jokes.download_data()

    if index > len(Jokes.data) or index < 1:
        await context.send("Index out of range")
    else:
        Jokes.data.pop(index - 1)
        for row in Jokes.data[index - 1: len(Jokes.data)]:
            row[Jokes.fieldnames[0]] = int(row[Jokes.fieldnames[0]])
            row[Jokes.fieldnames[0]] -= 1
        Jokes.upload_data()
        await context.send(f"Joke {index} successfully deleted.")

@client.command(aliases = ["sj", "show jokes"])
async def show_jokes(context):
    Jokes.download_data()
    final_msg = "**Index:\t\tAuthor:\t\t\t\t\t\t Joke:**" # adds header to message
    for row in Jokes.data:    # add rows to message
        final_msg += f"\n{row['Index:']}\t\t\t\t {row['Author:']}\t{row['Joke:']}"

    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Jokes.data)
    # print(final_msg)
    await context.send(final_msg)

@client.command(aliases = ["rj", "rand joke"])
async def rand_joke(context, user: discord.Member = None):
    Jokes.download_data()
    await get_joke(context, random.randint(0, len(Jokes.data)), user)

@client.command(aliases = ["gj", "get joke"])
async def get_joke(context, index, user: discord.Member = None):
    Jokes.download_data()
    index = int(index)
    if index > len(Jokes.data):
        await context.send(f"You requested joke #{index}. There are only {len(Jokes.data)} jokes available.")
        return

    if user == None:    mention = ""

    else:
        user = user.id
        mention = f"<@{user}>"

    await context.send(f"{mention} {Jokes.data[index - 1]['Joke:']}")  

# -------------------------- QUOTES SECTION --------------------------  

@client.command()
async def erase_all_quotes(context):
    if(context.author.id == User_ID["Nikhil"]):
        Quotes.write_header()
        await context.send("All quotes successfully deleted.")
    else:
        await context.send("Only supreme memer CodingBoy56 has access to this command.")

@client.command(aliases = ["eq"])
async def erase_quote(context, index):
    index = int(index)
    Quotes.download_data()

    if index > len(Quotes.data) or index < 1:
        await context.send("Index out of range")
    else:
        Quotes.data.pop(index - 1)
        for row in Quotes.data[index - 1: len(Quotes.data)]:
            row[Quotes.fieldnames[0]] = int(row[Quotes.fieldnames[0]])
            row[Quotes.fieldnames[0]] -= 1
        Quotes.upload_data()
        await context.send(f"Quote {index} successfully deleted.")

@client.command(aliases = ["sq", "show quotes"])
async def show_quotes(context):
    Quotes.download_data()
    final_msg = "**Index:\t\tAuthor:\t\t\t\t\t\t Quote:**" # adds header to message
    for row in Quotes.data:    # add rows to message
        final_msg += f"\n{row[Quotes.fieldnames[0]]}\t\t\t\t {row[Quotes.fieldnames[1]]}\t{row[Quotes.fieldnames[2]]}"
    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Quotes.data)
    # print(final_msg)
    await context.send(final_msg)

@client.command(aliases = ["rq", "rand quote"])
async def rand_quote(context, user: discord.Member = None):
    Quotes.download_data()
    await get_quote(context, random.randint(0, len(Quotes.data)), user)

@client.command(aliases = ["gq", "get quote"])
async def get_quote(context, index, user: discord.Member = None):
    Quotes.download_data()
    index = int(index)
    if index > len(Quotes.data):
        await context.send(f"You requested quote #{index}. There are only {len(Quotes.data)} quotes available.")
        return

    if user == None:    mention = ""

    else:
        user = user.id
        mention = f"<@{user}>"

    await context.send(f"{mention} {Quotes.data[index - 1]['Quote:']}")  

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
    with open (PP_Length.path, "a", newline = "") as PP_Length_File:
        writer = csv.DictWriter(PP_Length_File, fieldnames = PP_Length.fieldnames)
        writer.writerow({PP_Length.fieldnames[0] : f"{len(PP_Length.data) + 1}",
        PP_Length.fieldnames[1] : f"{author}", PP_Length.fieldnames[2] : f"{size}"})

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