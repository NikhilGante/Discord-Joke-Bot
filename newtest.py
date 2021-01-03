import csv

Insults_path = "C:/Users/HP/OneDrive/Documents/GitHub/Insults.csv"

Insults_File = open(Insults_path, newline = "")
reader = csv.reader(Insults_File)
header = next(reader)
data = []
User = [""]
Insults = [""]

for row in reader:
    Index = row[0]
    User = row[1]
    Insults = row[2]
    # print(f"{Index} {User} {Insults}")
    data.append([Index, User, Insults])

Insults_File.close()

Insults_File = open(Insults_path, "a")
writer = csv.writer(Insults_File)
writer.writerow(["Wet", "Ass", "Pussy"])

