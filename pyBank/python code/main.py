#import modules to read and opne csv files 
import os
import csv
#create list to store data from csv file
date = []
total = []
profit_change = []
#set variables



    
    

#path to collect data from specified folder
budget_csv= os.path.join('..','resources','budget_data.csv')
# open the csv file and read it 
with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #add date 
        date.append(row[0])
        #this gives the total number of months in the list
        num_months = len(date)
        #add total to a list and convert to an integer since its a string and i want a number
        total.append(int(row[1]))
        #this sums the losses and profits of the list 
        #https://www.geeksforgeeks.org/sum-function-python/ this is where i got code
        total_profits= sum(total)
        #change in profit is the specific month minus the previous month, ex: profit[1]-profit[0], or final profit minus the inital profit and then add that to a list and then take the average of that list
        


        



        

#this gives the total number of months in the list
print(num_months)
#this sums the losses and profits of the list 
print(total_profits)


