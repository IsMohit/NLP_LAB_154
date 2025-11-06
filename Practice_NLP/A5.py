import re 
import spacy

nlp = spacy.load("en_core_web_sm")

url = re.compile(r'http?://\S+|www\.\S+')
ip = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
date = re.compile(r'\d{4}-\d{2}-\d{2}')
pan = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')
email = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

def extract(text):
    doc = nlp(text)
    
    url1 = re.findall(url,text)
    ip1 = re.findall(ip,text)
    date1 = re.findall(date,text)
    pan1 = re.findall(pan,text)
    email1 = re.findall(email,text)
    
    ents = [(ent.text ,ent.label_) for ent in doc.ents]
    
    return{
        'url' : url1,
        'ip' : ip1,
        'date' : date1,
        'pan' : pan1,
        'email' : email1,
        'ent' : ents        
    }
    
text1 = """
Here is a sample text with a URL: https://www.google.com. 
Also, an IP address: 127.0.0.1 
The date is 2025-07-10.
A PAN number is ABPPI7976H.
Email is abc@gmail.com.
"""

result = extract(text1)
print("Url : ",result['url'])
print("IP : ",result['ip'])
print("Date : ",result['date'])
print("Pan : ",result['pan'])
print("Email : ",result['email'])
print("Entites : ",result['ent'])
