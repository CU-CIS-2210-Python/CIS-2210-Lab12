import csv #Load Python's CSV file reader

#Open the file.
file = open("example3.csv", "r")

#We COULD read the file line by line, but instead we will
#create a CSV File Reader.
#
#It will read the file for us, and give us each row as a List.
#
#It works basically the same, read the file line by line, split
#at commas, but it does all the hard work of taking care of the
#little details like escaping and quoting for us! YAY
csvFile = csv.reader(file)

#Read the header and discard it!
header = next(csvFile)

#HEY CHECK THIS OUT
#the csvFile is just another "Bunch of things in some order"
#We can just use a for loop to get the 
for book in csvFile:
    print(book[0])
    print(f"\tBy: {book[1]}")
    print(f"\tPublished {book[2]}")