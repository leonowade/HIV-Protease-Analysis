import pandas as pd
import os

def generate_pymol_script():
    # 1. Load the Consensus Results
    # Using the comparative report ensures we see 'Universal Gears'
    try:
        df = pd.read_csv('results/final_mechanicity_analysis.csv')
    except FileNotFoundError:
        print("❌ Error: Run map_mechanicity.py first to generate the final analysis!")
        return

    # 2. Prepare the PyMOL script
    with open('color_dimer.pml', 'w') as f:
        # Load the reference structure (Holo-form)
        f.write("load data/pdb/1idb.pdb\n")
        f.write("hide all\n")
        f.write("show cartoon\n")
        f.write("set ray_shadows, 0\n") # Clean look for figures
        
        # Color by Chain initially
        f.write("color gray80, chain A\n")
        f.write("color gray90, chain B\n")
        
        # 3. Apply Mechanicity Scores
        # We use the mechanicity_score (0 to 1 range)
        for _, row in df.iterrows():
            res_no = int(row['res_no'])
            # Scale to 0-100 for PyMOL's B-factor column
            scaled_val = row['mechanicity_score'] * 100
            
            # Apply to both chains of the dimer
            f.write(f"alter (resi {res_no}), b={scaled_val:.2f}\n")
        
        # 4. Create the Heatmap
        f.write("spectrum b, blue_white_red, minimum=0, maximum=100\n")
        
        # 5. Highlight the "Gears" (Top 10% residues)
        threshold = df['mechanicity_score'].quantile(0.90)
        gears = df[df['mechanicity_score'] >= threshold]['res_no'].tolist()
        
        gear_selection = "+".join(map(str, gears))
        f.write(f"select top_gears, resi {gear_selection}\n")
        f.write("show sticks, top_gears\n")
        f.write("set stick_radius, 0.3\n")
        f.write("color yellow, top_gears\n") # Distinct color for the gears
        
        # 6. Final Camera Polish
        f.write("orient\n")
        f.write("set cartoon_transparency, 0.1\n")
        f.write("bg_color white\n") # Professional white background for thesis
        
        print(f"✅ Enhanced PyMOL script generated: 'color_dimer.pml'")
        print(f"💡 Highlighted {len(gears)} top mechanical residues in yellow sticks.")

if __name__ == "__main__":
    generate_pymol_script()