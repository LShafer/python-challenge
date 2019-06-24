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
        print(f"Total Months: {months}")

        total_profit += int(row[1])
        #print("Total Revenue: " + "$" + str(total_profit))

        final_profit = int(row[1])
        monthly_profits = final_profit - initial_profit
        profit_change.append(monthly_profits)
        average_profit = (monthly_profits/months)
        #print("Average Change: " + "$" + str(average_profit))

        average = sum(profit_change)/ len(profit_change)
        #print("new avg" + str(average))

        highest = max(profit_change)
        print("greatest increase" + str(highest))

        lowest = min(profit_change)
        print("decrease" +str(lowest))

        #greatest_increase = int(row[1])
        #if monthly_profits > greatest_increase:
        #greatest_increase = monthly_profits
        increase_month = row[0]
        #else (monthly_profits < decrease[1]):
            #decrease[1] = monthly_profits
        decrease_month = row[0]
        print(f'Greatest Increase in Profits: {increase_month} (${highest}')
        print(f'Greatest Decrease in Profits: {decrease_month} (${lowest}')