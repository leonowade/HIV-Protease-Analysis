import os
import math
import pandas as pd
from collections import Counter
from Bio import SeqIO

VALID_AA = set("ACDEFGHIKLMNPQRSTVWY")

def extract_protease_region(full_seq):
    """Refined extraction: Finds the most likely 99AA Protease."""
    motif = "DTG"
    # Find all occurrences of DTG
    indices = [i for i in range(len(full_seq)) if full_seq.startswith(motif, i)]
    
    for index in indices:
        if index >= 24:
            start = index - 24
            protease = full_seq[start:start + 99]
            if len(protease) == 99:
                return protease
    return None

def clean_sequence(seq):
    return ''.join([aa if aa in VALID_AA else '-' for aa in seq])

def calculate_entropy(column):
    """Shannon entropy with a confidence check."""
    # Filter out gaps for the calculation
    amino_acids = [aa for aa in column if aa != '-']
    gap_count = column.count('-')
    total_obs = len(column)
    
    if len(amino_acids) == 0:
        return 0, 1.0 # Max gap fraction

    counts = Counter(amino_acids)
    total_aa = len(amino_acids)
    gap_fraction = gap_count / total_obs

    entropy = 0
    for count in counts.values():
        p = count / total_aa
        entropy -= p * math.log2(p)

    return entropy, gap_fraction

def calculate_entropy_from_fasta(fasta_path):
    if not os.path.exists(fasta_path):
        print(f"❌ File not found: {fasta_path}")
        return None

    valid_proteases = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        seq_str = str(record.seq).upper()
        
        # Priority 1: Exact length match
        if len(seq_str) == 99:
            valid_proteases.append(clean_sequence(seq_str))
        # Priority 2: Extract from polyprotein
        else:
            sliced = extract_protease_region(seq_str)
            if sliced:
                valid_proteases.append(clean_sequence(sliced))

    if not valid_proteases:
        return None

    print(f"🧬 Analyzing {len(valid_proteases)} high-quality protease sequences.")

    entropy_results = []
    max_entropy = math.log2(20)

    for i in range(99):
        column = [seq[i] for seq in valid_proteases]
        entropy, gap_frac = calculate_entropy(column)

        entropy_results.append({
            "res_no": i + 1,
            "entropy": entropy,
            "normalized_entropy": entropy / max_entropy,
            "gap_fraction": gap_frac,
            "sample_size": len(column) - column.count('-')
        })

    return pd.DataFrame(entropy_results)

if __name__ == "__main__":
    INPUT_FILE = os.path.join("data", "alignments", "hiv1_pr_sequences.fasta")
    df_entropy = calculate_entropy_from_fasta(INPUT_FILE)

    if df_entropy is not None:
        os.makedirs("results", exist_ok=True)
        # Truth Check: Filter out residues with >20% gaps as 'unreliable'
        df_unreliable = df_entropy[df_entropy['gap_fraction'] > 0.2]
        if not df_unreliable.empty:
            print(f"⚠️ Warning: {len(df_unreliable)} residues have high gap fractions (>20%).")

        df_entropy.to_csv("results/evolutionary_entropy.csv", index=False)
        print("✅ Evolutionary entropy saved.")