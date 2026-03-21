import os
from Bio.PDB import PDBList
import shutil

def download_pdb_structures(pdb_ids, save_path='data/pdb'):
    """Downloads and standardizes multiple PDB files for comparative analysis."""
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    pdbl = PDBList()
    
    for pdb_id in pdb_ids:
        print(f"📡 Fetching {pdb_id}...")
        # Downloads the file (usually as pdbXXXX.ent)
        downloaded_file = pdbl.retrieve_pdb_file(pdb_id.upper(), pdir=save_path, file_format='pdb')
        
        # Standardize the name to 'XXXX.pdb' for our analysis pipeline
        clean_name = os.path.join(save_path, f"{pdb_id.lower()}.pdb")
        
        if os.path.exists(downloaded_file):
            # Use move instead of copy to keep the folder clean
            shutil.move(downloaded_file, clean_name)
            print(f"✅ Success: {pdb_id} is ready at {clean_name}")
        else:
            print(f"❌ Error: Download failed for {pdb_id}.")

if __name__ == "__main__":
    # The 'Confidence Set' for your PhD research:
    # 1IDB: Holo (Baseline)
    # 1HHP: Apo (Open conformation)
    # 1KJF: Drug-resistant mutant
    target_pdbs = ['1IDB', '1HHP', '1KJF']
    download_pdb_structures(target_pdbs)