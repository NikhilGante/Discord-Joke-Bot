import csv
from Bot_Commands import Insults_path

def write_header():
    global Insults_File
    with open (Insults_path, "w") as Insults_File:
        for label in header:
            # Insults_File.write(label if header[-1] == label else label + ",")
            Insults_File.write(label + ",")


def download_data():
    with open (Insults_path, newline = "") as Insults_File:
        reader = csv.reader(Insults_File)
        global header, data, next_index
        header = next(reader)
        data = [[word for word in row] for row in reader] # reads stuff much faster 
        next_index = len(data) + 1

def upload_data():
    write_header()
        
    for row in data:
        Insults_File.write(f"{row[0]},{row[1]},{row[2]}\n")
