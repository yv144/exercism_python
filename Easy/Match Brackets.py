# Make sure that brackets and braces all match.

open_brackets = set("{[(")
close_brackets = set("}])")

pairs = {
    "{":"}",
    "[":"]",
    "(":")"
}
def is_paired(input_string):
    if len(input_string)==0:
        return True
    
    true_str = []
    for let in input_string:
        if let in open_brackets or let in close_brackets:
            true_str.append(let)
    first = true_str[0]

    if first in close_brackets:
        return False
    if len(true_str)%2 == 1:
        return False
    if true_str[-1] == pairs[true_str[0]]:
        return True
    if pairs[first] not in true_str[1:]:
        return False

    first_half = true_str[:true_str.index(pairs[first])+1]
    second_half = true_str[true_str.index(pairs[first])+1:]
    return all([is_paired(first_half),is_paired(second_half)])
