import csv
import sys

def izmijenaTekstaSaRijeci():
    global zamjenaVrijednost
    zamjenaVrijednost = input("Upisite novi sadrzaj redka: ") 

def unosImenaStupca():
    # global imeOriginalneDatoteke
    # imeDat = input("Unesite ime originalne datoteke: ")
    # imeOriginalneDatoteke = f"./{imeDat}.csv"
    # global imeStupcaZamjena
    # imeStupcaZamjena = input("Unesite ime stupca kojeg zelite izmijeniti: ")
    # print(imeStupcaZamjena)
    # global imeOutputDatoteke
    # imeOutputDatoteke = f"{imeDat}_EDITED.csv"
    odabir = input("Odaberite sta zelite napraviti s tekstom:\n"
    "1) Manualno upisi s kojom vrijednoscu kojom zelis\n"
    "2) Skrati recenicu na odredeni broj rijeci\n")
    if odabir == "1":
        izmijenaTekstaSaRijeci()
        print("odabrano")
    else:
        sys.exit()

imeStupcaZamjena = "PROPERTY"
zamjenaVrijednost = "zamjenaVrijednost"
imeOriginalneDatoteke = "./drugiMailTablicaCSV.csv"
imeOutputDatoteke = "testOutputFile.csv"

unosImenaStupca()
with open(imeOriginalneDatoteke, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    new_rows = []
    for row in reader:
        row[imeStupcaZamjena] = zamjenaVrijednost
        # Append the modified row to the list
        new_rows.append(row)

    # Reset the file pointer to the beginning of the file

    csvfile.seek(0)
    # Zapisivanje u datoteku

    with open(imeOutputDatoteke, "w", newline="", encoding="utf-8") as file:
        # Create a DictWriter object for the output file
        writer = csv.DictWriter(file, reader.fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for row in new_rows:
            writer.writerow(row)
            # print("radi")