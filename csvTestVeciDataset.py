import csv
# import sys

def skratiNaOdredeniBrojZnamenaka(p_recenica, maksElemenata):
    mySentence = []
    print(p_recenica)
    brojacZnamenka = 0
    words = [i for j in p_recenica.split() for i in (j, ' ')][:-1]
    # print(len(words))
    # slazi recenicu rijec po rijec dok ne dodes do 100 znamenka
    for word in words:
        brojacZnamenka += len(word)
        zadnjiElementRijeci = word[len(word)-1]
        # ako je 100. znamenka tocka, slozi recenica
        if brojacZnamenka <= maksElemenata and word==words[len(words)-1]:
            mySentence.append(word)
            editedSentence = "".join(mySentence)
            print(f"Prvi odabir: {mySentence}")
            return editedSentence
        elif (zadnjiElementRijeci == "." or zadnjiElementRijeci == "!" or zadnjiElementRijeci == "?")  and brojacZnamenka >= maksElemenata:
            mySentence.append(word)
            editedSentence = "".join(mySentence)
            print(f"Drugi odabir: {mySentence}")
            return editedSentence
        # ako 100. znamenka nije tocka, nastavi slagat rijeci
        else:
            mySentence.append(word)
            print(f"Treci odabir: {mySentence}")

def unosImenaStupca():
    global imeOriginalneDatoteke
    global imeStupcaZamjena
    global imeOutputDatoteke
    global sentences_for_editing_rows
    global new_rows
    global edited_rows

    # imeDat = input("Unesite ime originalne datoteke: ")
    # imeOriginalneDatoteke = f"./{imeDat}.csv"
    # imeStupcaZamjena = input("Unesite ime stupca kojeg zelite izmijeniti: ")
    # print(imeStupcaZamjena)
    # imeOutputDatoteke = f"{imeDat}_EDITED.csv"
    # odabir = input("Odaberite sta zelite napraviti s tekstom:\n"
    # "1) Manualno upisi s kojom vrijednoscu kojom zelis\n"
    # "2) Skrati recenicu na odredeni broj slova\n")
    # if odabir == "1":
    #     maksElem = input("Na koliko znamenki zelite skratiti recenicu:")
    # elif odabir == "2":
        # zamjenaVrijednost = skratiNaOdredeniBrojZnamenaka(recenica,100)
    citanjeDatoteke(imeOriginalneDatoteke, imeStupcaZamjena)
    for sentence in sentences_for_editing_rows:
        edited_rows.append(skratiNaOdredeniBrojZnamenaka(sentence,20))
    brojac = 0

    for row in new_rows:
        row[imeStupcaZamjena] = edited_rows[brojac]
        brojac+=1
    spremanjeEditiraneDatoteke(imeOutputDatoteke)

def citanjeDatoteke(p_imeOriginalneDatoteke, p_imeStupcaZamjena):
    global new_rows
    global imenaHeadera
    global sentences_for_editing_rows
    with open(p_imeOriginalneDatoteke, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        imenaHeadera = reader.fieldnames
        for row in reader:
            # row[p_imeStupcaZamjena] = zamjenaVrijednost
            # Append the modified row to the list
            new_rows.append(row)
            sentences_for_editing_rows.append(row[p_imeStupcaZamjena])
            # print(row[p_imeStupcaZamjena])

def spremanjeEditiraneDatoteke(p_imeOutputDatoteke):
    with open(p_imeOutputDatoteke, "w", newline="", encoding="utf-8") as file:
        # Create a DictWriter object for the output file
        writer = csv.DictWriter(file, imenaHeadera, delimiter=";")

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for row in new_rows:
            writer.writerow(row)

imeStupcaZamjena = "Opis"
imeOriginalneDatoteke = "./testiranjeCSVa.csv"
imeOutputDatoteke = "testOutputFile.csv"

new_rows = []
edited_rows = []
sentences_for_editing_rows = []
imenaHeadera = []
zamjenaVrijednost = "aaaaa"
unosImenaStupca()