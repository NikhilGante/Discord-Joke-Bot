from Logging_Functions import rankings_fieldnames
import Logging_Functions
import random
import operator
import csv
from Bot_Commands import Rankings_Path


# sorting stuff
# Logging_Functions.write_header_rank()

# author = "coggers"
# size = 54
# Logging_Functions.download_data_rank()
# Logging_Functions.upload_data_rank()
# with open (Rankings_Path, "a", newline = "") as Rankings_File:
#     writer = csv.DictWriter(Rankings_File, fieldnames = rankings_fieldnames)
#     writer.writerow({rankings_fieldnames[0] : f"{len(Logging_Functions.data_rank) + 1}",
#     rankings_fieldnames[1] : f"{author}", rankings_fieldnames[2] : f"{size}"})

def sort(values):
    for start_val in values:
        greatest = start_val
        for val in values[values.index(start_val) + 1: len(values)]:
            if val > greatest:
                greatest = val
        temp = greatest
        values[values.index(greatest)] = start_val
        values[values.index(start_val)] = temp
    return values

def sort_data_rank():
    Logging_Functions.download_data_rank()
    data_rank = Logging_Functions.data_rank
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

    Logging_Functions.upload_data_rank()

# sort_data_rank()
sort_data_rank()

