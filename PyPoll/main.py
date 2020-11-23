#import dependencies
import os
import csv


# count the number of rows exluding header
csvpath = os.path.join("Resources","election_data.csv")
print(csvpath)
vote_count = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        vote_count = vote_count + 1
print(f"Total Votes: {vote_count}")

candidates = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        candidates.append(row[2])
# print(candidates)
candidates_set = set(candidates)
print(candidates_set)


khan = 0
li = 0
correy = 0
otooley = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        if row[2] == "Khan":
            khan = khan + 1
print(f"Khan: (percentage), ({khan}) votes")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        if row[2] == "Li":
            li = li + 1
print(f"Li: (percentage), ({li}) votes")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        if row[2] == "Correy":
            correy = correy + 1
print(f"Correy: (percentage), ({correy}) votes")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        if row[2] == "O'Tooley":
            otooley = otooley + 1
print(f"Correy: (percentage), ({otooley}) votes")