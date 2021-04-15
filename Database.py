import discord
import csv
from User_ID import User_ID
import random

max_len = 68 # max amount of lines that can be sent on discord

class Database:
    path = ""   # path for .csv where database is contained
    fn = [] # fieldnames (string names to index list of dictionaries)
    channel = ""
    name = ""   # name of database to use when printing
    final_string = ""   # final string to print
    field_strings = []  # strings that contain all the elements in a field (e.g. "User")
    embed_colour = 0x3a5af2

    def write_header(self):
        with open (self.path, "w", newline = "") as File:
            writer = csv.DictWriter(File, fieldnames = self.fn)
            writer.writeheader()
    
    def download_data(self):
        with open (self.path, newline = "") as File:
            reader = csv.DictReader(File, fieldnames = self.fn)
            next(reader) # skips header
            self.data = list(reader) # converts reader to list
    
    def upload_data(self):
        with open (self.path, "w", newline = "") as File:
            writer = csv.DictWriter(File, fieldnames = self.fn)
            writer.writeheader()
            writer.writerows(self.data)
    
    # -------------------------- Generalized Logging Commands --------------------------  

    def add_entry(self, author, content):
        self.download_data()
        self.upload_data()
        with open (self.path, "a", newline = "") as self_File:
            writer = csv.DictWriter(self_File, fieldnames = self.fn)
            writer.writerow({self.fn[0] : f"{len(self.data) + 1}",\
            self.fn[1] : f"{author}", self.fn[2] : f"{content}"})

    async def erase_all(self, context):
        if(context.author.id == User_ID["Nikhil"]):
            self.write_header()        
            await context.send(f"All {self.name.lower()}s successfully deleted.")
        else:   await context.send("Only supreme memer CodingBoy56 has access to this command.")

    # Function for user to erase a specific index from database
    async def erase(self, context, index):
        index = int(index)
        self.download_data()

        if index > len(self.data) or index < 1:
            await context.send(f"You requested to erase {self.name.lower()} #{index}."\
            f" There are only {len(self.data)} {self.name.lower()}s.")
        else:
            self.data.pop(index - 1)
            for row in self.data[index - 1: len(self.data)]:
                row[self.fn[0]] = int(row[self.fn[0]])
                row[self.fn[0]] -= 1
            self.upload_data()
            await context.send(f"{self.name} {index} succesfully deleted.")           

    # Function for user to print out contents of a database
    async def show(self, context):
        self.download_data()
        Embed = discord.Embed(title = self.name, description = f"All of your {self.name.lower()}s so far.", color = self.embed_colour)
        self.field_strings = ["", "", ""]
        for row in range(len(self.data)):
            for field in range(len(self.data[row])):
                self.field_strings[field] += f"\n{self.data[row][self.fn[field]]}"
        for string in range(len(self.field_strings)):
            Embed.add_field(name = self.fn[string], value = self.field_strings[string], inline = True)

        # Embed.add_field(name = "Sample name: ", value = "sample value", inline = True)
        # Embed.set_footer(text = "footer shit haha")
        # Embed.set_author(name = "Nikki the chiken")
        await context.send(embed = Embed)

    # Function for user to access specific index of a database
    async def get(self, context, index, user: discord.Member = None):
        self.download_data()
        index = int(index)
        if index > len(self.data):
            await context.send(f"You requested {self.name.lower()} #{index}. There are only {len(self.data)} {self.name.lower()}s available.")
        
        mention = "" if user == None else f"<@{user.id}>"

        await context.send(f"{mention} {self.data[index - 1][self.fn[2]]}")
    
    async def random(self, context, user: discord.Member = None):
        self.download_data()
        await self.get(context, random.randint(0, len(self.data)), user)

