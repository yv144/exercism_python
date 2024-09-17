# Calculate the Hamming difference between two DNA strands.

def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b): 
        raise ValueError("Strands must be of equal length.")
    
    diff_count = 0
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            diff_count += 1
    return diff_count
