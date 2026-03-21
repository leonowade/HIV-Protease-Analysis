import pandas as pd
import os

def generate_summary():
    file_path = 'results/final_mechanicity_analysis.csv'
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found. Run map_mechanicity.py first.")
        return

    df = pd.read_csv(file_path)

    # 1. Re-map Residue Names (1IDB Reference)
    # Since HIV-1 PR is highly conserved, we use the standard HXB2 numbering/names
    aa_map = {
        1: "PRO", 2: "GLN", 10: "LEU", 25: "ASP", 26: "THR", 27: "GLY", 
        30: "ASP", 40: "ASN", 48: "GLY", 50: "ILE", 80: "THR", 82: "VAL", 84: "ILE"
    }
    # For a full list, you'd extract this from your SeqIO records
    df['res_name'] = df['res_no'].map(aa_map).fillna("UNK")

    # 2. Sort by the Consensus Mechanicity Score
    top_gears = df.sort_values(by='mechanicity_score', ascending=False).head(15)

    report_path = 'results/mechanicity_summary.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# 🧬 HIV-1 Protease Mechanicity & Conservation Report\n\n")
        f.write("## Executive Summary\n")
        f.write("This report identifies 'Mechanical Gears': residues that exhibit high structural flexibility ")
        f.write("across Apo (1HHP), Holo (1IDB), and Mutant (1KJF) states, yet remain evolutionarily ")
        f.write("static. These represent prime targets for durable 'Block-and-Lock' interventions.\n\n")

        f.write("## ⚙️ Top Mechanical Constraints\n")
        
        # Select relevant columns for the PhD-level table
        # We include 'consensus_flexibility' to show the cross-structure proof
        display_cols = [
            'res_no', 'res_name', 'consensus_flexibility', 
            'normalized_entropy', 'gap_fraction', 'mechanicity_score'
        ]
        
        f.write(top_gears[display_cols].to_markdown(index=False))
        
        f.write("\n\n## 🔍 Strategic Interpretation\n")
        f.write("- **Low Entropy + High Flex:** These are likely hinges or 'elbows' of the protein.\n")
        f.write("- **High Gap Fraction:** Use caution; low entropy may be due to poor sequence coverage.\n")
        f.write("- **Targeting Recommendation:** Focus on residues with `mechanicity_score > 0.8` for dCas9-KRAB guidance.\n")

    print(f"✅ PhD-level summary report generated at {report_path}")

if __name__ == "__main__":
    generate_summary()