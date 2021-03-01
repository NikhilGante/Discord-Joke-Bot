import discord
import csv
from User_ID import User_ID
import random

max_len = 62 # max amount of lines that can be sent on discord


class Database:
    path = ""
    fn = [] # fieldnames
    channel = ""
    name = ""
    final_string = ""
    field_strings = []

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

    async def show(self, context):
        self.download_data()
        Embed = discord.Embed(title = self.name, description = f"All of our {self.name.lower()}s so far.", color = 0x3a5af2)
        self.field_strings = ["", "", ""]
        for row in range(len(self.data)):
            for field in range(len(self.data[row])):
                self.field_strings[field] += f"\n{self.data[row][self.fn[field]]}"
        for string in range(len(self.field_strings)):
            Embed.add_field(name = self.fn[string], value = self.field_strings[string], inline = True)

            # self.fn[string]
            # self.field_strings[string]
        # Embed.add_field(name = "Sample name: ", value = "sample value", inline = True)
        # Embed.set_footer(text = "footer shit haha")
        # Embed.set_author(name = "Nikki the chiken")
        await context.send(embed = Embed)

        # await context.send(Insults.data)
        # print(final_msg)

        # self.final_string = f"**{self.fn[0]}\t\t{self.fn[1]}\t\t\t\t  \
        # {self.fn[2]}**" # adds header to message
        # for row in self.data:    # add rows to message
        #     self.final_string += f"\n{row[self.fn[0]]}\t\t\t\t {row[self.fn[1]]}\t{row[self.fn[2]]}"
        # await context.send(self.final_string)

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
            # temp_val = self.data[max_id][self.fn[1]]
            # self.data[max_id][self.fn[1]] = self.data[start_id][self.fn[1]]
            # self.data[start_id][self.fn[1]] = temp_val
            self.data[max_id][self.fn[1]], self.data[start_id][self.fn[1]]  = self.data[start_id][self.fn[1]], self.data[max_id][self.fn[1]]
            # exchanges value at greatest index and value at starting index
            """
            temp_val = self.data[max_id][self.fn[2]]
            self.data[max_id][self.fn[2]] = self.data[start_id][self.fn[2]]
            self.data[start_id][self.fn[2]] = temp_val
            """
            self.data[max_id][self.fn[2]], self.data[start_id][self.fn[2]]  = self.data[start_id][self.fn[2]], self.data[max_id][self.fn[2]]

        # gives each row the proper rank
        for row in self.data:
            row[self.fn[0]] = self.data.index(row) + 1

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
Insults.fn = ["Index:", "Author:", "Insult:"]
PP_Length.fn = ["Ranking:", "User:", "Length:"]
Jokes.fn = ["Index:", "Author:", "Joke:"]
Quotes.fn = ["Index:", "Author:", "Quote:"]

def truncate(n, decimals = 0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
