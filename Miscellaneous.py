import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "--")

# @client.command(aliases = ["h", "hm", "help me"])
# async def help_me(context):
    
#     author = context.author
#     # name = author.display_name
#     id = author.id
#     mention = f"<@{id}>"
#     # channel = context.channel

#     await context.send(f"{mention} I've sent you a list of all my commands")
#     await author.send("I just want to let you know... you're a little bitch :)")
#     Embed = discord.Embed(title = "PP memes", description = "All of our quotes so far", color = 0x3a5af2)
#     Embed.add_field(name = "Sample name: ", value = "sample value", inline = False)
#     Embed.set_footer(text = "footer shit haha")
#     Embed.set_author(name = "Nikki the chiken")

#     await context.message.author.send(embed = Embed)


# 74412C
@client.command(aliases = ["print"])
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

# @client.command (aliases = ["random image", "random img", "rand image", "randimg", "rand img", "ri"])
# async def random_image(context):


#     images = [, , , ]

#     random_image = random.choice(images)

#     context.send(file = discord.File(random_image))

