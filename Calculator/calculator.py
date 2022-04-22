import re
import pandas

class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score

lines = []

print("Reading file...")
with open("C:\\Users\\chris\\Documents\\Github\\UNTITLED\\Calculator\\testmessages.txt", "r", encoding="utf8") as file:
    for i in file:
        lines.append(i.rstrip("\n"))
print("Done!")

# for i in lines:       # line by line
#     print(i)          # print the txt file