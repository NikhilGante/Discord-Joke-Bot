import discord
from discord.ext import commands
import Insults
import csv
import random
from User_ID import User_ID

client = commands.Bot(command_prefix = "--")
Insults_path = "C:/Users/HP/OneDrive/Documents/GitHub/Insults.csv"

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
        Insults.write_header()
    else:
        context.send("Only supreme memer CodingBoy56 has access to this command.")

@client.command(aliases = ["ei"])
async def erase_insult(context, index):
    index = int(index)
    Insults.download_data()

    if index > len(Insults.data) or index < 1:
        await context.send("Index out of range")
    else:
        Insults.data.pop(index - 1)
        for row in Insults.data[index - 1: len(Insults.data)]:
            row["Index:"] = int(row["Index:"])
            row["Index:"] -= 1
        Insults.upload_data()

@client.command(aliases = ["si", "show insults"])
async def show_insults(context):
    Insults.download_data()
    final_msg = "Index:\t\tAuthor:\t\t\t\t\t\t Insult:" # adds header to message
    for row in Insults.data:    # add rows to message
        final_msg += f"\n{row['Index:']}\t\t\t\t {row['Author:']}\t{row['Insult:']}"

    # Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
    # Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
    # Embed.set_footer(text = "footer shit haha")
    # Embed.set_author(name = "Nikki the chiken")

    # await context.message.author.send(embed = Embed)

    # await context.send(Insults.data)
    # print(final_msg)
    await context.send(final_msg)

@client.command(aliases = ["ps", "ppsize", "peepee size"])
async def peepee_size(context):
    size =  truncate(random.uniform(0, 10), 2)
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

@client.command(aliases = ["ri", "rand insult"])
async def rand_insult(context, user: discord.Member = None):
    Insults.download_data()
    await get_insult(context, random.randint(0, len(Insults.data)), user)

@client.command(aliases = ["gi", "get insult"])
async def get_insult(context, index, user: discord.Member = None):
    Insults.download_data()
    if user == None:
        print ("none reached")
        mention = ""

    else:
        user = user.id
        print ("mention reached")
        mention = f"<@{user}>"

    await context.send(f"{mention} {Insults.data[int(index) - 1]['Insult:']}")    

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

