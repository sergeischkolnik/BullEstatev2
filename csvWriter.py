import csv

def writeCsv(file, data):
    with open(file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)