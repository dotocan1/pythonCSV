import csv
# import sys


### JAKO BITNO!!!!
### KRATI SE RECENICA SAMO AKO JE NAKON TOCKE RAZMAK
def skratiNaOdredeniBrojZnamenaka(p_recenica, p_maksElemenata):
    mySentence = []
    print(p_recenica)
    brojacZnamenka = 0
    words = [i for j in p_recenica.split() for i in (j, ' ')][:-1]
    # print(len(words))
    # slazi recenicu rijec po rijec dok ne dodes do 100 znamenka
    for word in words:
        brojacZnamenka += len(word)
        zadnjiElementRijeci = word[len(word)-1]
        # ako je broj znamenki manji od trazenog
        if brojacZnamenka <= p_maksElemenata and word==words[len(words)-1]:
            mySentence.append(word)
            editedSentence = "".join(mySentence)
            print(f"Prvi odabir: {mySentence}")
            return editedSentence
        elif (zadnjiElementRijeci == "." or zadnjiElementRijeci == "!" or zadnjiElementRijeci == "?")  and brojacZnamenka >= p_maksElemenata:
            mySentence.append(word)
            if brojacZnamenka >= 160:
               mySentence.append("trebaFixati")
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

    imeDat = input("Unesite ime originalne datoteke: ")
    imeOriginalneDatoteke = f"./{imeDat}.csv"
    imeStupcaZamjena = input("Unesite ime stupca kojeg zelite izmijeniti: ")
    print(imeStupcaZamjena)
    imeOutputDatoteke = f"{imeDat}_EDITED.csv"
    
    citanjeDatoteke(imeOriginalneDatoteke, imeStupcaZamjena)
    maksElementa = int(input("Upisite broj na koliko znamenki zelite skratiti recenicu:"))
    for sentence in sentences_for_editing_rows:
        edited_rows.append(skratiNaOdredeniBrojZnamenaka(sentence,maksElementa))
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

# imeStupcaZamjena = "Opis"
# imeOriginalneDatoteke = "./testiranjeCSVa.csv"
# imeOutputDatoteke = "testOutputFile.csv"

new_rows = []
edited_rows = []
sentences_for_editing_rows = []
imenaHeadera = []
zamjenaVrijednost = ""
unosImenaStupca()