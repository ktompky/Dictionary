import json
from difflib import get_close_matches
from config import dictionaryKey,thesaurusKey
import requests

w = input("Hello, what would you like to know the definition of? ")

def translate(w):
   response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{w}?key={dictionaryKey}")
   definition = response.json()
   new_def = definition[0]['def'][0]
   
   for key,value in new_def.items():
       print(key)
       for item in value:
           print(item[0][1]['dt'][0][1])
       

if __name__ == '__main__':
    translate(w)