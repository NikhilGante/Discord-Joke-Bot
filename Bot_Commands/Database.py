import csv

class Database:
    path = ""
    fieldnames = []
    channel = ""

    def write_header(self):
        with open (self.path, "w", newline = "") as File:
            writer = csv.DictWriter(File, fieldnames = self.fieldnames)
            writer.writeheader()
    
    def download_data(self):
        with open (self.path, newline = "") as File:
            reader = csv.DictReader(File, fieldnames = self.fieldnames)
            next(reader)
            self.data = list(reader) # converts reader to list
    
    def upload_data(self):
        with open (self.path, "w", newline = "") as File:
            writer = csv.DictWriter(File, fieldnames = self.fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

class Rankings(Database):
    def sort_data(self):
        self.download_data()
        for starting_value_index in range(len(self.data)-1):   # Sorts the rankings accordingly
            greatest_value_index = starting_value_index

            for index in range(starting_value_index, len(self.data)-1):
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

# create database objects
Insults = Database()
PP_Length = Rankings()
Jokes = Database()
Quotes = Database()

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


