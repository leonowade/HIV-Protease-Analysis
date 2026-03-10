import os
import pandas as pd
import numpy as np
from Bio.PDB import PDBParser

def extract_b_factors(pdb_id, pdb_dir='data/pdb'):
    # LOOK HERE: We are looking for 1hhp.pdb
    pdb_file = os.path.join(pdb_dir, f"{pdb_id.lower()}.pdb")
    
    if not os.path.exists(pdb_file):
        print(f"❌ Error: {pdb_file} not found. Run fetch_data.py first.")
        return None

    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, pdb_file)
    
    data = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.get_id()[0] == ' ': 
                    avg_b = np.mean([atom.get_bfactor() for atom in residue])
                    data.append({
                        'chain': chain.id,
                        'res_no': residue.get_id()[1],
                        'res_name': residue.get_resname(),
                        'b_factor': avg_b
                    })
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = extract_b_factors('1HHP')
    if df is not None:
        os.makedirs('results', exist_ok=True)
        df.to_csv('results/structural_dynamics.csv', index=False)
        print(f"✅ Structural data saved to results/structural_dynamics.csv")