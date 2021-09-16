# import module for file path
import os

# import module to read csv file
import csv

# create file path for csv file
election_file_path = os.path.join('Resources', 'election_data.csv')

# open up the election data csv file
with open(election_file_path, 'r') as csvfile:

    # create the csv reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # store the header row
    csv_header = next(csvreader)

    # create a dictionary to store candidate info, and a variable to store the vote count
    candidate_vote_counts = {}
    total_votes = 0

    # read through each row of the data
    for row in csvreader:

        # store the candidate voted for
        voted_for = row[2]

        # add to total vote count
        total_votes += 1

        # check to see if the candidate voted for is already in the dictionary
        # if so, add 1 to the count for that candidate
        if voted_for in candidate_vote_counts:
            candidate_vote_counts[voted_for] += 1
        
        # if not, add the new candidate to the dictionary and set there count equal to 1 
        else:
            candidate_vote_counts[voted_for] = 1
    
    # create a dictionary to store the percentages of votes each candidate received
    candidate_vote_percentages = {}

    # calculate percentages of votes each candidate got, store results in voting percentage dictionary
    for key in candidate_vote_counts:
        candidate_vote_percentages[key] = '{:.3%}'.format(candidate_vote_counts[key]/total_votes) #this format function was found using stack overflow

    # define values to determine and store the winner of the election
    winning_vote_count = 0
    election_winner = ''

    # determine the highest vote count, and store the key associated with that count to the election winner variable
    for key, value in candidate_vote_counts.items():
        if value > winning_vote_count:
            winning_vote_count = value
            election_winner = key
    
    # print results
    print('Election Results')
    print('-------------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------------')
    for key in candidate_vote_percentages:
        print(f'{key}: {candidate_vote_percentages[key]} ({candidate_vote_counts[key]})')
    print('-------------------------------')
    print(f'Winner: {election_winner}')
    print('-------------------------------')
