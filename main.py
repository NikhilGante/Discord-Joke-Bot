import discord
import csv
import Logging_Functions
from discord.ext import commands
from Channel_ID import text, voice
from User_ID import User_ID, bot_Token
import Bot_Commands
from Bot_Commands import client
from Keep_Alive import keep_alive

@client.event
async def on_message(message):
    # bot_testing_channel = client.get_channel(Channel_ID.text["bot-testing"])
    # bot_testing_channel.send("poggers") how to send to a specific channel
    author = message.author
    name = author.display_name
    id = author.id
    # mention = f"<@{id}>"
    channel = message.channel
    text = message.content.lower()
    
    if author == client.user: # ignores message if it was sent from bot
        return

    if "--" not in text:
            
        if str(channel) == "bot-requests":
            Logging_Functions.download_data_insult()
            Logging_Functions.upload_data_insult()
            with open (Bot_Commands.Insults_path, "a", newline = "") as Insults_File:
                writer = csv.DictWriter(Insults_File, fieldnames = ["Index:", "Author:", "Insult:"])
                writer.writerow({"Index:" : f"{len(Logging_Functions.data_insult) + 1}", "Author:" : f"{author}", "Insult:" : f"{message.content}"})
       
        elif id != User_ID["Nikhil"]: #channel isn't bot-testing and user isn't me
            print(f"The channel is: {channel}")
            print(author)
            print(name)
            print(f"Id: {author.id}")
            # await channel.send(f"I see you, {mention}")

        if "pp" in text or "penis" in text or "dick" in text or "cock" in text:
            await channel.send("ligma penis")

        if id == User_ID["Liam"]:    
            await channel.send("Liam, you're kinda cute")

    await client.process_commands(message)
    
@client.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandNotFound):
        await context.send("Command not found. Please type in a valid command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await context.send("Missing required arguments. Please type in *all* arguments.")    
    elif isinstance(error, commands.MissingPermissions):
        await context.send("You do not have the necessary permissions.")

@commands.Cog.listener()
async def on_typing(channel, user, when):
    print("typing has been detected")
    print(user.id)
    print(channel)
    print(when)
    
    # await channel.send(f"Don't even think about it @{user}")


@client.event
async def on_ready():
    bot_testing_channel = client.get_channel(802791468279398411) # bot-testing channel in bot-testing server

    await bot_testing_channel.send("Initialized.")
    await client.change_presence(status = discord.Status.online, activity = discord.Game("with my schlong"))



# keep_alive()    # keeps bot online via https web server
client.run(bot_Token)   # botID is privatized