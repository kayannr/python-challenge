import csv
import os

file_to_load = os.path.join('C:/Users/kayan/UCBWork/python-challenge/PyBank/raw_data/budget_data.csv')
file_to_output = os.path.join('analysis','budget_data_analysis.txt')

with open(file_to_load, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    profit_loss = [] #create list for profit/loss
    dates = [] #list of months/dates
    total_months = 0
    net_total= 0 

    for row in csvreader:
        
        profit_loss.append(int(row[1]))
        dates.append(str(row[0]))

        total_months = total_months+1 #count months 

        net_total = int(net_total) + int(row[1])
    
    rev_change = [] #create a list of revenue change
    for i in range(1, len(profit_loss)):
        rev_change.append(int(profit_loss[i]- int(profit_loss[i-1])))
    rev_average = float(sum(rev_change)/len(rev_change)) #average of revenue change
    rev_average = str(round(rev_average,2))
      
    max_ = max(rev_change)
    min_ = min(rev_change)
    max_location = int(rev_change.index(max(rev_change)))
    min_location = int(rev_change.index(min(rev_change)))
    date_max = str (dates[max_location+1]) 
    date_min = str (dates[min_location+1]) 
    
output = (
    f"\nFinancial Analysis\n"
    f"--------------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${rev_average}\n"
    f"Greatest Increase in Profits: {date_max} ${max_}\n"
    f"Greatest Decrease in Profits: {date_min} ${min_}\n")
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

