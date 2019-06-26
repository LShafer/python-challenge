import os
import csv
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

#set variables
total_votes = 0
candidate_list = []
percentage = 0
candidate_votes = []
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#open csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader, None)

    #calculate total votes
    for row in csvreader:
        total_votes += 1

    #list of candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

    #candidate votes
        if (row[2] == "Khan"):
            khan_votes += 1
        
        elif (row[2] == "Correy"):
            correy_votes += 1
            
        elif (row[2] == "Li"):
            li_votes += 1
            
        elif (row[2] == "O'Tooley"):
            otooley_votes += 1
           
    #percentage candidate/total_votes
    khan_percentage = khan_votes/total_votes
    correy_percentage = correy_votes/total_votes
    li_percentage = li_votes/total_votes
    otooley_percentage = otooley_votes/total_votes

    #print results
    print("Election Results")
    print("------------------------")
    print(f'Total Votes: {total_votes}')
    print("------------------------")
    print(f'Khan: {khan_percentage:.3%} ({khan_votes})')
    print(f'Correy: {correy_percentage:.3%} ({correy_votes})')
    print(f'Li: {li_percentage:.3%} ({li_votes})')
    print(f'OTooley: {otooley_percentage:.3%} ({otooley_votes})')
    print("------------------------------")

    #determine winner 
    winner = max(f'{khan_votes} {correy_votes} {li_votes} {otooley_votes}')
    if winner == khan_votes:
        print("Winner: " + "Khan")
    elif winner == correy_votes:
        print("Winner: " + "Correy")
    elif winner == li_votes:
        print("Winner: " + "Li")
    elif winner == otooley_votes:
        print("Winner: " + "O'Tooley")
        print("------------------------------")



    #output to election.txt
    file_output = "election.txt"

    print("Election Results")
    print("------------------------")
    print(f'Total Votes: {total_votes}')
    print("------------------------")
    print(f'Khan: {khan_percentage:.3%} ({khan_votes})')
    print(f'Correy: {correy_percentage:.3%} ({correy_votes})')
    print(f'Li: {li_percentage:.3%} ({li_votes})')
    print(f'OTooley: {otooley_percentage:.3%} ({otooley_votes})')
    print("------------------------------")


