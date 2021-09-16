# import module for file path
import os

# import module to read csv file
import csv

# create file path for csv file
election_file_path = os.path.join('Resources', 'election_data.csv')

# create variables and/or dictionaries
candidates = {}

# open up the election data csv file
with open(election_file_path, 'r') as csvfile:

    # create the csv reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # store the header row
    csv_header = next(csvreader)
    
    # read through each row of the data
    for row in csvreader:
        print(row)

        # check the name of the candidate: if new, add their name to the dictionary of candidates
        # crete their count variable and add to their count. If not new, add one to the candidate's count.

        # next row

    # total up all of the votes

    # calculate percentages of votes each candidate got, store results

    # sort the candidates based on percentage of votes received, most to least

    # print results
