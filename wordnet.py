#lexical database for the English language

from nltk.corpus import wordnet
syns = wordnet.synsets("program")
print(syns[0].name())
print(syns[0].lemmas()[0].name())
#Definition of that first synset:
print(syns[0].definition())
#Examples of the word in use
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    #các từ đồng nghĩa
    for l in syn.lemmas():
        #các từ đồng nghĩa
        synonyms.append(l.name())
        #các từ trái nghĩa
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#compare the noun of "ship" and "boat:"
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))


