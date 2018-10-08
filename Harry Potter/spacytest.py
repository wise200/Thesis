import sys
sys.path.insert(0, "C:\\users\\justi\\desktop\\thesis\\harry potter\\foolishness\\spaCy")
import spacy
from spacy.tokens import Doc
from NLPClasses import FreqTable
from matplotlib import pyplot as plt
import sys
import pickle



with open("postable.txt", "r") as file:
    POSMap = dict()
    for line in file:
        item = line.split("\t")
        POSMap[item[0]] = item[1].strip()
     

nlp = spacy.load("en_core_web_sm")

nlp.max_length = 1600000


'''
with open("HP7.txt", "r", encoding="utf-8") as file:
    doc = nlp(file.read())

    

doc = Doc(Vocab()).from_disk("spacydocs/HP1.bin")
'''

docs = []
for x in range(1,8):
    with open("spacydocs/HP" + str(x) + ".pickle", "rb") as file:
        docbytes, vocabbytes = pickle.load(file)
        vocab = nlp.vocab.from_bytes(vocabbytes)
        docs.append(Doc(vocab).from_bytes(docbytes))
        print(x)

POSTable = FreqTable("Harry Potter Series")
indyTables = []

for x in range(len(docs)):
    doc = docs[x]
    table = FreqTable(str(x+1))
    for token in doc:
        pos = POSMap[token.pos_]
        if pos == "Interjection":
            pos = "Other"
        if pos not in ["Punctuation", "Numeral", "Space", "Symbol"]:
            POSTable.add(pos)
            table.add(pos)
    indyTables.append(table)


#POSTable.pieplot(False, 121)

#FreqTable.plotMultiple(indyTables, True, 111, "POS Frequencies in HP Books", ["Book " + str(x) for x in range(1,8)], True)
count = 1
for pos in POSMap.values():
    if pos not in ["Punctuation", "Numeral", "Space", "Symbol", "Auxiliary", "Conjunction", "Subordinating conjunction"]:
        FreqTable.plotDiffs(indyTables, pos, False, (3,4,count), pos + " Frequency", True)
        count += 1

plt.show()
'''
table6 = FreqTable()
table7 = FreqTable()

for token in docs[5]:
    pos = POSMap[token.pos_]
    if pos == "Interjection":
        pos = "Other"
    if pos not in ["Punctuation", "Numeral", "Space", "Symbol"]:
        table6.add(pos)

for token in docs[6]:
    pos = POSMap[token.pos_]
    if pos == "Interjection":
        pos = "Other"
    if pos not in ["Punctuation", "Numeral", "Space", "Symbol"]:
        table7.add(pos)

table6.pieplot(False, 121)
table7.pieplot(True, 122)

with open("spacydocs/HP1.pickle", "wb") as file:
    docbytes = doc.to_bytes()
    vocabbytes = doc.vocab.to_bytes()
    pickle.dump((docbytes,vocabbytes), file)
'''