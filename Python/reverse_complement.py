# Find the reverse complement of a given DNA sequence
# 
# A dictionary is used to store complement nucleotides 


def reverse_complement(seq):
    complement = {'A':'T','T':'A','C':'G','G':'C'}
    reverse_comp = "".join(complement[base] for base in reversed(seq))
    return reverse_comp

sequence = "ATGCGTCAGCCGCGCCATCGAATCCGG"
print(reverse_complement(sequence))
