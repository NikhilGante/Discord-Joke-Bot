import discord
import csv
from User_ID import User_ID
import random

class Database:
    path = ""
    fieldnames = []
    channel = ""
    name = ""
    final_string = ""

    def write_header(self):
        with open (self.path, "w", newline = "") as File:
            writer = csv.DictWriter(File, fieldnames = self.fieldnames)
            writer.writeheader()
    
    def download_data(self):
        with open (self.path, newline = "") as File:
            reader = csv.DictReader(File, fieldnames = self.fieldnames)
            next(reader) # skips header
            self.data = list(reader) # converts reader to list
    
    def upload_data(self):
        with open (self.path, "w", newline = "") as File:
            writer = csv.DictWriter(File, fieldnames = self.fieldnames)
            writer.writeheader()
            writer.writerows(self.data)
    
    # -------------------------- Generalized Logging Commands --------------------------  

    def add_entry(self, author, content):
        self.download_data()
        self.upload_data()
        with open (self.path, "a", newline = "") as self_File:
            writer = csv.DictWriter(self_File, fieldnames = self.fieldnames)
            writer.writerow({self.fieldnames[0] : f"{len(self.data) + 1}",\
            self.fieldnames[1] : f"{author}", self.fieldnames[2] : f"{content}"})

    async def erase_all(self, context):
        if(context.author.id == User_ID["Nikhil"]):
            self.write_header()        
            await context.send(f"All {self.name.lower()}s successfully deleted.")
        else:   await context.send("Only supreme memer CodingBoy56 has access to this command.")

    async def erase(self, context, index):
        index = int(index)
        self.download_data()

        if index > len(self.data) or index < 1:
            await context.send(f"You requested to erase {self.name.lower()} #{index}."\
            f" There are only {len(self.data)} {self.name.lower()}s.")
        else:
            self.data.pop(index - 1)
            for row in self.data[index - 1: len(self.data)]:
                row[self.fieldnames[0]] = int(row[self.fieldnames[0]])
                row[self.fieldnames[0]] -= 1
            self.upload_data()
            await context.send(f"{self.name} {index} succesfully deleted.")           

    async def show(self, context):
        self.download_data()
        self.final_string = f"**{self.fieldnames[0]}\t\t{self.fieldnames[1]}\t\t\t\t  \
        {self.fieldnames[2]}**" # adds header to message
        for row in self.data:    # add rows to message
            self.final_string += f"\n{row[self.fieldnames[0]]}\t\t\t\t {row[self.fieldnames[1]]}\t{row[self.fieldnames[2]]}"
        await context.send(self.final_string)

    async def get(self, context, index, user: discord.Member = None):
        self.download_data()
        index = int(index)
        if index > len(self.data):
            await context.send(f"You requested Insult #{index}. There are only {len(self.data)} insults available.")
            # self.final_string = (f"You requested Insult #{index}. There are only {len(self.data)} insults available.")
            return
        if user == None:
            mention = ""
        else:
            mention = f"<@{user}>"
        await context.send(f"{mention} {self.data[index - 1][self.fieldnames[2]]}")
        # self.final_string = f"{mention} {self.data[index - 1][self.fieldnames[2]]}"
        # await context.send(self.final_string)
    
    async def random(self, context, user: discord.Member = None):
        self.download_data()
        await self.get(context, random.randint(0, len(self.data)), user)

class Rankings(Database):
    def sort_data(self):
        self.download_data()
        for starting_value_index in range(len(self.data)-1):   # Sorts the rankings accordingly
            greatest_value_index = starting_value_index

            for index in range(starting_value_index, len(self.data)):
                if self.data[index][self.fieldnames[2]] > self.data[greatest_value_index][self.fieldnames[2]]:
                    greatest_value_index = index

            # exchanges value at greatest index and value at starting index
            temp_val = self.data[greatest_value_index][self.fieldnames[2]]
            self.data[greatest_value_index][self.fieldnames[2]] = self.data[starting_value_index][self.fieldnames[2]]
            self.data[starting_value_index][self.fieldnames[2]] = temp_val

        # gives each row the proper rank
        for row in self.data:
            row[self.fieldnames[0]] = self.data.index(row) + 1

        self.upload_data()

# class Queue(Database):
#     def 




# create database objects
Insults = Database()
PP_Length = Rankings()
Jokes = Database()
Quotes = Database()

# sets names
Insults.name = "Insult"
# PP_Length.name = ""
Jokes.name = "Joke"
Quotes.name = "Quote"

# sets csv file paths
Insults.path = "C:/Users/HP/OneDrive/Documents/GitHub/Discord-Insult-Bot-Database/Insults.csv"
PP_Length.path = "C:/Users/HP/OneDrive/Documents/GitHub/Discord-Insult-Bot-Database/PP_Length.csv"
Jokes.path = "C:/Users/HP/OneDrive/Documents/GitHub/Discord-Insult-Bot-Database/Jokes.csv"
Quotes.path = "C:/Users/HP/OneDrive/Documents/GitHub/Discord-Insult-Bot-Database/Quotes.csv"

# sets channels
Insults.channel = "bot-insults"
Jokes.channel = "bot-jokes"
Quotes.channel = "bot-quotes"

# sets fieldnames
Insults.fieldnames = ["Index:", "Author:", "Insult:"]
PP_Length.fieldnames = ["Ranking:", "User:", "Length:"]
Jokes.fieldnames = ["Index:", "Author:", "Joke:"]
Quotes.fieldnames = ["Index:", "Author:", "Quote:"]


def truncate(n, decimals = 0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


