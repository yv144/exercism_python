# Determine what Bob will reply to someone when they say something to him or ask him a question.

import string

def response(hey_bob:str)->str:
    hey_bob = hey_bob.strip()
    if (set(hey_bob).issubset(set(string.whitespace))):
        reply = "Fine. Be that way!"
    elif (hey_bob.upper() == hey_bob) and (hey_bob[-1]=="?") and len(set(hey_bob) & set(string.ascii_letters))>0:
        reply = "Calm down, I know what I'm doing!"
    elif hey_bob[-1]=="?":
        reply = "Sure."
    elif hey_bob.upper() == hey_bob and len(set(hey_bob) & set(string.ascii_letters))>0:
        reply = "Whoa, chill out!"
    else:
        reply = "Whatever."
    return reply
