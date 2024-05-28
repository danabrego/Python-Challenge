#import and set path to csvfile
import os
import csv

# Variable and counters
months = []
profitlosschanges = []

countmonths = 0
netprofitloss = 0
previousmonthprofitloss = 0
currentmonthprofitloss = 0
profitlosschange = 0


# Path to CSV  and open
budgetpath = os.path.join("Pybank","Resources", "budget_data.csv")


with open(budgetpath, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    for row in csv_reader:

        # Count of months
        countmonths += 1

        # Total profit
        currentmonthprofitloss = int(row[1])
        netprofitloss += currentmonthprofitloss
    
        if (countmonths == 1):
            previousmonthprofitloss = currentmonthprofitloss
            continue

        else:

            # Compute change in profit loss 
            profitlosschange = currentmonthprofitloss - previousmonthprofitloss

            months.append(row[0])

            profitlosschanges.append(profitlosschange)

            previous_month_profit_loss = currentmonthprofitloss

    #hi-low change, sum and average calcualtions
    sum_profit_loss = sum(profitlosschanges)
    average_profit_loss = round(sum_profit_loss/(countmonths - 1), 2)

    highest_change = max(profitlosschanges)
    lowest_change = min(profitlosschanges)

    highest_month_index = profitlosschanges.index(highest_change)
    lowest_month_index = profitlosschanges.index(lowest_change)

    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# Print to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {countmonths}")
print(f"Total:  ${netprofitloss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# Print to txt file
budgetfile = os.path.join("Pybank","Analysis", "analysis.txt")
with open(budgetfile, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {countmonths}\n")
    outfile.write(f"Total:  ${netprofitloss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")