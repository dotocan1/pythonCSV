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
    global imeOriginalneDatoteke
    imeDat = input("Unesite ime originalne datoteke: ")
    imeOriginalneDatoteke = f"./{imeDat}.csv"
    global imeStupcaZamjena
    imeStupcaZamjena = input("Unesite ime stupca kojeg zelite izmijeniti: ")
    print(imeStupcaZamjena)
    global imeOutputDatoteke
    imeOutputDatoteke = f"{imeDat}_EDITED.csv"
    odabir = input("Odaberite sta zelite napraviti s tekstom:\n"
    "1) Manualno upisi s kojom vrijednoscu kojom zelis\n"
    "2) Skrati recenicu na odredeni broj slova\n")
    if odabir == "1":
        maksElem = input("Na koliko znamenki zelite skratiti recenicu:")
        citanjeIZapisivanjeDatoteke()
    elif odabir == "2":
        # zamjenaVrijednost = skratiNaOdredeniBrojZnamenaka(recenica,100)
        exit
    else:
        sys.exit()

def citanjeIZapisivanjeDatoteke(p_imeOriginalneDatoteke, p_imeOutputDatoteke):
    with open(p_imeOriginalneDatoteke, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        new_rows = []
        for row in reader:
            row[imeStupcaZamjena] = zamjenaVrijednost
            # Append the modified row to the list
            new_rows.append(row)

    # Reset the file pointer to the beginning of the file

        csvfile.seek(0)
    # Zapisivanje u datoteku

        with open(p_imeOutputDatoteke, "w", newline="", encoding="utf-8") as file:
            # Create a DictWriter object for the output file
            writer = csv.DictWriter(file, reader.fieldnames)

            # Write the header row
            writer.writeheader()

            # Write the data rows
            for row in new_rows:
                writer.writerow(row)
                # print("radi")

# imeStupcaZamjena = "PROPERTY"
# zamjenaVrijednost = "zamjenaVrijednost"
# imeOriginalneDatoteke = "./drugiMailTablicaCSV.csv"
# imeOutputDatoteke = "testOutputFile.csv"

unosImenaStupca()