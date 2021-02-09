import discord
from discord.ext import commands
from Database import Insults, PP_Length, Jokes, Quotes
import Database
import csv
import operator
import random
from User_ID import User_ID

client = commands.Bot(command_prefix = "--")

@client.command(aliases = ["h", "hm", "help me"])
async def help_me(context):
    
    author = context.author
    # name = author.display_name
    id = author.id
    mention = f"<@{id}>"
    # channel = context.channel

    await context.send(f"{mention} I've sent you a list of all my commands")
    await author.send("I just want to let you know... you're a little bitch :)")
    Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    Embed.set_footer(text = "footer shit haha")
    Embed.set_author(name = "Nikki the chiken")

    await context.message.author.send(embed = Embed)


# 74412C
@client.command(aliases = ["p", "pf", "p_f", "print"])
async def printf(context, phrase = "", amount = 0):
    for count in range(int(amount)):
        await context.send(f"{count + 1}: {phrase}")
    await context.send("Done.")
    
@client.command(aliases = ["c"])
async def clear(context, amount = 1):    
    if amount == -256:
            await context.channel.purge(bulk = True)

    else:
        await context.channel.purge(limit = amount + 1)

@client.command()
async def kick(context, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await context.send(f"{member.mention} has been kicked")

@client.command()
async def ban(context, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await context.send(f"{member.mention} has been banned")

@client.command()
async def unban(context, *, member):
    banned_users = await context.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await context.guild.unban(user)
            await context.send(f"{member.mention} has been unbanned")
            return

@client.command
async def join(context):
    # channel = context.message.author.voice.voice_channel
    #     channel = context.message.author.voice.voice_channel
    # context.voice_channel
    # discord.VoiceProtocol(client, context.voice_channel)

    # protocol = discord.VoiceProtocol(client, context.voice_channel)

    # await voiceChannel.connect(channel)
    # await protocol.connect(60,True)
    # await voiceChannel.connect(channel)
    # await connect(*, timeout=60.0, reconnect=True, cls=<class 'discord.voice_client.VoiceClient'>)
    pass

@client.command
async def leave(parameter_list):
    pass


# @client.command (aliases = ["random image", "random img", "rand image", "randimg", "rand img", "ri"])
# async def random_image(context):


#     images = [, , , ]

#     random_image = random.choice(images)

#     context.send(file = discord.File(random_image))

# -------------------------- INSULTS SECTION ----------------------------------  

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

# -------------------------- JOKES SECTION ----------------------------------  

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

# -------------------------- QUOTES SECTION ----------------------------------  

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

# -------------------------- PP_LENGTH SECTION ----------------------------------  

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

