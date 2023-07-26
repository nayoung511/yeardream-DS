import csv

with open("csv/output.csv", "w") as fd:
    writer = csv.writer(fd)
    writer.writerow((1, 2, 3))
    writer.writerows([
        (0, "나영", "980511"),
        (1, "수지", "951211"),
        (2, "맹구", "060806")
    ])