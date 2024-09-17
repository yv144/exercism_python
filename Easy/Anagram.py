# Give n a world and a list of possible anagrams, select hte correct sublist.

def analyze (key: str) -> dict:
    res = {}
    for letter in key.casefold():
        if letter in res:
            res[letter] +=1
        else: 
            res[letter] =1
    return res

def find_anagrams(word: str, cdts: list[str]) -> list[str]:
    output = []
    word_dct = analyze(word)
    for candidate in cdts:
        if  not word.casefold() == candidate.casefold():
            if word_dct == analyze(candidate):
                output.append(candidate)
    return output

candidates = ["dog", "goody"]

x = find_anagrams("good", candidates)
print(x)