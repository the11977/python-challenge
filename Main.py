# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Improved Reading using CSV module


total_month = 0
total_net = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    header = next(csvreader)
    #print(f"CSV Header: {csvheader}")

    first_row = next(csvreader)
    total_month = total_month + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        total_month = total_month + 1
        total_net = total_net + int(row[1])
 # Track the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]
        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
    net_monthly_average = sum(net_change_list)/len(net_change_list)

    print (total_month)
    print (total_net)
    print (net_monthly_average)
    print (greatest_increase[0], greatest_increase[1])
    print (greatest_decrease[0], greatest_decrease[1])