import os
import math
import pandas as pd
from collections import Counter
from Bio import SeqIO

def extract_protease_region(full_seq):
    """Finds the 99 AA protease within a longer Pol polyprotein using the DTG motif."""
    # The 'DTG' motif is highly conserved at residues 25-27
    motif = "DTG"
    index = full_seq.find(motif)
    
    # We need 24 residues before 'D' and 72 residues after 'G' (Total 99)
    if index != -1 and index >= 24:
        start = index - 24
        protease = full_seq[start : start + 99]
        if len(protease) == 99:
            return protease
    return None

def calculate_entropy_from_fasta(fasta_path):
    if not os.path.exists(fasta_path):
        print(f"❌ File not found: {fasta_path}")
        return None

    valid_proteases = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        seq_str = str(record.seq).upper()
        
        # Check if it's already a 99 AA monomer
        if len(seq_str) == 99:
            valid_proteases.append(seq_str)
        else:
            # Try to 'slice' it out of a longer polyprotein
            sliced = extract_protease_region(seq_str)
            if sliced:
                valid_proteases.append(sliced)
    
    if not valid_proteases:
        print("❌ Error: Could not find any 99 AA protease regions in the data.")
        return None

    print(f"🧬 Successfully extracted and analyzing {len(valid_proteases)} protease sequences.")

    num_res = 99
    entropy_results = []
    for i in range(num_res):
        column = [s[i] for s in valid_proteases]
        counts = Counter(column)
        total = len(column)
        
        # Shannon Entropy Formula
        entropy = sum([-(count/total) * math.log2(count/total) for count in counts.values()])
        entropy_results.append({'res_no': i + 1, 'entropy': entropy})
    
    return pd.DataFrame(entropy_results)

if __name__ == "__main__":
    INPUT_FILE = os.path.join('data', 'alignments', 'hiv1_pr_sequences.fasta')
    
    # Matches the function name defined above
    df_entropy = calculate_entropy_from_fasta(INPUT_FILE)
    
    if df_entropy is not None:
        os.makedirs('results', exist_ok=True)
        output_path = 'results/evolutionary_entropy.csv'
        df_entropy.to_csv(output_path, index=False)
        print(f"✅ Success! Evolutionary data saved to {output_path}")