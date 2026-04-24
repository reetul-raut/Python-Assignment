import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    row_count = sum(1 for row in reader)

print("Total number of rows:", row_count)