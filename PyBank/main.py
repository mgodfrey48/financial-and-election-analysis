# import module for file paths
import os

# import module to read csv files
import csv

# import module to write txt file
import sys

# create file paths for the csv file and output.txt
budget_file_path = os.path.join("Resources", "budget_data.csv")
output_file_path = os.path.join("analysis", "output.txt")

# read the csv file
with open(budget_file_path, 'r') as csvfile:
    
    # create the csv reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # remove/store the header
    csv_header = next(csvreader)
    
    # define variables for calculations
    month_count = 0
    net_profit = 0
    previous_change = 0
    total_of_changes = 0
    average_change = 0
    greatest_increase = 0
    best_month = ''
    greatest_decrease = 0
    worst_month = ''

    # loop through the csv file an make calculations over the entire dataset/year
    for row in csvreader:
       
        # add to the month count
        month_count += 1
        
        # set the current month and change variables
        current_change = int(row[1])
        current_month = str(row[0])
        
        # add to the net profit/loss
        net_profit += current_change
    
        # calculate the difference between current month's change and the previous month's change
        # add the monthly change to the total of monthly changes
        monthly_change = current_change - previous_change
        total_of_changes += monthly_change

        # set the current change to be the previous_change for the next row
        previous_change = current_change

        # store the greatest increase in profits and the month associated with it
        if current_change > greatest_increase:
            greatest_increase = current_change
            best_month = current_month
        
        # store the greatest decrease in profits and the month associated with it
        if current_change < greatest_decrease:
            greatest_decrease = current_change
            worst_month = current_month

    # calculate the average change
    average_change = round(total_of_changes/month_count, 2)

    # print the summary table in terminal
    print('Financial Analysis')
    print('--------------------------------------')
    print(f'Total Months: {month_count}')
    print(f'Total: ${net_profit}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {best_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {worst_month} (${greatest_decrease})')

    # print the summary table in the output.txt file (sys.stdout found from a google search and explanation from kite.com)
    sys.stdout = open(output_file_path, 'w')
    print('Financial Analysis')
    print('--------------------------------------')
    print(f'Total Months: {month_count}')
    print(f'Total: ${net_profit}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {best_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {worst_month} (${greatest_decrease})')
    sys.stdout.close()