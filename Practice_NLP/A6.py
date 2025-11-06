import spacy 
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

text = """
Mars is the fourth planet from the Sun in our solar system, often referred to as the “Red Planet” due to its reddish appearance caused by iron oxide on its surface"""
doc = nlp(text)

for token in doc:
    print(
        f"""
TOKEN : {token.text}
========================
{token.tag_ = }
{token.head.text = }
{token.dep_ = }      
        """
    )
    
displacy.serve(doc, style="dep")