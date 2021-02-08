import csv

Insults_path = "C:/Users/HP/OneDrive/Documents/GitHub/Insults.csv"
Rankings_Path = "C:/Users/HP/OneDrive/Documents/GitHub/Rankings.csv"

insults_fieldnames = ["Index:", "Author:", "Insult:"]
rankings_fieldnames = ["Ranking:", "User:", "Length:"]

def write_header_insult():
    with open (Insults_path, "w", newline = "") as Insults_File:
        writer = csv.DictWriter(Insults_File, fieldnames = insults_fieldnames)
        writer.writeheader()

def download_data_insult():
    with open (Insults_path, newline = "") as Insults_File:
        reader = csv.DictReader(Insults_File, fieldnames = insults_fieldnames)
        global data_insult
        next(reader)
        data_insult = list(reader) # converts reader to list
       
def upload_data_insult():
    with open (Insults_path, "w", newline = "") as Insults_File:
        writer = csv.DictWriter(Insults_File, fieldnames = insults_fieldnames)
        writer.writeheader()
        writer.writerows(data_insult)

def write_header_rank():
    with open (Rankings_Path, "w", newline = "") as Rankings_File:
        writer = csv.DictWriter(Rankings_File, fieldnames = rankings_fieldnames)
        writer.writeheader()

def download_data_rank():
    with open (Rankings_Path, newline = "") as Rankings_File:
        reader = csv.DictReader(Rankings_File, fieldnames = rankings_fieldnames)
        global data_rank
        next(reader)
        data_rank = list(reader) # converts reader to list 

def upload_data_rank():
    with open (Rankings_Path, "w", newline = "") as Rankings_File:
        writer = csv.DictWriter(Rankings_File, fieldnames = rankings_fieldnames)
        writer.writeheader()
        writer.writerows(data_rank)

def sort_data_rank():
    download_data_rank()
    pp_len = rankings_fieldnames[2]
    for starting_value_index in range(len(data_rank)-1):   # Sorts the rankings accordingly
        greatest_value_index = starting_value_index

        for index in range(starting_value_index, len(data_rank)):
            if data_rank[index][pp_len] > data_rank[greatest_value_index][pp_len]:
                greatest_value_index = index

        # exchanges value at greatest index and value at starting index
        temp_val = data_rank[greatest_value_index][pp_len]
        data_rank[greatest_value_index][pp_len] = data_rank[starting_value_index][pp_len]
        data_rank[starting_value_index][pp_len] = temp_val

    # gives each row the proper rank
    for row in data_rank:
        row[rankings_fieldnames[0]] = data_rank.index(row) + 1

    upload_data_rank()

def truncate(n, decimals = 0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
