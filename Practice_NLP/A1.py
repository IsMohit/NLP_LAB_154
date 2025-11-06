import spacy

nlp = spacy.load("en_core_web_sm")

about_text = (
    "India is my country."
    "Maharashtra is my state."
    "It is a Developing country."
)

# Tokenization
about_doc = nlp(about_text)
print("1. Tokenization")
for token in about_doc:
    print(token, token.idx)
    
    
# Stop word removal
about_doc = nlp(about_text)
print("\n2. Stop word removal")
print([token for token in about_doc if not token.is_stop])


# Lemmatization
about_doc = nlp(about_text)
print("\n3. Lemmatization")
for token in about_doc:
    if str(token) != str(token.lemma_):
       print(f"{str(token):>20} : {str(token.lemma_)}")
       
# POS Tagging
about_doc = nlp(about_text)
print("\n4. POS Tagging")
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=======
TAG: {str(token.tag_):10} POS: {str(token.pos_)}
Explaination: {spacy.explain(token.tag_)}
        """
    ) 