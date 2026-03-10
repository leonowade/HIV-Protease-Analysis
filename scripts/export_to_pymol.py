import pandas as pd
from Bio.PDB import PDBParser, PDBIO

def map_mechanicity_to_pdb():
    # Load our analysis
    results = pd.read_csv('results/final_mechanicity_analysis.csv')
    mechanicity_map = dict(zip(results.res_no, results.mechanicity_score))

    # Load the original PDB
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('1HHP', 'data/pdb/1hhp.pdb')

    # Replace B-factor with our Mechanicity Score
    for model in structure:
        for chain in model:
            if chain.id == 'A': # Focus on the monomer we analyzed
                for residue in chain:
                    res_id = residue.get_id()[1]
                    score = mechanicity_map.get(res_id, 0)
                    for atom in residue:
                        atom.set_bfactor(score)

    # Save the new PDB
    io = PDBIO()
    io.set_structure(structure)
    output_path = 'results/1hhp_mechanicity_mapped.pdb'
    io.save(output_path)
    print(f"✅ 3D Mapping complete! Open {output_path} in PyMOL and color by B-factor.")

if __name__ == "__main__":
    map_mechanicity_to_pdb()