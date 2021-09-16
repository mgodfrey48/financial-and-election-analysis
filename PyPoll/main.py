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

    # set the first key in the candidates dictionary
    first_vote = next(csvreader)
    candidates[first_vote[2]] = 1
    
#TEST CODE ---------------------------------------

    # first_vote = next(csvreader)
    # print(first_vote)

    # candidates[first_vote[2]] = 1
    # print(candidates)

    # next_vote = next(csvreader)
    # print(next_vote)

    # candidates[next_vote[2]] = 1
    # print(candidates)

    # for row in csvreader:
    #     candidates[row[2]] += 1
    #     print(candidates)


#END TEST CODE -----------------------------------

    # read through each row of the data
    for row in csvreader:

        # store the candidate voted for
        voted_for = row[2]

        # add to total vote count
        total_votes += 1

        # check to see if the candidate voted for is already in the dictionary
        if voted_for in candidates:
            candidates[voted_for] += 1
        else:
            candidates[voted_for] = 1

        # if so, add 1 to the count for that candidate
            # candidates
        # if not, add the new candidate to the dictionary and set there count equal to 1 
        # for key in candidates:

        #     # If the vote matches a candidate, add 1 to the count of that candidate (the value associated to their key) 
        #     if voted_for == key:
        #         candidates[key] += 1
           
        #     # If the candidate is not found, add their name as a key to the dictionary of candidates,
        #     # set/create their count variable to 1 
        #     else:
        #         candidates[voted_for] = 1

    print(candidates)

            

        # next row

    # calculate percentages of votes each candidate got, store results

    # sort the candidates based on percentage of votes received, most to least

    # print results
