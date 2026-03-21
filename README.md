# HIV Protease Mechanicity Analysis

## Overview

This project identifies **mechanically constrained residues in HIV-1 protease**
by integrating structural dynamics and evolutionary conservation.

The goal is to discover mutation-resistant antiviral targets.

## Scientific Hypothesis

Residues that show:

• high structural flexibility  
• low evolutionary entropy  

represent mechanical control points required for protease function.

These residues may serve as **mutation-resistant antiviral targets**.

## Data Sources

Structural data: Protein Data Bank  
Sequence data: NCBI Protein database

## Pipeline

The computational workflow consists of five stages:

1. Fetch PDB structures
2. Fetch protease sequences
3. Structural flexibility analysis
4. Evolutionary entropy analysis
5. Mechanicity mapping

## Repository Structure

scripts/ – analysis scripts  
data/ – raw datasets  
results/ – computed outputs  
figures/ – visualization outputs

## Running the Analysis

Install dependencies:

pip install -r requirements.txt

Run pipeline:

python run_pipeline.py

Sequence Data ──► Entropy Analysis
                       │
                       ▼
Structure Data ──► Flexibility Analysis
                       │
                       ▼
                Mechanicity Score
                       │
                       ▼
          Candidate Mechanical Residues

## Output

The pipeline produces:

• evolutionary entropy per residue  
• structural flexibility metrics  
• integrated mechanicity scores  
• visualization of mechanical constraints

![Mechanicity chart](results/mechanicity_quadrant_map.png)
![Mechanicity table](results/mechanicity_summary.md)
![Protease structure](results/protease_structure.png)

## Author

Leon Owade  
MSc Chemistry  
Research interest: computational structural biology