import os
from Bio import Entrez, SeqIO

Entrez.email = "leonowade@gmail.com" 

def fetch_hiv_protease_sequences(limit=1000):
    """Fetches and filters HIV-1 Protease sequences for high-confidence analysis."""
    print(f"📡 Searching NCBI for {limit} HIV-1 Protease sequences...")
    
    # Refined query: Focus on 'protease' and exclude 'synthetic' or 'vector' constructs
    search_query = "(HIV-1 protease[Protein Name]) AND 90:110[Sequence Length] NOT synthetic[Title]"
    
    handle = Entrez.esearch(db="protein", term=search_query, retmax=limit)
    record = Entrez.read(handle)
    ids = record["IdList"]
    
    print(f"📥 Downloading {len(ids)} candidates...")
    fetch_handle = Entrez.efetch(db="protein", id=ids, rettype="fasta", retmode="text")
    
    # We parse the sequences to apply a secondary 'Quality Control' filter
    records = list(SeqIO.parse(fetch_handle, "fasta"))
    fetch_handle.close()

    valid_sequences = []
    for rec in records:
        # Quality Check: Ensure it's roughly the size of a protease (99 AA)
        # This removes large Pol polyproteins that slow down the pipeline
        if 90 <= len(rec.seq) <= 105:
            valid_sequences.append(rec)

    save_path = 'data/alignments/hiv1_pr_sequences.fasta'
    os.makedirs('data/alignments', exist_ok=True)
    
    with open(save_path, "w") as f:
        SeqIO.write(valid_sequences, f, "fasta")
    
    print(f"✅ Filtered {len(valid_sequences)} high-quality sequences into {save_path}")

if __name__ == "__main__":
    # Increase limit for PhD-level confidence (e.g., 2000+ sequences)
    fetch_hiv_protease_sequences(limit=2000)