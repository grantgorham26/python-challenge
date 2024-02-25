#import os and csv to read files 
import csv
import os 


#create list to store different data from the list 
ballotid = []
candidate = []

#create an empty dcitionary thats contains each candidate and how many times they are voted for
candidate_counter_dict = {}

election_csv = os.path.join('resources','election_data.csv')
with open(election_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #since there is headers we need to skip those when reading it
    header = next(csvreader)
    #loop through the csvfile to add to the open lists
    for row in csvreader:
        #creates a list of the voter ids 
        ballotid.append(row[0])
        #measures the amount of voter id, giving the total vote count
        num_voters= len(ballotid)
        # creates a list of the candidates 
        candidate.append(row[2])
        #create a variable for candidate name
        candidate_name = row[2]
        #convert the dictionary into two list with unique candiates and there amount of votes
        #i used https://www.tutorialspoint.com/How-to-convert-Python-Dictionary-to-a-list 
        #to help convert the open dictinary to two seperate list based on whether they were keys or values
        #having these values and strings in separate list will be useful for finding the winner and percentage of votes in favor of a candidate 
        unique_candidate_list = list(candidate_counter_dict.keys())
        unique_candidate_list_votes = list(candidate_counter_dict.values())

        #used kevins extra examples to create a counter that puts each name into a dictionary
        if candidate_name in candidate_counter_dict:
            candidate_counter_dict[candidate_name] = candidate_counter_dict[candidate_name] + 1
        else:
            candidate_counter_dict[candidate_name] = 1
#obtain the max amount of votes from list of amount of votes from the counter dictionary            
highest_vote_count = max(unique_candidate_list_votes)
#obtain index of the candidate with highest votes
index_of_winner = unique_candidate_list_votes.index(max(unique_candidate_list_votes))
#obtain name of winner from list
winning_candidate = unique_candidate_list[index_of_winner]

#print out results to terminal
print('Election Results')
print('---------------------------------------')
print(f'total votes: {num_voters}')
print('---------------------------------------')
#use a loop to print out each candidates results so dont have to do it 2 extra times         
for i in range(len(unique_candidate_list)):
    percent_of_votes = round((unique_candidate_list_votes[i]/num_voters)*100,3)
    print(f'{unique_candidate_list[i]}: {percent_of_votes}% ({unique_candidate_list_votes[i]})')
print('---------------------------------------')
print(f'Winner: {winning_candidate}')
print('---------------------------------------')   

#write the results into a separate txt file 
#used day 2 activity 10 and activtiy 12 to help write the code to write the files into a new txt file
output_path = os.path.join('analysis','Poll_Results_analysis.txt')
with open(output_path,'w') as txtfile:
    txtfile.write('Election Results')
    txtfile.write('---------------------------------------')
    txtfile.write(f'total votes: {num_voters}')
    txtfile.write('---------------------------------------')        
    for i in range(len(unique_candidate_list)):
        percent_of_votes = round((unique_candidate_list_votes[i]/num_voters)*100,3)
        txtfile.write(f'{unique_candidate_list[i]}: {percent_of_votes}% ({unique_candidate_list_votes[i]})')
    txtfile.write('---------------------------------------')
    txtfile.write(f'Winner: {winning_candidate}')
    txtfile.write('---------------------------------------')
        

