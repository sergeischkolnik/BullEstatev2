import csv

import pandas as pd



def readCsvToPd(file):
    return pd.DataFrame(pd.read_csv(file, skiprows=1, names=['id','precio','metros','lat','lon','dormitorios','banios']))


def readCsvSinFiltrosBasicos(file):
    props = []
    print("Reading:" + str(file))
    with open(file, 'r', encoding='utf-8') as File:
        reader = csv.reader(File)
        first = True
        for row in reader:
            if first:
                first = False
                continue
            props.append(row)
        File.close()
    return props

def readCsvFiltrado(file, filtroBanio = 1, filtroDormitorios = 1):
    props = []
    print("Reading:" + str(file))
    with open(file, newline='') as File:
        reader = csv.reader(File)
        first = True
        for row in reader:
            if first:
                first = False
                continue
            if len(row[3])==0 or len(row[4])==0:
                continue
            if float(row[2]) < 20000000 or float(row[2]) > 500000000 or int(row[3]) != filtroDormitorios or int(
                    row[4]) != filtroBanio or float(row[5]) < 15 or float(row[5]) > 150:
                continue
            props.append(row)
        File.close()
    return props

