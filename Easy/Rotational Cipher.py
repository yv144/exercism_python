# Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.

import string

def rotate(text:str, key:int) -> str:
    alphabet = string.ascii_lowercase*2 + string.ascii_uppercase*2
    newtext = ""
    for letter in text:
        print(letter)
        if not letter.isalpha():
            newtext += letter
        else:
            location = alphabet.find(letter)
            newtext  += alphabet[location+key]
    return newtext
