recenica = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget pellentesque felis. Ut venenatis sodales erat sed ultricies. Sed a sagittis arcu. Aenean in felis egestas, pulvinar sem id, luctus libero. Donec posuere hendrerit magna, id ultrices ante euismod sit amet. Phasellus facilisis ac enim in maximus. Nullam finibus convallis molestie. Phasellus eu purus ut nisi vehicula iaculis. Nulla finibus dapibus sapien. Cras aliquet iaculis lectus, in consequat nisi vestibulum sit amet. Vestibulum sagittis diam purus, sed condimentum lorem dapibus eget. Maecenas iaculis, tortor vel posuere tincidunt, lacus mauris maximus orci, ullamcorper dignissim tellus nisl in tortor. Aenean mollis, est."

words = recenica.split()
print(words)
mySentence = []
brojacZnamenka = 0
maksElemenata = 100
# slazi recenicu rijec po rijec dok ne dodes do 100 znamenka
for x in words:
    brojacZnamenka += len(x)
    zadnjiElementRijeci = x[len(x)-1]
    # ako je 100. znamenka tocka, slozi recenica
    if(brojacZnamenka >= maksElemenata and zadnjiElementRijeci == "."):
        mySentence.append(x)
        editedSentence = " ".join(mySentence)
        print(editedSentence)
        break
    # ako 100. znamenka nije tocka, nastavi slagat rijeci
    else:
        mySentence.append(x)