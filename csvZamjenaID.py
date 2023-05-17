import csv

def zamjenaSaPripadnomVrijednoscu(p_imeStupcaUsporedbe, p_imeStupcaZamjena, p_vrijednostStupcaUsporedbe, p_zamjenskaVrijednost):
    global edited_rows
    for row in new_rows:
        # print(row)
        if row[p_imeStupcaUsporedbe] == p_vrijednostStupcaUsporedbe:
            row[p_imeStupcaZamjena] = p_zamjenskaVrijednost
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

def unosImenaStupca():
    # global imeOriginalneDatoteke
    # global imeStupcaZamjena
    # global imeOutputDatoteke


    imeDat = input("Unesite ime originalne datoteke: ")
    imeOriginalneDatoteke = f"./{imeDat}.csv"
    imeStupcaZamjena = input("Unesite ime stupca kojeg zelite izmijeniti: ")
    imeOutputDatoteke = f"{imeDat}_EDITED.csv"
    imeStupcaUsporedbe = input("Unesite ime stupca usporedbe:")
    vrijednostStupcaUsporedbe = input("Unesite vrijednost stupca usporedbe:")
    zamjenskaVrijednost = input("S kojim podatkom zelite zamjeniti vrijednost:")
    citanjeDatoteke(imeOriginalneDatoteke, imeStupcaZamjena)
    zamjenaSaPripadnomVrijednoscu(imeStupcaUsporedbe, imeStupcaZamjena, vrijednostStupcaUsporedbe, zamjenskaVrijednost )
    spremanjeEditiraneDatoteke(imeOutputDatoteke)


imeStupcaZamjena = "PROPERTY_ID"
imeStupcaUsporedbe = "PROPERTY_DESTINATION"
vrijednostStupcaUsporedbe = "Dubrovnik"
zamjenskaVrijednost = "zamjenskaVrijednost"
imeOriginalneDatoteke = "./3CAFIX.csv"
imeOutputDatoteke = "testOutputFile.csv"

new_rows = []
imenaHeadera = []
edited_rows = []

unosImenaStupca()


