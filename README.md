# HIV-1 Protease Mechanicity Analysis Pipeline

This project integrates structural dynamics (PDB data) with evolutionary conservation (NCBI sequence data) to identify Mechanical Constraints within the HIV-1 Protease enzyme.

## Project Structure
* `data/`: Raw PDB structures and FASTA sequence alignments.
* `scripts/`: Python and PML scripts for data processing and visualization.
* `results/`: CSV data, summary reports, and visualization plots.

## How to Run the Pipeline

1. Environment Setup:
   ```bash
   python -m venv venv
   source venv/bin/activate  # venv\Scripts\activate on Windows
   pip install biopython pandas matplotlib seaborn tabulate