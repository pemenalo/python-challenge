import os
import csv

VOTER_COL = 0
COUNTY_COL = 1
CAND_COL = 2
Kpercent = 0
Cpercent = 0
Lpercent = 0
Opercent = 0

with open(os.path.join('PyPoll', 'Resources', 'election_data.csv')) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)    # Print Header Row
    # print(first_row)
    # vote_count = sum(1 for row in csv_reader)    # The total number of votes cast 
    # print(vote_count)
    K_votes = 0
    C_votes =0
    L_votes =0
    O_votes =0
    total_votes = 0
    # A complete list of candidates who received votes
    for row in csv_reader:
        total_votes = total_votes + 1
        if (row[CAND_COL] == "Khan"):
         K_votes = K_votes + 1
        elif (row[CAND_COL] == "Correy"):
            C_votes = C_votes + 1
        elif (row[CAND_COL] == "Li"):
            L_votes = L_votes + 1
        elif (row[CAND_COL] == "O'Tooley"):
            O_votes = O_votes + 1
        # The percentage of votes each candidate won
        Kpercent = K_votes/total_votes
        Cpercent = C_votes/total_votes
        Lpercent = L_votes/total_votes
        Opercent = O_votes/total_votes
    # The winner of the election based on popular vote.
        if K_votes > C_votes and K_votes > L_votes and K_votes > O_votes:
            Winner = "Khan"
        elif C_votes >K_votes and C_votes > L_votes and C_votes > O_votes:
            Winner = "Correy"
        elif L_votes > K_votes and L_votes > C_votes and L_votes > O_votes:
            Winner = "Li"
        elif O_votes > K_votes and O_votes > C_votes and O_votes >L_votes:
            Winner = "O'Tooley"
    #Print to the terminal
    print("Election Results")
    print(".........................")
    print("Total Votes " + str(total_votes))
    print(".........................")
    print("Khan: "+ str(round(Kpercent*100,2)) + "% ("+str(K_votes) +")")
    print("Correy: "+ str(round(Cpercent*100,2)) + "% ("+str(C_votes) +")")
    print("Li "+ str(round(Lpercent*100,2)) + "% ("+str(L_votes) +")")
    print("O'Tooley: "+ str(round(Opercent*100,2)) + "% ("+str(O_votes) +")")
    print(".........................")
    print("Winner: " + Winner)
    print(".........................")
#Print to a text file in analysis folder
output_path = os.path.join('PyPoll', 'Analysis', 'solved_election_data.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')
    #create header row and print rows
    csvwriter.writerow(['Election Results:\n'
    '------------------:\n'
    'Total Votes: '+ (str(total_votes)+')'), "\n"
    'Khan: '+ str(round(Kpercent*100,2)) + '% ' + '/Votes Received: ' + (str(K_votes) +')'), "\n"
    'Correy: '+ str(round(Cpercent*100,2)) + '% ' + '/Votes Received: ' + (str(C_votes) +')'), "\n"
    'Li: '+ str(round(Lpercent*100,2)) + '% ' + '/Votes Received: ' + (str(L_votes) +')'), "\n"
    'OTooley: '+ str(round(Opercent*100,2)) + '% ' + '/Votes Received: ' + (str(O_votes) +')'), "\n"
    '------------------:\n'
    'Election Winner: '+ Winner]), "\n"
    '------------------:\n'