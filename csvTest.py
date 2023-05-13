import csv

with open('./testiranjeCSVfix.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # This will print out all columns for the column 'Ime'
        #print(row['Ime'])
        print('Radi')

reader.fieldnames[0] = 'ID_podatka'
print(reader.fieldnames)