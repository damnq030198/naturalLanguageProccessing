from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."
#stop word in english
stop_words = set(stopwords.words('english'))
print(stop_words)
#tokenize word in sentence
word_tokens = word_tokenize(example_sent)
#remove stop word in sentence
filtered_sentence = [w for w in word_tokens if not w in stop_words]
# #remove stop word in sentence
# filtered_sentence = []

# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)