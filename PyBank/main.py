import os
import csv
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

file_output = "results.txt"

with open(csvpath, 'r') as csvfile:
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
    
    increase = ['', 9999999]
    decrease = ['', 0]
    
    for row in csvreader:
        months = months + 1
        print(f"Total Months: {months}")

        total_profit = total_profit + int(row[1])
        print("Total Revenue: " + "$" + str(total_profit))

        final_profit = int(row[1])
        monthly_profits = final_profit - initial_profit
        profit_change.append(monthly_profits)
        average_profit = (monthly_profits/months)
        print("Average Change: " + str(average_profit))

        if monthly_profits > increase[1]:
            increase[1] = monthly_profits
            increase[0] = row[0]
        else monthly_profits < decrease [1]:
                decrease[1] = monthly_profits
                decrease[0] = row[0]
        print(f'Greatest Increase in Profits: {increase[0]} (${increase[1]}')
        print(f'Greatest Decrease in Profits: {decrease[0]} (${decrease[1]}')