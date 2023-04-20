import csv
#Open the file and create a CSV File Reader.
csvFile = csv.reader(open("groceries.csv", "r"))

#discard the header
header = next(csvFile)

#Load ALL the data into a list (of lists!)
receipts = list(csvFile)

prices = [line[4] for line in receipts]

print("Put a debug breakpoint here and run the program")

prices = [float(line[4]) for line in receipts]

print("Put a debug breakpoint here and run the program")

print(f"Total of all sales: {sum(prices)}")