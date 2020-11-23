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

