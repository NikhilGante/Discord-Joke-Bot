import discord
from discord.ext import commands
from Miscellaneous import client

client.remove_command("help")
client.group(invoke_without_command = True)
async def help(context):
    Embed = discord.Embed(title = "Help", description = "Use help <command> for more detailed information regarding the command.", color = context.author.color)

    Embed.add_field(name = "Database", value = "erase_all_insults, erase_all_jokes, erase_all_quotes, erase_insult, erase_joke, erase_quote", inline = false)
    Embed.add_field(name = "PP_Lnegth", value = "peepee_size, get_rank, rank", inline = false)
    Embed.add_field(name = "Music", value = "join, leave, pause, play, stop", inline = false)
    Embed.add_field(name = "Utilities", value = "printf, clear, help, ban, kick, unban", inline = false)


    await context.send(embed = Embed)










