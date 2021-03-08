import discord
from discord.ext import commands
from Miscellaneous import client

# client.group(invoke_without_command = True)
client.remove_command("help")
client.command(aliases = "h")
async def help(context):
    Embed = discord.Embed(title = "Help", description = "Use help <command> for more detailed a description.", color = context.author.color)

    Embed.add_field(name = "Database", value = "erase_all_insults, erase_all_jokes, erase_all_quotes, erase_insult, erase_joke, erase_quote", inline = False)
    Embed.add_field(name = "PP_Length", value = "get_rank, rank, peepee_size", inline = False)
    Embed.add_field(name = "Music", value = "join, leave, pause, play, stop", inline = False)
    Embed.add_field(name = "Utilities", value = "clear, ban, help, kick, printf, unban", inline = False)

    await context.send(embed = Embed)

# @help.command()
# async def erase_all_insults(context):
#     Embed = discord.Embed(title = erase_all_insults, description = "Wipes the insult database")
    
#     Embed.add_field(name = "Syntax", value = "--erase_all_insults")
#     Embed.add_field(name = "Aliases", value = "None.")
#     Embed.add_field(name = "Notes", value = "This command is only available to supreme memer CodingBoy56.")

#     await context.send(embed = Embed)






