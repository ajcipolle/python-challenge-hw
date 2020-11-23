#import dependencies
import os
import csv


# count the number of rows exluding header
csvpath = os.path.join("Resources","budget_data.csv")
print(csvpath)
count = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        count = count + 1
# print(count)

# sum the totals of the second column 
profit = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
            profit = profit + int(row[1])
#initialize two lists for next month and this month
first_month = [0]
next_month = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        first_month.append(row[1])
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)    
    for row in csvreader:
        next_month.append(row[1])
#make sure each list is the same length
next_month.append(0)

# # check month lists if need be
# print(f"first month {first_month}")
# print(f"next month {next_month}")

#initialize list for tracking monthly changes
change_profit = []
#fill list with differences from next month to this month
for i in range(len(next_month)):
    change_profit.append(int(next_month[i]) - int(first_month[i]))

#remove first and last items of list of profit changes
change_profit.pop(0)
change_profit = change_profit[:-1]

# # check the full list of monthly changes to profit
# print(f"Monthly list of change in profit = {change_profit}")

#Define avg, min and max monthly profit changes
avg_change_profit = sum(change_profit) / len(change_profit)
max_change_profit = max(change_profit)
min_change_profit = min(change_profit)

# print to terminal
print("PyBank Monthly Profits Analysis:" + "\n" + "**************")

#total months
total_months = count
print(f"Total Months = {count}")

# total_profit =
total_profit = profit
print(f"Total Profit = {profit}")

# avg_change_profit = 
print(f"Average Monthly Change in Profits = {avg_change_profit}")

# max_inc_profit =
print(f"Maximum Monthly Increase in Profits = {max_change_profit}")
# max_dec_losses = 
print(f"Maximum Monthly decrease in Profits = {min_change_profit}")


# export as a .txt text file
import sys
sys.stdout = open("Analysis/pybank_analysis.txt", "w")
print("PyBank Monthly Profits Analysis:" + "\n" + "**************")

#total months
total_months = count
print(f"Total Months = {count}")

# total_profit =
total_profit = profit
print(f"Total Profit = {profit}")

# avg_change_profit = 
print(f"Average Monthly Change in Profits = {avg_change_profit}")

# max_inc_profit =
print(f"Maximum Monthly Increase in Profits = {max_change_profit}")
# max_dec_losses = 
print(f"Maximum Monthly decrease in Profits = {min_change_profit}")
