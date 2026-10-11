# Find the most frequent kmer in a list of sequences by counting kmers across all sequences. 
# An example list of sequences is shown and will print the most frequent kmer to the console.

def most_frequent_kmer_list(sequences, k):
    # dictionary outside the loop and make a for loop to go through all sequences in the list
    dic_count = {}
    # create a loop to search each sequence in the list
    for sequence in sequences:
        length = len(sequence)
        if k > length:
            # Skip sequences shorter than k
            continue
        for i in range(length - k + 1):
            kmer = sequence[i:i + k]
            if kmer not in dic_count:
                dic_count[kmer] = 1
            else:
                dic_count[kmer] += 1
    value_key_list = [(value, key) for key, value in dic_count.items()]
    # add the k-mer from all sequences and else for no results found
    return max(value_key_list)[1] if value_key_list else "No valid k-mers found"

# Example list of sequences
sequences = [
    "ATGCTGCCGTAATGCCGATCAACGTCGGACTATGC",
    "GCCGTGCGCTGATGCGCCGATACGATGCCGATATG",
    "ATGCCGATACGTAGCCGATCGTGCCGATGATGCTG"
]
k = 4
print(most_frequent_kmer_list(sequences, k))
