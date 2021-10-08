# Your task is to create a Python script that analyzes the records to calculate each of the following:

#import the csv file 
import os
import csv
from types import prepare_class

DATE_COL = 0
PL_COL = 1
with open(os.path.join('PyBank', 'Resources', 'budget_data.csv')) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)    # Discard header row
    month_count = 0 
    maxchange_value = 0
    minchange_value = 0 
    total_change = 0
    first_row  = next(csvreader)
    change_list = []
    # base = int(first_row[1])
    # print(first_row)
    month_count = 1
    current_month = first_row[DATE_COL]
    current_pl = int(first_row[PL_COL])
    pl_total = current_pl
    prev_pl = current_pl
    for row in csvreader:
        #Total months, total, 
        month_count += 1
        current_month = row[DATE_COL]
        current_pl = int(row[PL_COL])
        pl_total += current_pl
        print(f"Month Total: {month_count}, Current Total: {pl_total}")
        # average change, greatest increase, greatest decrease 
        current_change = current_pl - prev_pl
        total_change += current_change
        #track changes in list
        change_list.append(current_change)
        prev_pl = int(row[1])
        #The greatest increase in profits (date and amount) over the entire period
        print(f"Greatest Increase: {max(change_list)}")
        # The greatest decrease in profits (date and amount) over the entire period
        print(f"Greatest Decrease: {min(change_list)}")
        #Maxchange_value, max change, minchange_value, min_change
        #define the variables
        maxchange_value = current_change
        prev_pl = current_pl    # setup for next run
        # calculate the average change
    average_change = total_change / (month_count - 1)
    print(f"Average Net Change: {average_change}")

    header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']

output_path = os.path.join('PyBank', 'Resources', 'solved_budget_data.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    # write the header
    csvwriter.writerow(['Finacial Analysis'])
    # write the data
    csvwriter.writerow(['Month Total: 86', 
    'Current Total: 38382578', 'Greatest Increase: 1926159', 'Greatest Decrease: -2196167', 'Average Net Change: -2315.1176470588234'])
        
    

  