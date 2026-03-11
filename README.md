# HIV-1 Protease Mechanicity Analysis Pipeline

This project integrates structural dynamics (PDB data) with evolutionary conservation (NCBI sequence data) to identify Mechanical Constraints within the HIV-1 Protease enzyme.

## Project Structure
* `data/`: Raw PDB structures and FASTA sequence alignments.
* `scripts/`: Python and PML scripts for data processing and visualization.
* `results/`: CSV data, summary reports, and visualization plots.

## How to Run the Pipeline

**1. Environment Setup:**
```bash
   python -m venv venv
   source venv/bin/activate  # venv\Scripts\activate on Windows
   pip install biopython pandas matplotlib seaborn tabulate
```

**2. Data Acquisition:**
```bash
    python scripts/fetch_data.py # :  Downloads 1HHP (Apo-Protease) from the PDB.
    python scripts/fetch_sequences.py #: Downloads ~500 HIV-1 Protease/Pol sequences from NCBI.
```

**3. Feature Extraction:**
```bash
    python scripts/analyze_structure.py #: Calculates residue-level B-factors (Physical flexibility).
    python scripts/analyze_evolution.py #: Uses a 'DTG-motif slicer' to calculate Shannon Entropy (Mutation rate).
```

**4. Integration & Visualization:**
```bash
    python scripts/map_mechanicity.py #: Merges data and generates the Mechanicity Scatter Plot.
    python scripts/generate_report.py #: Outputs a Markdown summary of the top "Gears."
    python scripts/export_to_pymol.py #: Maps scores back to a PDB file for 3D viewing.
```