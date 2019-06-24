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
        #profit = profit + [profit_change]

        #for i in range(0,len(row[1]) -1):
            #profit_change.append(int(final_profit[i+1]-int(initial_profit[i])))

            
    #for i[0]
    #total = int(0)
    #while i < len(budget_data):
        #total = total + budget_data[i]
        #i = i + 1
    #print("Total: " + int(net_total))    

#def Average(budget_data):
    #i = int(0)
    #total = int(0)
    #while i < len(budget_data):
        #total = total + budget_data[i]
        #i = i + 1
    #print("Average Change: " + int(total/len(budget_data)))