# 1. Total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.
# 6. A complete list of all the counties.
# 6. The total number of votes for each county.
# 7. The percentage of voter turnout for each county.
# 8. The county with the largest voter turnout.


# Add dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Initialize a total vote counter per county.
total_county_votes = 0


# Initialize a list to be able to get names of candidates from file.
candidate_options = []
# Initialize a list to be able to get names of counties from file.
county_options = []


# Declare empty dictionary of candidate names and votes for each candidate.
candidate_votes = {}
# Declare empty dictionary of county names and votes for each county.
county_votes = {}


# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County with the most votes
largest_county_name = ""
largest_county_count = 0
largest_county_percentage = 0

# Open the election results and read the file:
with open(file_to_load) as election_data:

    # To do:  read and analyze the data here for candidates.
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

        # If the candidate name does not match an existing candidate on the list then add to the list of candidates.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            
            # Create each candidate as a key to keep track of the votes for each candidate.
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
            

    # Save the election results to the text file, election_analysis.txt
    with open(file_to_save, "w") as txt_file:
        election_results = (f"\nElection Results\n---------------\nTotal Votes: {total_votes}\n---------------\n")
        print(election_results, end="")
        txt_file.write(election_results)


# Open the election results and read the file:
with open(file_to_load) as election_data:

    # To do:  read and analyze the data here for the counties.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total county votes count.
        total_county_votes +=1

        # Print the county name from each row.
        county_name = row[1]

        # If the county name does not match an existing county on the list then add to the list of counties.
        if county_name not in county_options:

            # Add the county name to the county list.
            county_options.append(county_name)

            # Create each county as a key to keep track of the votes for each county.
            county_votes[county_name] = 0

        # Add a vote to that county's count.
        county_votes[county_name] += 1
    
    # Determine the county with the biggest turnout of voters by looping through the vote counts for each county.
    # Iterate through the county list.
    for county in county_votes:

        # Collect the total voter turnout.
        total_county_votes = county_votes[county]

        # Calculate the percentage of votes received for each county.
        county_vote_percentage = float(total_county_votes) / float(total_votes) * 100

        # Determine the county with the largest turnout of voters.
        # Determine if the votes are greater than the largest number of voters.
        if (total_county_votes > largest_county_count) and (county_vote_percentage > largest_county_percentage):

            # If true then set Largest_county_count equal to votes and largest_county_percentage = county_vote_percentage.
            largest_county_count = total_county_votes
            largest_county_percentage = county_vote_percentage

            # Set the county with largest voter turn out to name of county.
            largest_county_name = county

    # Print the name of the county with the largest turnout.
    with open(file_to_save, "w") as txt_file:
        largest_county_turnout = (f"---------------\nLargest County Turnout: {county_name}\n---------------\n")
        print(largest_county_turnout, end="")
        txt_file.write(largest_county_turnout)
 
    # Print the county names, vote count and percentage of votes for each to text file, election_analysis.txt.
    with open(file_to_save, "w") as txt_file:
        county_results = (f"{county}: ({total_county_votes:,}) {county_vote_percentage:.1f}%\n")
        print(county_results, end="")
        txt_file.write(county_results)   

    # Determine the percentage of votes for each candidate and each county by looping through the vote counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:

        # Collect the vote count of a candidate.
        votes = candidate_votes[candidate]
            

        # Calculate the percentage of votes received for each candidate.
        vote_percentage = float(votes) / float(total_votes) * 100
            

        # Determine winning vote count and candidate.
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            # Set the wining_candidate equal to the candidate's name.
            winning_candidate = candidate

    
        
    # Print the candidate name, vote count and percentage of votes to text file, election_analysis.txt.
    with open(file_to_save, "w") as txt_file:
        candidate_results = (f"{candidate}: ({votes:,}) {vote_percentage:.1f}%\n")
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    # Announce the Winning Candidate, their total votes, and the percentage of their votes to text file, election_analysis.txt.
    with open(file_to_save, "w") as txt_file:
        winning_candidate_summary = (f"---------------\nWinner: {winning_candidate}\nWinning Vote Count: {winning_count}\nWinning Percentage: {winning_percentage:.1f}%\n---------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

    


    


    



