import pandas as pd

# Read the csv into a dataframe
pybank_data = pd.read_csv("Resources/budget_data.csv")

# Calculate total number of months and net total amount
months = len(pybank_data)
total = pybank_data["Profit/Losses"].sum()

# Calculate average change
pybank_data["Last_Month_Profit/Loss"] = pybank_data["Profit/Losses"].shift(1)
pybank_data["Change"] = pybank_data["Profit/Losses"] - pybank_data["Last_Month_Profit/Loss"]
ave_change = pybank_data["Change"].mean()

# Find date and amount of max increase and decrease of profits
max_profit = [pybank_data["Change"].max(), pybank_data["Date"].iloc[pybank_data["Change"].idxmax()]]
max_loss = [pybank_data["Change"].min(), pybank_data["Date"].iloc[pybank_data["Change"].idxmin()]]

# Print analysis to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}") 
print(f"Total: ${total}")
print(f"Average Change: {ave_change}")
print(f"Greatest Increase in Profits: {max_profit[1]} (${max_profit[0]})")
print(f"Greatest Decrease in Profits: {max_loss[1]} (${max_loss[0]})")

# Write analysis to text file
with open('analysis/analysis.txt', 'w') as f:
    f.write(f'Financial Analysis\n----------------------------\nTotal Months: {months}\nTotal: ${total}\nAverage Change: {ave_change}\nGreatest Increase in Profits: {max_profit[1]} (${max_profit[0]})\nGreatest Decrease in Profits: {max_loss[1]} (${max_loss[0]})')