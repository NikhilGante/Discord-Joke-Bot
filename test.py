import discord
from discord.ext import commands
import random
import pandas as pd

df = pd.read_csv("C:/Users/HP/OneDrive/Documents/GitHub/Discord-Insult-Bot/Insults.csv", index_col = 0)
# df = pd.dataframe({"User": "", "Insults" : ""})

# rowData = df.loc[0]
# print(f"{rowData}")
# print(f"type: {type(rowData)}")
# rowData = {}

# df[index] = df['column name'].replace(['old value'],'new value')
# df.ix['User','0'] = "Nikhil"
# df.ix['Insults','0'] = "memers haha funny"

print(df['User'][0])    # how you actually index stuff
print(df['Insults'][0])

print(f"df before: {df}")
# df['User'][0] = "Nikhil"
# df['Insults'][0] = "momma so chunky"

# df["User"].discard(0)
# df["Insults"].discard(0)
df.drop(0) 
print(f"df after: {df}")
df.to_csv("C:/Users/HP/OneDrive/Documents/GitHub/Discord-Bot/Insults.csv")

print("shit shit shit")
df = pd.read_csv("C:/Users/HP/OneDrive/Documents/GitHub/Discord-Bot/Insults.csv", index_col = 0)
print(f"df: {df}")


