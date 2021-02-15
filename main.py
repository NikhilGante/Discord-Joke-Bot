import discord
import csv
from Bot_Commands.Database import Insults, PP_Length, Jokes, Quotes
from discord.ext import commands
from Channel_ID import text, voice
from User_ID import User_ID, bot_Token
from Bot_Commands import Logging_Functions
from Bot_Commands.Voice import client
from Bot_Commands.Miscellaneous import client
from Keep_Alive import keep_alive

@client.event
async def on_message(message):
    # bot_testing_channel = client.get_channel(Channel_ID.text["bot-testing"])
    # bot_testing_channel.send("poggers") how to send to a specific channel
    author = message.author
    # name = author.display_name
    id = author.id
    # mention = f"<@{id}>"
    channel = message.channel
    text = message.content.lower()
    
    if author == client.user: # ignores message if it was sent from bot
        return

    if "--" not in text:
            
        if str(channel) == Insults.channel:
            Insults.download_data()
            Insults.upload_data()
            with open (Logging_Functions.Insults.path, "a", newline = "") as Insults_File:
                writer = csv.DictWriter(Insults_File, fieldnames = ["Index:", "Author:", "Insult:"])
                writer.writerow({"Index:" : f"{len(Insults.data) + 1}", "Author:" : f"{author}", "Insult:" : f"{message.content}"})
     
        elif str(channel) == Jokes.channel:
            Jokes.download_data()
            Jokes.upload_data()
            with open (Logging_Functions.Jokes.path, "a", newline = "") as Jokes_File:
                writer = csv.DictWriter(Jokes_File, fieldnames = ["Index:", "Author:", "Joke:"])
                writer.writerow({"Index:" : f"{len(Jokes.data) + 1}", "Author:" : f"{author}", "Joke:" : f"{message.content}"})       

        elif str(channel) == Quotes.channel:
            Quotes.download_data()
            Quotes.upload_data()
            with open (Logging_Functions.Quotes.path, "a", newline = "") as Quotes_File:
                writer = csv.DictWriter(Quotes_File, fieldnames = ["Index:", "Author:", "Quote:"])
                writer.writerow({"Index:" : f"{len(Quotes.data) + 1}", "Author:" : f"{author}", "Quote:" : f"{message.content}"})     

        # elif id != User_ID["Nikhil"]: #user isn't me and user isn't adding to a database
        #     print(f"The channel is: {channel}")
        #     print(author)
        #     print(name)
        #     print(f"Id: {author.id}")
        #     # await channel.send(f"I see you, {mention}")

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