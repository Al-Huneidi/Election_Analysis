# The data we need to retrieve.
# 1. Total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.



# Add dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize a list to be able to get names of candidates from file.
candidate_options = []

# Declare empty dictionary of candidate names and votes for each.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file:
with open(file_to_load) as election_data:

    # To do:  read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read the header row.
    headers = next(file_reader)
    
# Print each row in the CSV file.
    for row in file_reader:    

        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate name does not match an existing candidate on the list.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Create each candidate as a key to keep track of the votes for each candidate.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Save the results to the text file, election_analysis.txt
    with open(file_to_save, "w") as txt_file:
        election_results = (f"\nElection Results\n---------------\nTotal Votes: {total_votes}\n---------------\n")
        print(election_results, end="")
        txt_file.write(election_results)
            
        # Determine the percentage of votes for each candidate by looping through the vote counts.
        # Iterate through the candidate list.
        for candidate in candidate_votes:

            # Collect the vote count of a candidate.
            votes = candidate_votes[candidate]

            # Calculate the percentage of votes received for each candidate.
            vote_percentage = float(votes) / float(total_votes) * 100

            # Print the candidate name, vote count and percentage of votes to text file, election_analysis.txt.
            candidate_results = (f"{candidate}: ({votes:,}) {vote_percentage:.1f}%\n")
            print(candidate_results, end="")
            txt_file.write(candidate_results)


            # Determine winning vote count and candidate
            # Determine of the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true then set winning_count = votes and winning_percent = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage

                # Set the wining_candidate equal to the candidate's name.
                winning_candidate = candidate

        # Announce the Winning Candidate, their total votes, and the percentage of their votes.
        winning_candidate_summary = (f"---------------\nWinner: {winning_candidate}\nWinning Vote Count: {winning_count}\nWinning Percentage: {winning_percentage:.1f}%\n---------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
    


    


    



