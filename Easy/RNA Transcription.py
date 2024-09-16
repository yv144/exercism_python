# Given a DNA strand, return its RNA Complement Transcription.

def to_rna(dna_strand:str) -> str:
    dna_strand = dna_strand.replace("A","U").replace("T","A")
    rna = ""
    for let in dna_strand:
        if let == "G":
            rna += "C"
        elif let == "C":
            rna += "G"
        else:
            rna += let
    return rna
