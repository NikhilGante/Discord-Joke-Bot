

array = [
{"hello" : "yo", "uwu": "poggers", "quirky": "coggers"},
{"hello" : "meme", "uwu": "hotties", "quirky": "titties"},
{"hello" : "uncogging indeed", "uwu": "sock", "quirky": "brrr"},
{"hello" : "whassupo", "uwu": "funny", "quirky": "haha"},
{"hello" : "peepee", "uwu": "cum", "quirky": "nincompoop"},
]

temp_row = array[0]["uwu"], array[0]["quirky"]
array[0]["uwu"], array[0]["quirky"] = array[3]["uwu"], array[3]["quirky"] 
array[3]["uwu"], array[3]["quirky"] = temp_row

for row in array:
    print(row)