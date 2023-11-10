#Rutgers Boot Camp - Module 3 Challenge - Python script to modernize its vote-counting process.
#Bhagya Prasad

#PREREQUISITES
#Source Input file = election_data.csv
#Source File directory where election_data.csv is stored needs to be replaced as per the environment
#Summary Putfile File directory where Election_Results.txt is generated needs to be replaced as per the environment

#Python Code starts here

# Import Dependencies Section
import os, csv
from pathlib import Path 

#File Handling Section
sourcefile = Path("/Users/babloo/Documents/rutgers/Module3", "PyPoll/resources", "election_data.csv")
summaryfile = Path("/Users/babloo/Documents/rutgers/Module3", "PyPoll/resources", "Election_Results_Summary.txt")


# Declare Variables Section
totalVotes = 0 
charlesVotes = 0
dianaVotes = 0
raymonVotes = 0

# Storing CSV Data Section
with open(sourcefile,newline="", encoding="utf-8") as pollingData:

    pollingReader = csv.reader(pollingData,delimiter=",") 

    # Storing data taking the header out
    header = next(pollingReader)     

    for row in pollingReader: 

        totalVotes +=1

        if row[2] == "Charles Casper Stockham": 
            charlesVotes +=1
        elif row[2] == "Diana DeGette":
            dianaVotes +=1
        elif row[2] == "Raymon Anthony Doane": 
            raymonVotes +=1

 # Determine the winner by creating dictionary out of the two lists created before 
candidatesList = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votesList = [charlesVotes, dianaVotes,raymonVotes]

candidatesVotesDict = dict(zip(candidatesList,votesList))
winner = max(candidatesVotesDict, key=candidatesVotesDict.get)

# Percentage Calculation Section
charlesPercent = (charlesVotes/totalVotes) *100
dianaPercent = (dianaVotes/totalVotes) * 100
raymonPercent = (raymonVotes/totalVotes)* 100

# Print Console Output Section
print(f"Election Results")
print(f"--------------------------------------")
print(f"Total Votes: {totalVotes}")
print(f"--------------------------------------")
print(f"Charles Casper Stockham: {charlesPercent:.3f}% ({charlesVotes})")
print(f"Diana DeGette: {dianaPercent:.3f}% ({dianaVotes})")
print(f"Raymon Anthony Doane: {raymonPercent:.3f}% ({raymonVotes})")
print(f"--------------------------------------")
print(f"Winner: {winner}")
print(f"--------------------------------------")

# Summary File Section

with open(summaryfile,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"--------------------------------------")
    file.write("\n")
    file.write(f"Total Votes: {totalVotes}")
    file.write("\n")
    file.write(f"--------------------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {charlesPercent:.3f}% ({charlesVotes})")
    file.write("\n")
    file.write(f"Diana DeGette: {dianaPercent:.3f}% ({dianaVotes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {raymonPercent:.3f}% ({raymonVotes})")
    file.write("\n")
    file.write(f"--------------------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"--------------------------------------")
    