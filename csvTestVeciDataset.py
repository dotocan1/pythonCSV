import csv
import sys

def izmijenaTekstaSaRijeci():
    global zamjenaVrijednost
    zamjenaVrijednost = input("Upisite novi sadrzaj redka: ")

def skratiNaOdredeniBrojZnamenaka(p_recenica, maksElemenata):
    global zamjenaVrijednost
    words = recenica.split()
    # print(words)
    mySentence = []
    brojacZnamenka = 0
    # slazi recenicu rijec po rijec dok ne dodes do 100 znamenka
    for x in words:
        brojacZnamenka += len(x)
        zadnjiElementRijeci = x[len(x)-1]
        # ako je 100. znamenka tocka, slozi recenica
        if(brojacZnamenka >= maksElemenata and (zadnjiElementRijeci == "." or zadnjiElementRijeci == "?" or zadnjiElementRijeci == "!")):
            mySentence.append(x)
            editedSentence = " ".join(mySentence)
            # print(editedSentence)
            zamjenaVrijednost = editedSentence
            break
        # ako 100. znamenka nije tocka, nastavi slagat rijeci
        else:
            mySentence.append(x)

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
    "2) Skrati recenicu na odredeni broj slova\n")
    if odabir == "1":
        maksElem = input("Na koliko znamenki zelite skratiti recenicu:")
    elif odabir == "2":
        # zamjenaVrijednost = skratiNaOdredeniBrojZnamenaka(recenica,100)
        citanjeDatoteke(imeOriginalneDatoteke)
        editDatoteke(new_rows, imeStupcaZamjena)
        print(edited_rows)
    else:
        sys.exit()

def citanjeDatoteke(p_imeOriginalneDatoteke):
    global new_rows
    with open(p_imeOriginalneDatoteke, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            # row[p_imeStupcaZamjena] = zamjenaVrijednost
            # Append the modified row to the list
            new_rows.append(row)

    # Reset the file pointer to the beginning of the file

        #csvfile.seek(0)
        # Zapisivanje u datoteku
def editDatoteke(p_new_rows, p_imeStupcaZamjena):
    global edited_rows
    for row in p_new_rows:
        row[p_imeStupcaZamjena] = zamjenaVrijednost
        edited_rows.append(row)
        # with open(p_imeOutputDatoteke, "w", newline="", encoding="utf-8") as file:
        #     # Create a DictWriter object for the output file
        #     writer = csv.DictWriter(file, reader.fieldnames)

        #     # Write the header row
        #     writer.writeheader()

        #     # Write the data rows
        #     for row in new_rows:
        #         writer.writerow(row)

imeStupcaZamjena = "PROPERTY"
zamjenaVrijednost = "zamjenaVrijednost"
imeOriginalneDatoteke = "./drugiMailTablicaCSV.csv"
imeOutputDatoteke = "testOutputFile.csv"

new_rows = []
edited_rows = []
unosImenaStupca()