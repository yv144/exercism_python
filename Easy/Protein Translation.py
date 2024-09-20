# Translate RNA sequences into proteins.

TRANSLATIONS = {
    'Methionine': ['AUG'],
    'Phenylalanine': ['UUU', 'UUC'],
    'Leucine':['UUA', 'UUG'],
    'Serine':['UCU', 'UCC', 'UCA', 'UCG'],
    'Tyrosine':['UAU', 'UAC'],
    'Cysteine':['UGU', 'UGC'],
    'Tryptophan':['UGG'] 
}
STOP  = ['UAA','UAG','UGA']

# reverse dictionary
def rev(d:dict) -> dict:
    rd = dict()
    for key,values in d.items():
        for value in values:
            rd[value] = key
    return rd

def proteins(strand:str)->list[str]:
    
    # step 1 break down into threes
    codons  = []
    for step in range(len(strand)//3):
        codons.append(strand[step*3:(step+1)*3:])
        
    # step 1.5 reverse dictionary
    REV_TRANSLATIONS = rev(TRANSLATIONS)

    # step 2 replace names for each codon
    proteins = []

    for codon in codons:
        if codon in STOP:
            break
        else:
            proteins.append(REV_TRANSLATIONS[codon])
    return proteins
