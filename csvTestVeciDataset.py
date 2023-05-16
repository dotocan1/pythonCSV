import csv
# import sys

def skratiNaOdredeniBrojZnamenaka(p_recenica, maksElemenata):
    mySentence = []
    brojacZnamenka = 0
    brojac = 0
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
            # print(editedSentence)
            return editedSentence
        elif zadnjiElementRijeci == "." and brojacZnamenka > maksElemenata:
            mySentence.append(word)
            editedSentence = "".join(mySentence)
            # print(editedSentence)
            return editedSentence
        # ako 100. znamenka nije tocka, nastavi slagat rijeci
        else:
            mySentence.append(word)

def unosImenaStupca():
    global imeOriginalneDatoteke
    global imeStupcaZamjena
    global imeOutputDatoteke
    global sentences_for_editing_rows

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
    brojac = 0
    for sentence in sentences_for_editing_rows:
        edited_rows[brojac] = skratiNaOdredeniBrojZnamenaka(sentence,100)
    brojac = 0
    for row in new_rows:
        row[imeStupcaZamjena] = edited_rows[brojac]
    # editDatoteke(imeStupcaZamjena)
    spremanjeEditiraneDatoteke(imeOutputDatoteke)

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
            sentences_for_editing_rows.append(row[p_imeStupcaZamjena])


    # Reset the file pointer to the beginning of the file

        #csvfile.seek(0)
        # Zapisivanje u datoteku
# def editDatoteke(p_imeStupcaZamjena):
#     global edited_rows
#     for row in new_rows:
#         # recenica = row[p_imeStupcaZamjena]
#         # row[p_imeStupcaZamjena] = skratiNaOdredeniBrojZnamenaka(recenica, 180)
#         edited_rows.append(row)

def spremanjeEditiraneDatoteke(p_imeOutputDatoteke):
    with open(p_imeOutputDatoteke, "w", newline="", encoding="utf-8") as file:
        # Create a DictWriter object for the output file
        writer = csv.DictWriter(file, imenaHeadera, delimiter=";")

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for row in new_rows:
            writer.writerow(row)

imeStupcaZamjena = "DOZIVLJAJ_3_TEKST"
imeOriginalneDatoteke = "./3CAFIX.csv"
imeOutputDatoteke = "testOutputFile.csv"

new_rows = []
edited_rows = []
sentences_for_editing_rows = []
imenaHeadera = []
zamjenaVrijednost = "aaaaa"
unosImenaStupca()