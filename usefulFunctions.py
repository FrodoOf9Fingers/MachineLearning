import csv

def loadCSV(fileName):
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        rawData = list(reader)
    return rawData