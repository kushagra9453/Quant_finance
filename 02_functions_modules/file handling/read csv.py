import csv
with open("portfolio.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