class Rankings(Database):
    def sort_data(self):
        self.download_data()
        for start_id in range(len(self.data)-1):   # Sorts the rankings accordingly
            max_id = start_id

            for index in range(start_id, len(self.data)):
                if self.data[index][self.fn[2]] > self.data[max_id][self.fn[2]]:
                    max_id = index
            # exchanges user at greatest index and value at starting index
            self.data[max_id][self.fn[1]], self.data[start_id][self.fn[1]]  = self.data[start_id][self.fn[1]], self.data[max_id][self.fn[1]]
            self.data[max_id][self.fn[2]], self.data[start_id][self.fn[2]]  = self.data[start_id][self.fn[2]], self.data[max_id][self.fn[2]]

        # gives each row the proper rank
        for row in self.data:
            row[self.fn[0]] = self.data.index(row) + 1

        self.upload_data()
    
    # Function for user to print out the desired amount of (ordered) rankings
    async def get_rank(self, context, amount):
        self.sort_data()
        amount = int(amount)

        # if no user input, or input is more than what discord allows, send as many rows as discord allows
        if amount == 0:
            if len(self.data) > max_len:
                amount = max_len
            elif len(self.data) <= max_len:
                amount = len(self.data)
        elif amount > len(self.data):
            await context.send(f"You requested more than the available in database."\
            f" There are {len(self.data)} available rankings in database.")
            return
        elif amount > max_len:
            amount = max_len

        # show message
        self.download_data()
        Embed = discord.Embed(title = f"{self.name}s", description = f"All of your {self.name.lower()}s so far.", color = self.embed_colour)
        self.field_strings = ["", "", ""]
        
        for row in range(amount):
            for field in range(len(self.data[row])):
                self.field_strings[field] += f"\n{self.data[row][self.fn[field]]}"
        for string in range(len(self.field_strings)):
            Embed.add_field(name = self.fn[string], value = self.field_strings[string], inline = True)
        
        await context.send(embed = Embed)

    # Function for user to rank another user, and select the amount of indices printed out
    async def rank(self, context, amount, user: discord.Member = None):
        self.sort_data()
        amount = int(amount)

        # user_sorted_rankings is filled with a list of dictionaries pertaining to the requested user
        user_sorted_rankings = [row for row in self.data if row[self.fn[1]] == str(user)]

        if amount == 0: # if no user input, send all available rows for requested user in database
            if len(user_sorted_rankings) > max_len:    # if discord can't send all rows, send as many as possible
                amount = max_len
            elif len(user_sorted_rankings) <= max_len:
                amount = len(user_sorted_rankings)
        elif amount > len(user_sorted_rankings):
            await context.send(f"You requested more than the available rankings for {user}."\
            f" There are {len(user_sorted_rankings)} available rankings for {user}.")
        elif amount > max_len:    # if discord can't send all rows, send as many as possible
            amount = max_len
        else:
            print(f"Sucess or Unknown condition triggered | amount received: {amount}")
            
        # shows message
        self.download_data()
        Embed = discord.Embed(title = f"{self.name}s", description = f"All of {user}'s {self.name.lower()}s so far.", color = self.embed_colour)
        self.field_strings = ["", "", ""]
        
        # fills field_strings with contents of user_sorted_rankings
        for row in range(amount):
            for field in range(len(self.data[row])):
                self.field_strings[field] += f"\n{user_sorted_rankings[row][self.fn[field]]}"
        
        # prints the 3 embeds inline
        for string in range(len(self.field_strings)):
            Embed.add_field(name = self.fn[string], value = self.field_strings[string], inline = True)
            # Embed.set_footer(text = "footer shit haha")
            # Embed.set_author(name = "Nikki the chiken")
        await context.send(embed = Embed)
        

# class Queue(Database):
#     def 

# create database objects
Insults = Database()
PP_Length = Rankings()
Jokes = Database()
Quotes = Database()

# defines names
Insults.name = "Insult"
PP_Length.name = "PP length"
Jokes.name = "Joke"
Quotes.name = "Quote"

# defines csv file paths
Insults.path = "C:/Users/HP/Documents/GitHub/Discord-Insult-Bot-Database/Insults.csv"
PP_Length.path = "C:/Users/HP/Documents/GitHub/Discord-Insult-Bot-Database/PP_Length.csv"
Jokes.path = "C:/Users/HP/Documents/GitHub/Discord-Insult-Bot-Database/Jokes.csv"
Quotes.path = "C:/Users/HP/Documents/GitHub/Discord-Insult-Bot-Database/Quotes.csv"

# defines channels
Insults.channel = "bot-insults"
Jokes.channel = "bot-jokes"
Quotes.channel = "bot-quotes"

# defines fieldnames
Insults.fn = ["Index:", "Author:", "Insult:"]
PP_Length.fn = ["Ranking:", "User:", "Length:"]
Jokes.fn = ["Index:", "Author:", "Joke:"]
Quotes.fn = ["Index:", "Author:", "Quote:"]

# defines embed colours
Insults.embed_colour = 0x3a5af2
PP_Length.embed_colour = 0x1e8c34
Jokes.embed_colour = 0x23eeb7
Quotes.embed_colour = 0x160bd3

def truncate(n, decimals = 0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
