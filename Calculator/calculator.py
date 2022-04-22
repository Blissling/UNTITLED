import re
# import pandas

class User:                                                         # User class to be used later in order to attach scores to individual user objects
    def __init__(self, name, score):
        self.name = name
        self.score = score

lines = []

with open("testmessages.txt", "r", encoding="utf8") as file:        # Access text file
    for i in file:                                                  # Append each line in the text file as an index in a list variable
        lines.append(i.rstrip("\n"))                                # .rstrip("\n") prevents it from adding a new line at the end of the string

# for i in lines:       # line by line
#     print(i)          # print the txt file

