import csv

def zamjenaSaPripadnomVrijednoscu():
    global edited_rows
    for row in new_rows:
        # print(row)
        if row["PROPERTY_DESTINATION"] == "Dubrovnik":
            row["PROPERTY_ID"] = "zamjenaVrijednost"
            edited_rows.append(row)
        else:
            edited_rows.append(row)


def citanjeDatoteke(p_imeOriginalneDatoteke, p_imeStupcaZamjena):
    global new_rows
    global imenaHeadera
    with open(p_imeOriginalneDatoteke, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        imenaHeadera = reader.fieldnames
        for row in reader:
            # row[p_imeStupcaZamjena] = zamjenaVrijednost
            # Append the modified row to the list
            new_rows.append(row)

def spremanjeEditiraneDatoteke(p_imeOutputDatoteke):
    global edited_rows
    with open(p_imeOutputDatoteke, "w", newline="", encoding="utf-8") as file:
        # Create a DictWriter object for the output file
        writer = csv.DictWriter(file, imenaHeadera, delimiter=";")

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for row in edited_rows:
            writer.writerow(row)




imeStupcaZamjena = "PROPERTY_ID"
imeOriginalneDatoteke = "./3CAFIX.csv"
imeOutputDatoteke = "testOutputFile.csv"

new_rows = []
imenaHeadera = []
edited_rows = []

citanjeDatoteke(imeOriginalneDatoteke, imeStupcaZamjena)
zamjenaSaPripadnomVrijednoscu()
spremanjeEditiraneDatoteke(imeOutputDatoteke)