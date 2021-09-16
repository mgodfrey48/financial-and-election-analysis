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
    candidates = {}
    total_votes = 0
    
#TEST CODE ---------------------------------------

    first_vote = next(csvreader)
    print(first_vote)

    candidates[first_vote[2]] = 1
    print(candidates)

    next_vote = next(csvreader)
    print(next_vote)

    candidates[next_vote[2]] = 1
    print(candidates)


#END TEST CODE -----------------------------------




    # read through each row of the data
    # for row in csvreader:

        # store the candidate voted for
        # voted_for = row[2]
        # print(voted_for)

        # if no votes have been counted yet (aka the candidate dictionary is empty), create
        # the first entry in the dictionary
        # if total_votes == 0:
        #     candidates = {row[2] : 1}

        # # add to total vote count
        # total_votes += 1

        # search the candidate dictionary for the vote recipient   
        # for key in candidates:

            # If the vote matches a candidate, add 1 to the count of that candidate (the value associated to their key) 
            # if row[2] == key:
            #     candidates[key] += 1
            # else:
            #     candidates[row[2]]

            # If the candidate is not found, add their name as a key to the dictionary of candidates,
            # set/create their count variable to store as the key and add to the count 


        # next row

    # calculate percentages of votes each candidate got, store results

    # sort the candidates based on percentage of votes received, most to least

    # print results
