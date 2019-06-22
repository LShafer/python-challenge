import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)

    def count_rows(budget_data):
        print("Total Months: " + len(budget_data))


    def net_total(budget_data):
        print("Total: " + net_total)
        for i = 0
        total = 0
        while(i < len(budget_data))
            total = total + budget_data[i]
            i = i + 1
        print("Total: " + int(net_total))    

    def Average(budget_data):
        for i = 0
        total = 0
        while(i < len(budget_data))
            total = total + budget_data[i]
            i = i + 1
        print("Average Change: " + int(total/len(budget_data)

    def max(budget_data):
        max = budget_data[0]
        for item in budget_data:
            if item > max:
                max = item
        print("Greatest Increase in Profits: " + "Date" + max


    def min(budget_data):
        min = budget_data[0]
        for item in budget_data:
            if item < min:
                min = item
        print("Greatest Decrease in Profits: " + "Date" + min)




