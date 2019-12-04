# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

with open(csvpath, newline='') as election_data:

    # CSV reader specifies delimiter and variable that holds contents
    # csvreader = csv.reader(csvfile, delimiter=',')

    reader = csv.reader(election_data)
    # Read the header
    header = next(reader)

#row 2 because index starts with 0
    for row in reader: 
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
#Data mine the winner 
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
#Determine which candidate is winner
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        print (candidate, votes, vote_percentage)
    print (total_votes)
    print (winning_candidate)
    print (winning_count)
    


