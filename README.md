# python-challenge
 
Pybank:
![revenue-per-lead](https://github.com/grantgorham26/python-challenge/assets/154031840/fc92c94d-fd8a-4849-bbb4-efdeea97d220)


In the pybank challenge the goal of this project was to write a python script that would analyze financial records. The financial records include the profit/losses for specific months of a year. The scrip that was created obtained the total amount of months of financial records, the net profit/losses, the average change in profit/losses fro each month, the month with the  greatest increase in profits and the month with the greatest loss in profit.
When writing the code for pybank I had to first import os and csv to so i could read the provided csv file. I used the code from day 2 activity 8 and 9 to help write this portion. Then I created 4 open list to sort the data into specific categories so it could be used for analysis. To guide me through that portion I used day 3 actvity 4 and 5. I then created a loop to add the data to the lists and obtain the number of months of the list as well as the total profit/loss. I used this #https://www.geeksforgeeks.org/sum-function-python/ to help sum the list. To find the change in profit between each month I created another loop that took a certain month then subtracted that from the previous month. To help create this loop I used xpert learning assistant. In this loop i was also able to find the greatest increase in profit by using the max function and the greatest decrease in profit by using he min function. I was also able to determine the specific date of the greatest increase and decrease by using the index function then apllying the index to the list of chang in profit. I then printed out the desired results then created a path to write a txt file that had the results. i used the write funtion to write the results into a txt file and \n to create new lines after each result. To help with creating new lines in the txt file I used https://stackoverflow.com/questions/11497376/how-do-i-specify-new-lines-in-a-string-in-order-to-write-multiple-lines-to-a-fil as a resource. 



Pypoll:
![Vote_counting](https://github.com/grantgorham26/python-challenge/assets/154031840/3d562225-cb23-45b9-b7b8-4aaf514b296d)


In the pypoll challenge the goal of the project was to help a small rural town count its votes for a political race but in a more modernized way. To achieve that i wrote them a python script that would loop through the data to count the voters so they wouldnt have to count them all by hand the old fashioned way. The script that I created is able to count the total number of votes cast, how many votes each specific candidate has and the percetage of their votes and determine the winner of the election.
To start the code for pypoll I again imported os and csv to rea the provided cvs file. Activity 8 and 9 from day 2 were used to help write this code. I created 2 open lists to stroe the candidate and ballot id. I used he ballot id list to count the total number of voters. I also created an open dictionary to store the candidates names and the amount of votes with that specfic name. To add the data to the list I created a loop that read through the csv file then added the ballot id and candidate names to separate list. After creating the lists I added the candidate names and number of votes to the open dictionary. To right this code I used the example that Kevin showed us at the end of the third class on python. After adding all the names and the amount of votes to the dictionary I created 2 new list. The first list was composed of the keys of the dictionary and the second list was composed of the values of the dictionary. To convert the dictinary to list I used https://www.tutorialspoint.com/How-to-convert-Python-Dictionary-to-a-list this as a guide. To determine the winner I used the max function and applied it to the the list of the number of votes. To associate the name with the max votes I applied the index function to the max votes and used the index in the unique candiates list. I printed out the results to the terminal and used another loop to print out the percentage by using the two list I created from the dictionary. To write the results into a separate txt file I used the same method as the pybank challenge. 
