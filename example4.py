import csv #Load Python's CSV file reader

#Open the file.
file = open("example3.csv", "r")

#Create a CSV File Reader.
csvFile = csv.reader(file)

#Read the header and discard it!
header = next(csvFile)

#Load ALL the data into a list (of lists!)
books = list(csvFile)

print("Put a debug breakpoint here and run the program")