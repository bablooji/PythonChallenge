#Rutgers Boot Camp - Module 3 Challenge - Python script to analyze the financial records of the company.
#Bhagya Prasad

#PREREQUISITES
#Source Input file = budget_data.csv
#Source File directory where budget_data.csv is stored needs to be replaced as per the environment
#Summary Putfile File directory where Financial_Analysis_Summary.txt is stored needs to be replaced as per the environment

#Python Code starts here

# Import Dependencies Section
import os, csv
from pathlib import Path 

#File Handling Section
sourcefile = Path("/Users/babloo/Documents/rutgers/Module3", "PyBank/resources", "budget_data.csv")
summaryfile = Path("/Users/babloo/Documents/rutgers/Module3", "PyBank/resources", "Financial_Analysis_Summary.txt")


# Lists Section
totalmonths = []
totalprofit = []
monthlyProfit = []
 
# Storing CSV Data Section
with open(sourcefile,newline="", encoding="utf-8") as budgetData:

    budgetReader = csv.reader(budgetData,delimiter=",") 

    # Storing data taking the header out
    header = next(budgetReader)  

    for budgetrow in budgetReader: 

        # Keep adding the total months and total profit iteratively
        totalmonths.append(budgetrow[0])
        totalprofit.append(int(budgetrow[1]))

    # Calculate monthly change in profits
    for i in range(len(totalprofit)-1):
        
        monthlyProfit.append(totalprofit[i+1]-totalprofit[i])
        
# Determine maximum and minimum from the montly profit change
maxIncreaseProfit = max(monthlyProfit)
maxDecreaseProfit = min(monthlyProfit)

maxMonthlyIncrease = monthlyProfit.index(max(monthlyProfit)) + 1
maxMonthlyDecrease = monthlyProfit.index(min(monthlyProfit)) + 1 

# Print Console Output Section

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(totalmonths)}")
print(f"Total: ${sum(totalprofit)}")
print(f"Average Change: {round(sum(monthlyProfit)/len(monthlyProfit),2)}")
print(f"Greatest Increase in Profits: {totalmonths[maxMonthlyIncrease]} (${(str(maxIncreaseProfit))})")
print(f"Greatest Decrease in Profits: {totalmonths[maxMonthlyDecrease]} (${(str(maxDecreaseProfit))})")

# Summary File Section

with open(summaryfile,"w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(totalmonths)}")
    file.write("\n")
    file.write(f"Total: ${sum(totalprofit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthlyProfit)/len(monthlyProfit),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {totalmonths[maxMonthlyIncrease]} (${(str(maxIncreaseProfit))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {totalmonths[maxMonthlyDecrease]} (${(str(maxDecreaseProfit))})")
