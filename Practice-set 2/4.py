sequences = [
    "ATGCGTATACCGTGC",
    "ATATATATATATATA",
    "GCGCGCGCGCGCGCG",
    "CCCTATAGGG"
]

f_sequences = []

for seq in sequences:
    has_tata = "TATA" in seq
    
    gc_count = seq.count("G") + seq.count("C")
    gc_ratio = gc_count / len(seq)
    
    if has_tata and gc_ratio > 0.5:
        f_sequences.append(seq)

print(f_sequences)