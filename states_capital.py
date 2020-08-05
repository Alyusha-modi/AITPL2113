import csv
filename = "capitals.csv"
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        print(row)

    print("Total no. of rows: " ,(csvreader.line_num))
