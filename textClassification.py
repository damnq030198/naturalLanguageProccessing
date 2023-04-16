import nltk
import random
from nltk.corpus import movie_reviews
#lấy ra các từ và nhãn(pos and neg) của nó
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
#phân phối tuần tự
all_words = nltk.FreqDist(all_words)
print("---------------")
print(all_words.most_common(14))
print("---------------")
print(all_words["stupid"])