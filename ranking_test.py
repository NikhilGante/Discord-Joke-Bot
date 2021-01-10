from Logging_Functions import rankings_fieldnames
import Logging_Functions
import random
import operator
import csv
from Bot_Commands import Rankings_Path

# size =  truncate(random.uniform(0, 10), 2)
# author = str(context.author)
# author = author[0:-5]
# finalStr = (f"{author}'s peepee is {size} inches long.\n")
# if size > 5:
#     finalStr += "What a damn Chad."
# elif size < 3:
#     finalStr += "I got some viagra bro, if you ever need it."
# else:
#     finalStr += "Ayo same."
# await context.send(finalStr)

def truncate(n, decimals = 0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
    
# size =  truncate(random.uniform(0, 10), 2)
# author = "NikkiChiken#3809"
# author = author[0:-5]
# finalStr = (f"{author}'s peepee is {size} inches long.\n")
# if size > 5:
#     finalStr += "What a damn Chad."
# elif size < 3:
#     finalStr += "I got some viagra bro, if you ever need it."
# else:
#     finalStr += "Ayo same."
# # await context.send(finalStr)

# Logging_Functions.download_data_rank()
# Logging_Functions.upload_data_rank()
# with open (Rankings_Path, "a", newline = "") as Rankings_File:
#     writer = csv.DictWriter(Rankings_File, fieldnames = Logging_Functions.rankings_fieldnames)
#     writer.writerow({rankings_fieldnames[0] : f"{len(Logging_Functions.data_rank) + 1}",
#      rankings_fieldnames[1] : f"{author}", rankings_fieldnames[2] : f"{size}"})

# sorting stuff

# Logging_Functions.download_data_rank(False)
with open (Rankings_Path, newline = "") as Rankings_File:
    reader = csv.reader(Rankings_File)
    global data_rank
    next(reader)
    data_rank = reader
    Logging_Functions.data_rank = sorted(data_rank, key = operator.itemgetter(2), reverse = True)
with open (Rankings_Path, "w", newline = "") as Rankings_File:
    writer = csv.writer(Rankings_File)
    writer.writerows(data_rank)

