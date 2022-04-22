import re
# import pandas

class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score

lines = []

with open("testmessages.txt", "r", encoding="utf8") as file:
    for i in file:
        lines.append(i.rstrip("\n"))

# for i in lines:       # line by line
#     print(i)          # print the txt file

# morse was here 2
# and chris said hi