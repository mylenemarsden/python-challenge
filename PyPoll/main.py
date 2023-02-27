import pandas as pd

# Read the csv into a dataframe
pypoll_data = pd.read_csv("Resources/election_data.csv")

# Calculate total votes
total_votes = len(pypoll_data)

# Create dataframe for candidates and their votes count
candidates = pd.DataFrame({
    "names": ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"],
    "votes": [0, 0, 0],
    "percent": [0, 0, 0]
})

# Iterate through the election data and count votes for each candidate
for x in range(len(pypoll_data)):
    if pypoll_data.loc[x, "Candidate"] == "Charles Casper Stockham":
        candidates.loc[0,"votes"] += 1
    elif pypoll_data.loc[x, "Candidate"] == "Diana DeGette":
        candidates.loc[1,"votes"] += 1
    else:
        candidates.loc[2,"votes"] += 1

# Calculate percentage of votes
candidates["percent"] = candidates["votes"]/total_votes * 100

# Take the candidate with the most votes as the winner
winner = candidates.loc[candidates["votes"].idxmax(), "names"]
    
# Print analysis to terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Charles Casper Stockham: {'%.3f'%candidates.loc[0, 'percent']}% ({candidates.loc[0, 'votes']})")
print(f"Diana DeGette: {'%.3f'%candidates.loc[1, 'percent']}% ({candidates.loc[1, 'votes']})")
print(f"Raymon Anthony Doane: {'%.3f'%candidates.loc[2, 'percent']}% ({candidates.loc[2, 'votes']})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

# Write analysis into text file
with open("analysis/analysis.txt", "w") as f:
    f.write(f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\nCharles Casper Stockham: {'%.3f'%candidates.loc[0, 'percent']}% ({candidates.loc[0, 'votes']})\nDiana DeGette: {'%.3f'%candidates.loc[1, 'percent']}% ({candidates.loc[1, 'votes']})\nRaymon Anthony Doane: {'%.3f'%candidates.loc[2, 'percent']}% ({candidates.loc[2, 'votes']})\n-------------------------\nWinner: {winner}\n-------------------------")