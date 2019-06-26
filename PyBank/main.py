import os
import csv
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

file_output = "results.txt"

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader, None)
    
    #define variables
    months = 0
    month_count = []
    total_profit = 0
    initial_profit = 0
    profit_change = []
    greatest_increase = 0
    increase_month = 0
    greatest_decrease = 0
    decrease_month = 0
    
    for row in csvreader:
        #count months
        months += 1
       
        #calculate total profit
        total_profit += int(row[1])
        
        #calculate profit change
        final_profit = int(row[1])
        monthly_profits = final_profit - initial_profit
        profit_change.append(monthly_profits)
        month_count.append(row[0])
        average_profit = round(monthly_profits/months)
        
        #calculate greatest increase/decrease
        if greatest_increase < int(row[1]):
            greatest_increase = int(row[1])
            increase_month = row[0]
        if greatest_decrease > int(row[1]):
            greatest_decrease = int(row[1])
            decrease_month = row[0]

    #print results
    print("Financial Analysis")
    print("--------------------------------------")   
    print(f'Total Months: {months}')
    print(f'Total Revenue: ${total_profit}')
    print(f'Average Change: ${average_profit}')
    print(f'Greatest Increase in Profits: {increase_month} ${greatest_increase}')
    print(f'Greatest Decrease in Profits: {decrease_month} ${greatest_decrease}')
    print("--------------------------------------")
    
    #output to txt