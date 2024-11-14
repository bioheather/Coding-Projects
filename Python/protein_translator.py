# Assignment 1 
# Heather Johansen
# The purpose of this code is to translate randomly generated DNA sequences into predicted protein sequences using codon tables 
# from https://en.wikipedia.org/wiki/Genetic_code. 
# 
#
import random
#
# Define a dictionary with all the possible codons
codons = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

# I will use a reverse complement function to account for both forward and reverse readings of the strands
def reverse_complement(seq):
    complement = {'A':'T','T':'A','C':'G','G':'C'}
    reverse_comp = "".join(complement[base] for base in reversed(seq))
    return reverse_comp


# Now we need to define a function that will translate the DNA sequence
def translate(seq):
    protein_sequence = ""
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    start_index = seq.find(start_codon)
    if start_index == -1:
        return "No start codon found"
    
    for i in range(start_index, len(seq), 3):
        codon = seq[i:i+3]
        if codon in stop_codons:
            break
        if codon in codons:
            protein_sequence += codons[codon]
        else:
            protein_sequence += "?"

    return protein_sequence

# now to generate some random DNA sequence simulations of 200bp each
def make_random_DNA(length):
    return ''.join(random.choices("ATGC", k=length))

# run the simulation and generate 10 random sequences of 200bp each
for _ in range(10):
    dna_seq = make_random_DNA(200)
    protein_seq = translate(dna_seq)
    print(f"DNA: {dna_seq}")
    print(f"Protein: {protein_seq}\n")