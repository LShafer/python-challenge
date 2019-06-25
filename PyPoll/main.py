import os
import csv
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

total_votes = 0
candidate_list = []
percentage = 0
candidate_votes = []
winner = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csvheader = next(csvreader, None)
    print("Election Results")
    print("------------------------")

    for row in csvreader:
        total_votes += 1
        print(f'Total Votes: {total_votes}')
        print("------------------------")

    #list of candidate_list
    #append.row[] // column 3

    #if candidate is on list then count until name changes
    
    #percentage candidate/total_votes

    #winner max(total votes)

    #print 

    #output to election.txt


