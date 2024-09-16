# Determine if a sentence is a pangram

import string

def is_pangram(sentence:str) -> bool:
    ascii_letters = set(string.ascii_lowercase)
    sentence_letters = set(sentence.lower())
    return sentence_letters.issuperset(ascii_letters)
