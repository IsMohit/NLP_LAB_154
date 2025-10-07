import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = """
Mars is the fourth planet from the Sun in our solar system, often referred to as the “Red Planet” due to its reddish appearance caused by iron oxide on its surface.S
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")


