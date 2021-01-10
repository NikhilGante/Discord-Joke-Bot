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
        global header, data_insult
        header = next(reader)
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

def download_data_rank(Convert_to_list = True):
    with open (Rankings_Path, newline = "") as Rankings_File:
        reader = csv.DictReader(Rankings_File, fieldnames = rankings_fieldnames)
        global data_rank
        next(reader)
        if Convert_to_list:
            data_rank = list(reader) # converts reader to list
        else:
            data_rank = reader
       
def upload_data_rank():
    with open (Rankings_Path, "w", newline = "") as Rankings_File:
        writer = csv.DictWriter(Rankings_File, fieldnames = rankings_fieldnames)
        writer.writeheader()
        writer.writerows(data_rank)

