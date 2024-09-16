# Determine if a word or phrase is an isogram

def is_isogram(string:str) -> bool:
    string = string.replace(" ","").replace("-","").lower()
    return not any(string.count(let.lower())>1 for let in string)
