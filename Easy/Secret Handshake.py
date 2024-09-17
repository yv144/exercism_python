# Given a decimal number, convert it to the appropriate sequence of events for a secret handshake

actions = {
    0: "wink",
    1: "double blink",
    2: "close your eyes",
    3: "jump"
}
def commands(binary_str: str)->list[str]:
    output = []
    for reversed_index,value in enumerate(binary_str[:0:-1]):
        if value == "1":
          output.append(actions[reversed_index])
    
    if binary_str[0]=="1":
       output.reverse()
    return output
