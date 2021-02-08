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

# create database objects
Insults = Database()
PP_Rankings = Rankings()
Jokes = Database()
Quotes = Database()

# set csv file paths
Insults.path = "C:/Users/HP/OneDrive/Documents/GitHub/Insults.csv"
Rankings.path = "C:/Users/HP/OneDrive/Documents/GitHub/Rankings.csv"
# Insults_path = "C:/Users/HP/OneDrive/Documents/GitHub/Insults.csv"
# Rankings_Path = "C:/Users/HP/OneDrive/Documents/GitHub/Rankings.csv"

# set fieldnames
Insults.fieldnames = ["Index:", "Author:", "Insult:"]
Rankings.fieldnames = ["Ranking:", "User:", "Length:"]
# insults_fieldnames = ["Index:", "Author:", "Insult:"]
# rankings_fieldnames = ["Ranking:", "User:", "Length:"]



# def write_header_insult():
#     with open (Insults_path, "w", newline = "") as Insults_File:
#         writer = csv.DictWriter(Insults_File, fieldnames = insults_fieldnames)
#         writer.writeheader()

# def download_data_insult():
#     with open (Insults_path, newline = "") as Insults_File:
#         reader = csv.DictReader(Insults_File, fieldnames = insults_fieldnames)
#         global data_insult
#         next(reader)
#         data_insult = list(reader) # converts reader to list
       
# def upload_data_insult():
#     with open (Insults_path, "w", newline = "") as Insults_File:
#         writer = csv.DictWriter(Insults_File, fieldnames = insults_fieldnames)
#         writer.writeheader()
#         writer.writerows(data_insult)

# def write_header_rank():
#     with open (Rankings_Path, "w", newline = "") as Rankings_File:
#         writer = csv.DictWriter(Rankings_File, fieldnames = rankings_fieldnames)
#         writer.writeheader()

# def download_data_rank():
#     with open (Rankings_Path, newline = "") as Rankings_File:
#         reader = csv.DictReader(Rankings_File, fieldnames = rankings_fieldnames)
#         global data_rank
#         next(reader)
#         data_rank = list(reader) # converts reader to list 

# def upload_data_rank():
#     with open (Rankings_Path, "w", newline = "") as Rankings_File:
#         writer = csv.DictWriter(Rankings_File, fieldnames = rankings_fieldnames)
#         writer.writeheader()
#         writer.writerows(data_rank)



def truncate(n, decimals = 0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
