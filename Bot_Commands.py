import discord
from discord.ext import commands
from Logging_Functions import rankings_fieldnames, Insults_path, Rankings_Path
import Logging_Functions
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

@client.command(aliases = ["q", "a_q", "aq"])
async def add_quote(context):

    await context.send(f"Here's your quote, lil' bitch ({context.message.author})")

@client.command(aliases = ["q_b", "qb"])
async def quotebook(context):

    await context.send("Quotebook test:")
    
    #send embed
    Embed = discord.Embed(title = "Quotebook", description = "All of our quotes so far", color = 0xba5ef7)
    Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    Embed.set_footer(text = "footer shit haha")
    Embed.set_author(name = "Nikki the chiken")

    await context.send(embed = Embed)
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
    
@client.command()
async def erase_all_insults(context):
    if(context.author.id == User_ID["Nikhil"]):
        Logging_Functions.write_header_insult()
    else:
        context.send("Only supreme memer CodingBoy56 has access to this command.")

@client.command(aliases = ["ei"])
async def erase_insult(context, index):
    index = int(index)
    Logging_Functions.download_data_insult()

    if index > len(Logging_Functions.data_insult) or index < 1:
        await context.send("Index out of range")
    else:
        Logging_Functions.data_insult.pop(index - 1)
        for row in Logging_Functions.data_insult[index - 1: len(Logging_Functions.data_insult)]:
            row["Index:"] = int(row["Index:"])
            row["Index:"] -= 1
        Logging_Functions.upload_data_insult()
        await context.send(f"Insult {index} succesfully deleted.")

@client.command(aliases = ["si", "show insults"])
async def show_insults(context):
    Logging_Functions.download_data_insult()
    final_msg = "**Index:\t\tAuthor:\t\t\t\t\t\t Insult:**" # adds header to message
    for row in Logging_Functions.data_insult:    # add rows to message
        final_msg += f"\n{row['Index:']}\t\t\t\t {row['Author:']}\t{row['Insult:']}"

    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Logging_Functions.data_insult)
    # print(final_msg)
    await context.send(final_msg)

@client.command(aliases = ["ri", "rand insult"])
async def rand_insult(context, user: discord.Member = None):
    Logging_Functions.download_data_insult()
    await get_insult(context, random.randint(0, len(Logging_Functions.data_insult)), user)

@client.command(aliases = ["gi", "get insult"])
async def get_insult(context, index, user: discord.Member = None):
    Logging_Functions.download_data_insult()
    if user == None:
        print ("none reached")
        mention = ""

    else:
        user = user.id
        print ("mention reached")
        mention = f"<@{user}>"

    await context.send(f"{mention} {Logging_Functions.data_insult[int(index) - 1]['Insult:']}")  

@client.command(aliases = ["ps", "ppsize", "peepee size"])
async def peepee_size(context):
    size =  Logging_Functions.truncate(random.uniform(0, 10), 2)
    author = str(context.author)
    author = author[0:-5]
    finalStr = (f"{author}'s peepee is {size} inches long.\n")
    if size > 5:
        finalStr += "What a damn Chad."
    elif size < 3:
        finalStr += "I got some viagra bro, if you ever need it."
    else:
        finalStr += "Ayo same."
    await context.send(finalStr)
    
    Logging_Functions.download_data_rank()
    Logging_Functions.upload_data_rank()
    with open (Rankings_Path, "a", newline = "") as Rankings_File:
        writer = csv.DictWriter(Rankings_File, fieldnames = Logging_Functions.rankings_fieldnames)
        writer.writerow({rankings_fieldnames[0] : f"{len(Logging_Functions.data_rank) + 1}",
        rankings_fieldnames[1] : f"{author}", rankings_fieldnames[2] : f"{size}"})

@client.command(aliases = ["gr", "get rank"])
async def get_rank(context, amount = 0):
    Logging_Functions.sort_data_rank()
    amount = int(amount)
    data_rank = Logging_Functions.data_rank
    if amount == 0: # if no user input, send all rows in database
        amount = len(data_rank)
    final_msg = "**Ranking:\t\t\tLength:\t\t\tOwner of PP:**" # adds header to message
    
    for row in range(amount):    # add rows to message
        final_msg += f"\n{data_rank[row][rankings_fieldnames[0]]}\t\t\t\t\t\t"\
        f" {data_rank[row][rankings_fieldnames[2]]}\t\t\t\t{data_rank[row][rankings_fieldnames[1]]}"
    print(final_msg)
    
    # for row in Logging_Functions.data_rank:    # add rows to message
    #     final_msg += f"\n{row[rankings_fieldnames[0]]}\t\t\t\t\t\t {row[rankings_fieldnames[2]]}\t\t\t\t{row[rankings_fieldnames[1]]}"
    # print(final_msg)

    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Logging_Functions.data_insult)
    # print(final_msg)
    await context.send(final_msg)



# @client.command(aliases = ["r"])
# async def rank(context, user: discord.Member = None):

#     def write_header_rank():
#     with open (Insults_path, "w", newline = "") as Rankings_File:
#         writer = csv.DictWriter(Insults_File, fieldnames = Logging_Functions.rankings_fieldnames)
#         writer.writeheader()

# def download_data():
#     with open (Insults_path, newline = "") as Insults_File:
#         reader = csv.DictReader(Insults_File, fieldnames = ["Index:", "Author:", "Insult:"])
#         global header, data
#         header = next(reader)
#         data = list(reader) # converts reader to list
       
# def upload_data():
#     with open (Insults_path, "w", newline = "") as Insults_File:
#         writer = csv.DictWriter(Insults_File, fieldnames = ["Index:", "Author:", "Insult:"])
#         writer.writeheader()
#         writer.writerows(data)




  
