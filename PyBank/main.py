import os
import csv
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath, newline='') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
    for row in csvreader:
        print(row)

    count_rows = len(budget_data)
    print("Total Months: " + count_rows)


    def net_total(budget_data):
        i = int(0)
        total = int(0)
        while i < len(budget_data):
            total = total + budget_data[i]
            i = i + 1
        print("Total: " + int(net_total))    

    def Average(budget_data):
        i = int(0)
        total = int(0)
        while i < len(budget_data):
            total = total + budget_data[i]
            i = i + 1
        print("Average Change: " + int(total/len(budget_data)))