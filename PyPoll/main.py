import os
import csv
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

total_votes = 0
candidate_list = []
percentage = 0
candidate_votes = []
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csvheader = next(csvreader, None)
    print("Election Results")
    print("------------------------")

    for row in csvreader:
        total_votes += 1
        print(f'Total Votes: {total_votes}')
        #print("------------------------")

    #list of candidates
        #if row[2] not in candidate_list:
            #candidate_list.append(row[2])
        #print(f'{candidate_list}')

    #if candidate is on list then count until name changes
        if (row[2] == "Khan"):
            khan_votes += 1
            #delete this print when % is done
            print(f'Khan: {khan_votes}') 
        #elif (row[2] == "Correy"):
            #correy_votes += 1
            #print(f'Correy: {correy_votes}')
        #elif (row[2] == "Li"):
            #li_votes += 1
            #print(f'Li: {li_votes}')
        #else (row[2] == "O'Tooley"):
        #   otooley_votes += 1
        #   print(f'O'Tooley: {otooley_votes}')   
    
    #percentage candidate/total_votes
        khan_percentage = khan_votes/total_votes
        print(f'Khan: {khan_percentage:.3%} ({khan_votes})')
    
    #print("------------------------------")
    #winner max(total votes)
    #print("------------------------------")



    #output to election.txt


