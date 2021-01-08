import discord
from discord.ext import commands
import Insults
import csv
import random

Insults.download_data()
print(Insults.data[0]["Insult:"])



