import csv
import sys
import re

def izmijenaTekstaSaRijeci():
    global zamjenaVrijednost
    zamjenaVrijednost = input("Upisite novi sadrzaj redka: ")

def skratiNaOdredeniBrojZnamenaka(p_recenica, maksElemenata):
    global zamjenaVrijednost
    mySentence = []
    brojacZnamenka = 0
    brojac = 0
    words = [i for j in p_recenica.split() for i in (j, ' ')][:-1]
    # print(len(words))
    # slazi recenicu rijec po rijec dok ne dodes do 100 znamenka
    print(f"Ovo je recenica: {words}")
    for word in words:
        brojacZnamenka += len(word)
        zadnjiElementRijeci = word[len(word)-1]
        print(word)
        print(f"Ovo je brojac znamenki: {brojacZnamenka}")
        print(f"Ovo je zadnjiElementRijeci: {zadnjiElementRijeci}")
        print(f"Ovo je maks element: {maksElemenata}")
        # ako je 100. znamenka tocka, slozi recenica
        if brojacZnamenka <= maksElemenata and word==words[len(words)-1]:
            print("Ima manje rijeci svekupno")
            print(f"Ovo je zadnji element rijeci {zadnjiElementRijeci}")
            print(f"Ovo je rijec {word} a ovo je zadnja rijec {words[len(words)-1]}")
            print(f"A ovo je brojac znamenka {brojacZnamenka} a ovo je maks elementi: {maksElemenata}")
            mySentence.append(word)
            editedSentence = "".join(mySentence)
            # print(editedSentence)
            return editedSentence
        elif zadnjiElementRijeci == "." and brojacZnamenka > maksElemenata:
            print("Trazi se tocka")
            print(f"Ovo je zadnji element rijeci {zadnjiElementRijeci}")
            print(f"Ovo je rijec {word} a ovo je zadnja rijec {words[len(words)-1]}")
            print(f"A ovo je brojac znamenka {brojacZnamenka} a ovo je maks elementi: {maksElemenata}")
            mySentence.append(word)
            editedSentence = "".join(mySentence)
            # print(editedSentence)
            return editedSentence
        # ako 100. znamenka nije tocka, nastavi slagat rijeci
        else:
            mySentence.append(word)

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
    elif odabir == "2":
        # zamjenaVrijednost = skratiNaOdredeniBrojZnamenaka(recenica,100)
        citanjeDatoteke(imeOriginalneDatoteke)
        editDatoteke(imeStupcaZamjena)
        spremanjeEditiraneDatoteke(imeOutputDatoteke)
    else:
        sys.exit()

def citanjeDatoteke(p_imeOriginalneDatoteke):
    global new_rows
    with open(p_imeOriginalneDatoteke, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        global imenaHeadera
        imenaHeadera = reader.fieldnames
        for row in reader:
            # row[p_imeStupcaZamjena] = zamjenaVrijednost
            # Append the modified row to the list
            new_rows.append(row)

    # Reset the file pointer to the beginning of the file

        #csvfile.seek(0)
        # Zapisivanje u datoteku
def editDatoteke(p_imeStupcaZamjena):
    global edited_rows
    for row in new_rows:
        recenica = row[p_imeStupcaZamjena]
        row[p_imeStupcaZamjena] = skratiNaOdredeniBrojZnamenaka(recenica, 180)
        edited_rows.append(row)

def spremanjeEditiraneDatoteke(p_imeOutputDatoteke):
    with open(p_imeOutputDatoteke, "w", newline="", encoding="utf-8") as file:
        # Create a DictWriter object for the output file
        writer = csv.DictWriter(file, imenaHeadera, delimiter=";")

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for row in edited_rows:
            writer.writerow(row)

imeStupcaZamjena = "PROPERTY"
# zamjenaVrijednost = "zamjenaVrijednost"
imeOriginalneDatoteke = "./drugiMailTablicaCSV.csv"
imeOutputDatoteke = "testOutputFile.csv"

new_rows = []
edited_rows = []
imenaHeadera = []
zamjenaVrijednost = "aaaaa"
unosImenaStupca()