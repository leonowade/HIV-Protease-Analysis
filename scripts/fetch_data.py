import os
from Bio.PDB import PDBList
import shutil

def download_pdb_structure(pdb_id, save_path='data/pdb'):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    pdbl = PDBList()
    # This downloads the file
    downloaded_file = pdbl.retrieve_pdb_file(pdb_id, pdir=save_path, file_format='pdb')
    
    # Standardize the name so analyze_structure.py can find it
    clean_name = os.path.join(save_path, f"{pdb_id.lower()}.pdb")
    
    if os.path.exists(downloaded_file):
        shutil.copy(downloaded_file, clean_name)
        print(f"✅ Success: {pdb_id} is ready at {clean_name}")
    else:
        print(f"❌ Error: Download failed.")

if __name__ == "__main__":
    download_pdb_structure('1HHP')