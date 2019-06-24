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

    
