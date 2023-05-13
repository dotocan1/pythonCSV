import csv

imeStupcaZamjena = "PROPERTY"
zamjenaVrijednost = "zamjenaVrijednost"
imeOriginalneDatoteke = "./drugiMailTablicaCSV.csv"
imeOutputDatoteke = "testOutputFile.csv"

with open(imeOriginalneDatoteke, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    new_rows = []
    for row in reader:
        row[imeStupcaZamjena] = zamjenaVrijednost
        # Append the modified row to the list
        new_rows.append(row)
        row
        break

    # Reset the file pointer to the beginning of the file

    csvfile.seek(0)
    # Zapisivanje u datoteku

    with open(imeOutputDatoteke, "w", newline="", encoding="utf-8") as file:
        # Create a DictWriter object for the output file
        print(new_rows)
        writer = csv.DictWriter(file, reader.fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for row in new_rows:
            writer.writerow(row)
            # print("radi")