#import modules to read and opne csv files 
import os
import csv
#create list to store data from csv file
date = []
profit = []
profit_change = []

#path to collect data from specified folder
budget_csv= os.path.join('..','resources','budget_data.csv')
# open the csv file and read it 
with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #since there is headers we need to skip those when reading it
    header = next(csvreader)
    #loop through the csv file to add to the open lists
    for row in csvreader:
        #add date 
        date.append(row[0])
        #this gives the total number of months in the list
        num_months = len(date)
        #add total to a list and convert to an integer since its a string and i want a number
        profit.append(int(row[1]))
        #this sums the losses and profits of the list 
        #https://www.geeksforgeeks.org/sum-function-python/ this is where i got code
        total_profits= sum(profit)
        

            
#change in profit/loss is the specific month minus the previous month, ex: profit[1]-profit[0], 
#or final profit minus the inital profit and then add that to a list and then take the average of that list
#used xpert leaning assistant to help find this out. i asked it how to loop through a list of and find the 
#change between the numbers
    for i in range(1,len(profit)):
        change = profit[i]- profit[i-1]
        #add the profit change through a month to a new list 
        profit_change.append(change)
        avgprofitchange = (sum(profit_change))/(len(profit_change))
        #use the max function to find the greatest increase
        greatest_increase_profit = max(profit_change)
        #use the index function to find the index in the list where greatest increase is to match it up with the date
        index_greatest_increase= profit_change.index(max(profit_change))
        #use the max function to find the greatest decrease
        greatest_decrease_profit = min(profit_change)
        #use the index function to find the index in the list where greatest decrease is to match it up with the date
        index_greatest_decrease= profit_change.index(min(profit_change))

#print out results to terminal        
print('Financial Analysis')
print('---------------------------')
#this gives the total number of months in the list
print(f'Total Months: {num_months}')
#this sums the losses and profits of the list 
print(f'Total: ${total_profits}')
print(f'Average Change: ${round(avgprofitchange,2)}')
#need a plus one to make it correct 
print(f'Greatest Increase in Profits: {date[index_greatest_increase+1]} (${greatest_increase_profit})')
#need a plus one to make it correct 
print(f'Greatest Decrease in Profits: {date[index_greatest_decrease+1]} (${greatest_decrease_profit})')




#write the results into a separate txt files
#used day 2 activity 10 and activtiy 12 to help write the code to write the files into a new txt file
output_path = os.path.join('..','analysis','Budget_analysis.txt')
with open(output_path,'w') as txtfile:
    txtfile.write('Financial Analysis')
    txtfile.write('---------------------------')
    txtfile.write(f'Total Months: {num_months}')
    txtfile.write(f'Total: ${total_profits}')
    txtfile.write(f'Average Change: ${round(avgprofitchange,2)}')
    txtfile.write(f'Greatest Increase in Profits: {date[index_greatest_increase+1]} (${greatest_increase_profit})')
    txtfile.write(f'Greatest Decrease in Profits: {date[index_greatest_decrease+1]} (${greatest_decrease_profit})')
    