import discord
from discord.ext import commands
from Channel_ID import text, voice
from User_ID import User_ID, bot_Token
import Bot_Commands
from Bot_Commands import client
import pandas


@client.event
async def on_message(message):
    # bot_testing_channel = client.get_channel(Channel_ID.text["bot-testing"])
    # bot_testing_channel.send("ligma penis") how to send to a specific channel
    author = message.author
    name = author.display_name
    id = author.id
    # mention = f"<@{id}>"
    channel = message.channel
    text = message.content.lower()
    
    if author == client.user: # ignores message if it was sent from bot
        return

    if "--" not in text and id != User_ID["Nikhil"]:

        # await channel.send(f"The channel is: {channel}")
        print(f"The channel is: {channel}")
        print(author)
        print(name)
        print(f"Id: {author.id}")
        # await channel.send(f"I see you, {mention}")


        if " pp " in text or "penis" in text:
            await channel.send("ligma penis")

        if id == User_ID["Liam"]:    
            await channel.send("Liam, you're kinda cute")
        
    if str(channel) == "bot-testing":
        await channel.send("in bot-testing")

        df = pandas.read_csv("C:/Users/HP/OneDrive/Documents/GitHub/Insults.csv", index_col = 0)
        df = df.append({"User": str(author), "Insults": str(message.content)}, ignore_index = True)
        # df = df.append({}, ignore_index = True)
        df.to_csv("C:/Users/HP/OneDrive/Documents/GitHub/Insults.csv") 

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
    bot_testing_channel = client.get_channel(793377011569393665)

    await bot_testing_channel.send("Initialized.")
    await client.change_presence(status = discord.Status.online, activity = discord.Game("with Chandu's schlong"))

    # df = pandas.DataFrame({"A": ["yo", "bitch"]})
    # df.to_csv("C:/Users/HP/OneDrive/Documents/Visual Studio Code/Beginner Projects/Innovirus.exe/Insults.csv")

# botID is privatized
client.run(bot_Token)