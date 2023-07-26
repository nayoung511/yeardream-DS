import csv

with open("csv/data.csv", "r") as fd:
    reader = csv.reader(fd)

    for entry in reader:
        print(entry)