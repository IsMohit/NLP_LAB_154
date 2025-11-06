import gensim 
from gensim import corpora
from gensim.utils import simple_preprocess

text = [
    """
    I love programming
    Python is my favourite programming language.
    Programming allow me solve real-time problems.
    """
]

tokens = [[item for item in line.split()] for line in text]
dict2 = corpora.Dictionary(tokens)

print("The Dictionary has ",str(len(dict2))," tokens\n")
print(dict2.token2id)

bow2 = [dict2.doc2bow(token, allow_update = True) for token in tokens]
print("Bag of Words : ",bow2)

dict3 = corpora.Dictionary([simple_preprocess(line) for line in text])
bow3 = [dict3.doc2bow(simple_preprocess(line)) for line in text]
print("\nDictionary : ")
for item in bow3:
    print([[dict3[id], freq] for id,freq in item])