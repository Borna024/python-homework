from pathlib import Path
import csv

budget_data = Path("budget_data.csv")

with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    csv_header = next(csv_reader)
    
    months = 0
    total_return = 0
    value = 0
    change = 0
    profits = []
    dates = []
    
    
    first_row = next(csv_reader)
    months += 1
    total_return += int(first_row[1])
    value = int(first_row[1])

    for row in csv_reader:

        
        dates.append(row[0]) 
        
        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])
        
        total_return += int(row[1]) 
        
        months += 1
        
        
    ave_change = sum (profits) / len(profits)
        
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]
    
    greatest_decrease = min(profits)
    least_index = profits.index(greatest_decrease)
    least_date = dates[least_index]
    
    
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {months}')
    print(f"Total: ${total_return}")
    print(f"Average Change: ${str(round(ave_change,2))}")
    print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {least_date} (${str(greatest_decrease)})")


output = open("budget_data.txt", "w")
    
line_1 = "Financial Analysis"
line_2 = "----------------------------"
line_3 = str(f'Total Months: {months}')
line_4 = str(f"Total: ${total_return}")
line_5 = str(f"Average Change: ${sum (profits) / len(profits)}")
line_6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line_7 = str(f"Greatest Decrease in Profits: {least_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line_1,line_2,line_3,line_4,line_5,line_6,line_7))







