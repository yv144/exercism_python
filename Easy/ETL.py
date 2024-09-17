# Change data format for scoring a game 
# to more easily add other languages.

def transform(legacy_data):
    new_data = {}
    for score, values in legacy_data.items():
        for letter in values:
            new_data[letter.lower()] = score
    return new_data
