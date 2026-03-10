import pandas as pd

def generate_summary():
    df = pd.read_csv('results/final_mechanicity_analysis.csv')
    
    # Sort by Mechanicity Score to find the top "Gears"
    top_gears = df.sort_values(by='mechanicity_score', ascending=False).head(10)
    
    report_path = 'results/mechanicity_summary.md'
    with open(report_path, 'w') as f:
        f.write("# HIV-1 Protease Mechanicity Report\n\n")
        f.write("## Top 10 Mechanical Constraints (High Flex, Low Mutation)\n")
        f.write("These residues are structurally flexible but evolutionarily conserved.\n\n")
        f.write(top_gears[['res_no', 'res_name', 'b_factor', 'entropy', 'mechanicity_score']].to_markdown(index=False))
        
    print(f"✅ Summary report generated at {report_path}")

if __name__ == "__main__":
    generate_summary()