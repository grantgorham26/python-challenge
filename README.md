# python-challenge1
 
Pybank:

In the pybank challenge the goal of this project was to write a python script that would analyze financial records. The financial records include the profit/losses for specific months of a year. The scrip that was created obtained the total amount of months of financial records, the net profit/losses, the average change in profit/losses fro each month, the month with the  greatest increase in profits and the month with the greatest loss in profit.
When writing the code for pybank I had to first import os and csv to so i could read the provided csv file. Then I created 4 open list to sort the data into specific categories so it could be used for analysis. I then created a loop to add the data to the lists and obtain the number of months of the list as well as the total profit/loss. I used this #https://www.geeksforgeeks.org/sum-function-python/ to help sum the list. To find the change in profit between each month I created another loop that took a certain month then subtracted that from the previous month. To help create this loop I used xpert learning assistant. In this loop i was also able to find the greatest increase in profit by using the max function and the greatest decrease in profit by using he min function. I was also able to determine the specific date of the greatest increase and decrease by using the index function then apllying the index to the list of chang in profit. I then printed out the desired results then created a path to write a txt file that had the results. i used the write funtion to write the results into a txt file and \n to create new lines after each result. To help with creating new lines in the txt file I used https://stackoverflow.com/questions/11497376/how-do-i-specify-new-lines-in-a-string-in-order-to-write-multiple-lines-to-a-fil as a resource. 



Pypoll:

In the pypoll challenge the goal of the project was to help a small rural town count its votes for a political race but in a more modernized way. To achieve that i wrote them a python script that would loop through the data to count the voters so they wouldnt have to count them all by hand the old fashioned way. The script that I created is able to count the total number of votes cast, how many votes each specific candidate has and the percetage of their votes and determine the winner of the election.
