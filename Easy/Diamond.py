# Given a letter, pritnt a diamond starting with 'A' with the
# supplied letter at the widest point

from string import ascii_uppercase as ASCUP



def rows(letter:str) -> list[str]:
    
    if letter == "A":
        return ["A"]
    
    printable = ASCUP[:ASCUP.find(letter)]
    delimeter = " "

    margin = len(printable)
    gap = -1

    output = []
    for let in printable:
        output.append(f'{delimeter*margin}{let}{delimeter*gap}{let if gap > 0 else ""}{delimeter*margin}')
        margin -= 1
        gap += 2
    output.append(delimeter*margin + letter + delimeter*(gap) + letter + delimeter*margin)
    for let in reversed(printable):
        margin += 1
        gap -= 2
        output.append(f'{delimeter*margin}{let}{delimeter*gap}{let if gap > 0 else ""}{delimeter*margin}')
    return output
