import nltk
from nltk.util import ngrams

sent = "Mars is the fourth planet from the Sun in our solar system"

n = 1
unigrams = ngrams(sent.split(),n)
print("==================== UNIGRAM =========================")
for item in unigrams:
    print(item)

n = 2
bigrams = ngrams(sent.split(),n)
print("\n==================== BIGRAM =========================")
for item in bigrams:
    print(item)

n = 3
trigrams = ngrams(sent.split(),n)
print("\n==================== TRIGRAM =========================")
for item in trigrams:
    print(item)