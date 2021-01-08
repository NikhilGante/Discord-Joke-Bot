import csv
from Bot_Commands import Insults_path

def write_header():
    with open (Insults_path, "w", newline = "") as Insults_File:
        writer = csv.DictWriter(Insults_File, fieldnames = ["Index:", "Author:", "Insult:"])
        writer.writeheader()

def download_data():
    with open (Insults_path, newline = "") as Insults_File:
        reader = csv.DictReader(Insults_File, fieldnames = ["Index:", "Author:", "Insult:"])
        global header, data
        header = next(reader)
        data = list(reader) # converts reader to list
       
def upload_data():
    with open (Insults_path, "w", newline = "") as Insults_File:
        writer = csv.DictWriter(Insults_File, fieldnames = ["Index:", "Author:", "Insult:"])
        writer.writeheader()
        writer.writerows(data)
