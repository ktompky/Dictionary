import json
from difflib import get_close_matches
from PyDictionary import PyDictionary

data = PyDictionary()

def translate(w):
    w = w.lower()
    return data.meaning(w)


w = input("Enter a word: ")

output = (translate(w))

if type(output) == list:

    for item in output:
        print(item)
else:
    print(output)
