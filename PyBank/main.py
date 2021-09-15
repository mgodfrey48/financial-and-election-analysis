# import module for file paths
import os

# import module to read csv files
import csv

# create file path
file_path = os.path.join("Resources", "budget_data.csv")

# read the csv file
with open(file_path) as csvfile:
    
    # create the csv reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # remove/store the header
    csv_header = next(csvreader)
    
    # define variables for calculations
    month_count = 0
    net_profit = 0
    previous_month = 0
    greatest_increase = 0
    best_month = ''
    greatest_decrease = 0
    worst_month = ''

    # loop through the csv file an make calculations over the entire dataset/year
    for row in csvreader:
       
        # add to the month count
        month_count += 1
        
        current_change = int(row[1])
        current_month = str(row[0])
        
        # add to the net profit/loss
        net_profit += current_change
    
        # changes in profit/loss over the entire period, used to calculate
        # the average change
        

        # greatest increase in profits
        if current_change > greatest_increase:
            greatest_increase = current_change
            best_month = current_month
        
        # greatest decrease in profits
        if current_change < greatest_decrease:
            greatest_decrease = current_change
            worst_month = current_month

    # print the summary table
    print(f'Total Months: {month_count}')
    print(f'Total: ${net_profit}')
    print(f'Greatest Increase in Profits: {best_month} ${greatest_increase}')
    print(f'Greates Decrease in Profits: {worst_month} ${greatest_decrease}')




