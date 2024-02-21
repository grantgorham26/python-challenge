#import os and csv to read files 
import csv
import os 


#create list to store different data from the list 
ballotid = []
candidate = []

#create an empty dcitionary thats contains each candidate and how many times they are voted for
candidate_counter_dict = {}

election_csv = os.path.join('..','resources','election_data.csv')
with open(election_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #creates a list of the voter ids 
        ballotid.append(row[0])
        #measures the amount of voter id, giving the total vote count
        num_voters= len(ballotid)
        # creates a list of the candidates 
        candidate.append(row[2])
        #create a variable for candidate name
        candidate_name = row[2]
        #create two list with unique candiates and there votes 
        unique_candidate_list = list(candidate_counter_dict.keys())
        unique_candidate_list_votes = list(candidate_counter_dict.values())

        #
        if candidate_name in candidate_counter_dict:
            candidate_counter_dict[candidate_name] = candidate_counter_dict[candidate_name] + 1
        else:
            candidate_counter_dict[candidate_name] = 1
        

            
    vote_count_charles = candidate_counter_dict['Charles Casper Stockham']
    vote_count_diana = candidate_counter_dict['Diana DeGette']
    vote_count_raymon = candidate_counter_dict['Raymon Anthony Doane']
    percent_vote_charles = round((vote_count_charles/num_voters)*100,2)
    percent_vote_diana = round((vote_count_diana/num_voters)*100,2)
    percent_voters_raymon = round((vote_count_raymon/num_voters)*100,2)
    highest_vote_count = max(unique_candidate_list_votes)
    highest_vote_candidate_index = unique_candidate_list.index(max(highest_vote_count))



print(highest_vote_count)

print('Election Results')
print('---------------------------------------')
print(f'total votes: {num_voters}')
print('---------------------------------------')
print(f'{unique_candidate_list[0]}: {percent_vote_charles}% ({vote_count_charles})')
print(f'{unique_candidate_list[1]}: {percent_vote_diana}% ({vote_count_diana})')
print(f'{unique_candidate_list[2]}: {percent_voters_raymon}% ({vote_count_raymon})')
print('---------------------------------------')
print(f'Winner: {unique_candidate_list[highest_vote_candidate_index]}')
print('---------------------------------------')