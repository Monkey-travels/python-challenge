#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Vote count & election result

#Dependencies
import csv
import os

#Files to load and output
file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("election_analysis.txt")

#Total vote counter
total_votes = 0

#Candidate options and vote counter
candidate_options = []
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0

#Read the csv and convert it into a list
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    #read the header
    header = next(reader)
    
    for row in reader:
        
        #add to total vote count
        total_votes = total_votes + 1
        
        #extract the candidate name from each row
        candidate_name = row[2]
        
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #add it to the list of candidates in the running
            candidate_options.append(candidate_name)  
            #start tracking the candidate voter count
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
with open(file_to_output, "w") as txt_file:
    #run the final vote count 
    
    election_results = (
        "Election Results\n" +
        "------------------------------\n" +
        "Total Votes: " + str(total_votes) + "\n"+
        "------------------------------\n" 
    )

    print(election_results, end="")

    #save the final vote count to text file
    txt_file.write(election_results)
    
    #Determine the winner by looping through the counts
    for candidate in candidate_votes:
        
        #Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #Determine winning vote count and candidate
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        #Print each candidates' voter count and percentage to terminal
        voter_output = f"{candidate}: {vote_percentage: .3f}% ({votes})\n"
        
        print(voter_output, end="")
        
        txt_file.write(voter_output)
        
    #Print the winning candidates
    winning_candidate_summary = (
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"------------------------------\n"
    )
    print(winning_candidate_summary)
    
    #Save the winning candidate name to text file
    txt_file.write(winning_candidate_summary)
            


# In[ ]:




