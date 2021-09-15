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
    
    # add up the total number of months in the dataset

    # calculate net profit/loss over the entire period

    # change in profit/loss over the entire period, used to calculate
    # the average change

    # greatest increase in profits

    # greatest decrease in profits

    # print the summary table
