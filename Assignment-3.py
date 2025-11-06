import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")

example_class_text = (
    "Elon Musk is the CEO of Tesla."
    "Golden Gate Bridge is situated in San Francisco."
    "Donald Trump is the current president of USA."
    "The GDP of India is 4.19 trillion dollars."
    "The first manufactured car was made by Ford."
    "Italy is famous for its Pizza."
    "The Second World War came to end in 1945. "
    "Andes are tallest mountain ranges in American continent."
    "Dead Sea is mostly of salt."
)
doc = nlp(example_class_text)

for ent in doc.ents:
    print(
        f"""
{ent.text = }
{ent.start_char = }
{ent.end_char = }
{ent.label_ = }
spacy.explain('{ent.label_}') = {spacy.explain(ent.label_)}"""
)
    
displacy.serve(doc, style="ent")