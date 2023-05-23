import csv

data = []

with open("archive_dataset.csv", "r")as f:
    csvReader = csv.reader(f)

    for row in csvReader:
        data.append(row)

headers = data[0]
planetData = data[1:]

for dataPoint in planetData:
    dataPoint[2] = dataPoint[2].lower()

planetData.sort(key = lambda planetData: planetData[2])

with open("archive_dataset_sorted.csv", "a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)

with open("archive_dataset_sorted.csv")as input, open("archived_dataset_sorted_sorted.csv", "w")as output:
    writer = csv.writer(output)
    
    for row in csv.reader(input):
        if any(field.strip()for field in row):
               writer.writerow(row)