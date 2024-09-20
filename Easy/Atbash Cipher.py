# Create an implementaion of the atbash cipher,
# an ancient encryprion system created in the Middle East

import string

db = string.ascii_lowercase
r_db = db[::-1]

def encode(plain_text: str,dec: bool = False) -> str:
    output = []
    for let in plain_text:
        if let == " " or let in string.punctuation:
            continue
        elif let.lower() in db:
            location = db.find(let.lower())
            output.append(r_db[location])
        else:
            output.append(let)
        if len("".join(output).strip().replace(" ","")) % 5==0 and not dec:
            output.append(" ")
    return "".join(output).strip()


def decode(ciphered_text: str) -> str:
    return encode(ciphered_text,dec=True)
