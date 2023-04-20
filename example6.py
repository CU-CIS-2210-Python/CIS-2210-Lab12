import csv

#Load the CSV File
csvFile = csv.reader(open("groceries.csv", "r"))
header = next(csvFile)
receipts = list(csvFile)

#Remember the file looks like this:
#customer_id,cashier_id,product_name,department_name,price

meatSales = 0.00 #Replace this line with your answer.

print(f"Total of meat sales: {meatSales}")