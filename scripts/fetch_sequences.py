import os
from Bio import Entrez, SeqIO

# Provide your email to NCBI so they can contact you if there's an issue
Entrez.email = "leonowade@gmail.com" 

def fetch_hiv_protease_sequences(limit=100):
    """Fetches HIV-1 Protease sequences from NCBI."""
    print(f"Fetching {limit} HIV-1 Protease sequences...")
    
    # Search query for HIV-1 Protease sequences
    search_query = "(HIV-1 protease[Protein Name]) OR (pol polyprotein[Protein Name] AND HIV-1[Organism])"
    handle = Entrez.esearch(db="protein", term=search_query, retmax=limit)
    record = Entrez.read(handle)
    ids = record["IdList"]
    
    # Fetch the actual sequences in FASTA format
    fetch_handle = Entrez.efetch(db="protein", id=ids, rettype="fasta", retmode="text")
    
    save_path = 'data/alignments/hiv1_pr_sequences.fasta'
    os.makedirs('data/alignments', exist_ok=True)
    
    with open(save_path, "w") as f:
        f.write(fetch_handle.read())
    
    print(f"✅ Saved {len(ids)} sequences to {save_path}")

if __name__ == "__main__":
    fetch_hiv_protease_sequences(limit=500)