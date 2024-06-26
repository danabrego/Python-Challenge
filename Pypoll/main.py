import os
import csv

#set path

PyPollcsv = os.path.join('Pypoll','Resources','election_data.csv')

# variables/lists

count = 0
candidatelist = []
uniquecandidate = []
votecount = []
votepercent = []


with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    

    for row in csvreader:

        # calcualte votes and percentages for candidates
        count = count + 1
        candidatelist.append(row[2])
        
    for x in set(candidatelist):
        uniquecandidate.append(x)
        
        candidatecount = candidatelist.count(x)
        votecount.append(candidatecount)
        
        candidatepercent = (candidatecount/count)*100
        votepercent.append(candidatepercent)
        
    winning_vote_count = max(votecount)
    winner = uniquecandidate[votecount.index(winning_vote_count)]
    
 #print in terminal
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(uniquecandidate)):
            print(uniquecandidate[i] + ": " + str(votepercent[i]) +"% (" + str(votecount[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

#print in txt file 

electionfile = os.path.join("Pypoll","Analysis", "analysis.txt")
with open(electionfile, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("---------------------------------------\n")
    outfile.write("Total Vote: " + str(count) + "\n")
    outfile.write("---------------------------------------\n")
    for i in range(len(set(uniquecandidate))):
        outfile.write(uniquecandidate[i] + ": " + str(votepercent[i]) +"% (" + str(votecount[i]) + ")\n")
    outfile.write("---------------------------------------\n")
    outfile.write("The winner is: " + winner + "\n")
    outfile.write("---------------------------------------\n")

