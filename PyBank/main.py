import os
import csv
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

file_output = "results.txt"

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader, None)
    print("Financial Analysis")
    print("--------------------------------------")
    
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
        months += 1
        print(f'Total Months: {months}')

        total_profit += int(row[1])
        print(f'Total Revenue: ${total_profit}')

        final_profit = int(row[1])
        monthly_profits = final_profit - initial_profit
        profit_change.append(monthly_profits)
        month_count.append(row[0])
        average_profit = round(monthly_profits/months)
        print(f'Average Change: ${average_profit}')

        if greatest_increase < int(row[1]):
            greatest_increase = int(row[1])
            increase_month = row[0]
        if greatest_decrease > int(row[1]):
            greatest_decrease = int(row[1])
            decrease_month = row[0]
        print(f'Greatest Increase in Profits: {increase_month} ${greatest_increase}')
        print(f'Greatest Decrease in Profits: {decrease_month} ${greatest_decrease}')
