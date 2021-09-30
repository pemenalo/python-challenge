# Your task is to create a Python script that analyzes the records to calculate each of the following:

#import the csv file 
import os

import csv

with open(r'\Users\hitst\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    totalmonths = len(list(csvreader))
    
    print(totalmonths - 1)





# The total number of months included in the dataset


# The net total amount of "Profit/Losses" over the entire period


# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in profits (date and amount) over the entire period