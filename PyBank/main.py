import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
print(csvpath)
count = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        count = count + 1
print(count)

profit = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
            profit = sum(int(row))

    
#define analysis for outputs
total_months = count
print(f"Total Months = {count}")

# total_profit =
total_profit = profit
print(f"Total Profit = {profit}")

# avg_change_profit = 

# max_inc_profit =

# max_dec_losses = 

# print to terminal

# export as a .txt text file

