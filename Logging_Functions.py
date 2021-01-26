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
    values = []
    for row in data_rank:
        values.append(row[rankings_fieldnames[2]])
 
    for start_val_id in range(len(values)-1):
        # start_val = values[start_val_id]
        # greatest = start_val
        greatest_id = start_val_id
        # vals_left = values[start_val_id + 1: len(values)]
        for val_id in range(start_val_id, len(values)):
            if values[val_id] > values[greatest_id]:    greatest_id = val_id

        temp_val = values[greatest_id]
        values[greatest_id] = values[start_val_id]
        values[start_val_id] = temp_val

        # Replaces appropriate rows in data_rank list
        temp_row = data_rank[greatest_id]
        data_rank[greatest_id] = data_rank[start_val_id]
        data_rank[start_val_id] = temp_row

    # gives each row the proper rank
    for row in data_rank:
        row[rankings_fieldnames[0]] = data_rank.index(row) + 1

    upload_data_rank()

def truncate(n, decimals = 0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
