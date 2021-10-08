import os
import csv

VOTER_COL = 0
COUNTY_COL = 1
CAND_COL = 2

with open(os.path.join('PyPoll', 'Resources', 'election_data.csv')) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    voter_data = list(csvreader)
    first_row = next(csvreader)

    print(first_row)

    # next(csvreader)
    # first_row = next(csvreader)
    # print(first_row)

    # total_cast_votes = 0
    # voter_count = 0
    # candidate_list = 0


# The total number of votes cast
    # voter_count = 1
    # current_voter = int(first_row[VOTER_COL])
    # current_cand = (first_row[CAND_COL])
    # cand_total = current_cand
    # prev_cand = current_cand
    # for row in csvreader:
    #     #Total months, total, 
    #     voter_count += 1
    #     current_voter = row[VOTER_COL]
    #     current_cand = (row[CAND_COL])
    #     cand_total += current_cand
    #     print(f"Month Total: {voter_count}, Current Total: {cand_total}")

# A complete list of candidates who received votes
   

# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.

