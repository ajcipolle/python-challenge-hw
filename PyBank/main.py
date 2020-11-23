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
            profit = profit + int(row[1])


first_month = [0]
next_month = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        # avg_change_profit = sum(int(row[1]) - int((row - 1)[1]))/86
        first_month.append(row[1])
    for row in csvreader:
        next_month.append(row[1])
next_month.append(0)

print(first_month)
print(next_month)


#define analysis for outputs
total_months = count
print(f"Total Months = {count}")

# total_profit =
total_profit = profit
print(f"Total Profit = {profit}")

# avg_change_profit = 
print(f"Average Monthly Change In Profit = {avg_change_profit}")
# max_inc_profit =

# max_dec_losses = 

# print to terminal

# export as a .txt text file

