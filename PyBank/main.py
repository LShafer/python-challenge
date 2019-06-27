import os
import csv
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader, None)
    
    #define variables
    months = 0
    profit = 0
    total_profit = []
    date = []
    month_change_list = []
    increase_month = 0
    decrease_month = 0

    
    for row in csvreader:
        #count months
        months += 1

        #create list of dates
        date.append(row[0])
       
        #calculate total profit
        profit += int(row[1])
        total_profit.append(int(row[1]))
        
        #calculate profit change
    for i in range(len(total_profit)-1):
        month_change_list.append(total_profit[i+1]-total_profit[i])
        
highest_rev = max(month_change_list)
lowest_rev = min(month_change_list)

increase_month = date[month_change_list.index(highest_rev)+1]
decrease_month = date[month_change_list.index(lowest_rev)+1]

#print results
print("Financial Analysis")
print("--------------------------------------")   
print(f'Total Months: {months}')
print(f'Total Revenue: ${profit}')
print(f'Average Change: ${round(sum(month_change_list)/len(month_change_list))}')
print(f'Greatest Increase in Profits: {increase_month} (${highest_rev})')
print(f'Greatest Decrease in Profits: {decrease_month} (${lowest_rev})')
print("--------------------------------------")
    
#output to txt
output_file = "budget.txt"
os.path.join('..', 'PyBank', 'budget.txt')
with open(output_file, 'w') as text_file:

    print("Financial Analysis \n", file=text_file)
    print("------------------------ \n", file=text_file)
    print(f'Total Months: {months} \n', file=text_file)
    print(f'Total Revenue: ${profit} \n', file=text_file)
    print(f'Average Change: ${round(sum(month_change_list)/len(month_change_list))} \n', file=text_file)
    print(f'Greatest Increase in Profits: {increase_month} (${highest_rev}) \n', file=text_file)
    print(f'Greatest Decrease in Profits: {decrease_month} (${lowest_rev}) \n', file=text_file)
    print("------------------------ \n", file=text_file)