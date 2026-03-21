import os
import pandas as pd
import numpy as np
from Bio.PDB import PDBParser

def process_pdb(pdb_id, file_path):
    """Extracts, averages, and normalizes B-factors for a homodimer."""
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, file_path)
    
    res_data = {}

    for model in structure:
        for chain in model:
            if chain.id in ['A', 'B']:
                for residue in chain:
                    # Ensure we only track standard amino acids
                    if residue.get_resname() in ['HOH', 'WAT']: continue
                    
                    res_no = residue.get_id()[1]
                    # Average B-factor for all atoms in the residue
                    b_factors = [atom.get_bfactor() for atom in residue]
                    avg_b = sum(b_factors) / len(b_factors) if b_factors else 0
                    
                    if res_no not in res_data:
                        res_data[res_no] = []
                    res_data[res_no].append(avg_b)

    # Convert to DataFrame
    rows = []
    for res_no, b_list in res_data.items():
        # Only include residues present in both chains for symmetry
        # Convert to DataFrame
        # LOGIC CHECK: If it's a dimer (len=2), average them. 
        # If it's a monomer (len=1), use the single value.
        avg_dimer_b = sum(b_list) / len(b_list)
        rows.append({'res_no': res_no, 'b_factor': avg_dimer_b})
        
        if not rows:
            print(f"⚠️ Warning: No residues found in {pdb_id}. Check chain IDs.")
            return pd.DataFrame(columns=['res_no', 'b_factor', 'b_norm'])

        df = pd.DataFrame(rows).sort_values('res_no')
    
    df = pd.DataFrame(rows).sort_values('res_no')

    # CRITICAL: Z-score Normalization
    # This allows comparison between 1IDB (1.9A) and 1HHP (2.8A)
    mean_b = df['b_factor'].mean()
    std_b = df['b_factor'].std()
    df['b_norm'] = (df['b_factor'] - mean_b) / std_b
    
    return df

def run_comparative_analysis(input_dir='data/pdb', output_dir='results'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    all_dfs = []
    pdb_files = [f for f in os.listdir(input_dir) if f.endswith('.pdb')]

    for filename in pdb_files:
        pdb_id = filename.split('.')[0]
        print(f"🔬 Processing Structure: {pdb_id}...")
        
        df = process_pdb(pdb_id, os.path.join(input_dir, filename))
        df.to_csv(os.path.join(output_dir, f"{pdb_id}_dynamics.csv"), index=False)
        
        # Prepare for global comparison
        df_named = df[['res_no', 'b_norm']].rename(columns={'b_norm': f'b_norm_{pdb_id}'})
        all_dfs.append(df_named)

    # Merge all structures into one master report
    if all_dfs:
        master_df = all_dfs[0]
        for next_df in all_dfs[1:]:
            master_df = pd.merge(master_df, next_df, on='res_no', how='inner')
        
        # Calculate Consensus Flexibility (Mean of normalized B-factors)
        norm_cols = [c for c in master_df.columns if 'b_norm_' in c]
        master_df['consensus_flexibility'] = master_df[norm_cols].mean(axis=1)
        
        master_df.to_csv(os.path.join(output_dir, 'comparative_dynamics_report.csv'), index=False)
        print(f"✅ Master report saved with {len(norm_cols)} structures.")

if __name__ == "__main__":
    run_comparative_analysis()