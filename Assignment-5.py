import spacy
import re

nlp = spacy.load("en_core_web_sm")

url_pattern = re.compile(r'https?://\S+|www\.\S+')

ip_address_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
pan_number_pattern = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')

def extract_entities(text):
    doc = nlp(text)

    urls = re.findall(url_pattern, text)
    ip_addresses = re.findall(ip_address_pattern, text)
    dates = re.findall(date_pattern, text)
    pan_numbers = re.findall(pan_number_pattern, text)

    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return {
        'urls': urls,
        'ip_addresses': ip_addresses,
        'dates': dates,
        'pan_numbers': pan_numbers,
        'spaCy_entities': entities
    }

text_data = """
Here is a sample text with a URL: https://www.google.com. 
Also, an IP address: 127.0.0.1 
The date is 2025-07-10.
A PAN number is ABPPI7976H.
"""

results = extract_entities(text_data)

print("URLs:", results['urls'])
print("IP Addresses:", results['ip_addresses'])
print("Dates:", results['dates'])
print("PAN Numbers:", results['pan_numbers'])
print("Entities:", results['spaCy_entities'])