import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_mechanicity_plot():
    csv_out = 'results/final_mechanicity_analysis.csv'
    plot_out = 'results/mechanicity_plot.png'
    
    # Load the datasets
    struct_df = pd.read_csv('results/structural_dynamics.csv')
    evolve_df = pd.read_csv('results/evolutionary_entropy.csv')
    
    # Filter for Chain A
    struct_df = struct_df[struct_df['chain'] == 'A'].copy()
    
    # Merge on residue number
    merged_df = pd.merge(struct_df, evolve_df, on='res_no')
    
    # Calculate Mechanicity Score (Movement / (Entropy + epsilon))
    merged_df['mechanicity_score'] = merged_df['b_factor'] / (merged_df['entropy'] + 0.1)
    
    # Save the merged data
    merged_df.to_csv(csv_out, index=False)
    
    # Visualization
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data=merged_df, x='entropy', y='b_factor', 
                    hue='mechanicity_score', palette='magma', size='mechanicity_score', sizes=(20, 200))
    
    # Identify the 'Gears' (Low entropy, High B-factor)
    # Adjust thresholds based on your data distribution
    avg_entropy = merged_df['entropy'].mean()
    avg_b = merged_df['b_factor'].mean()
    
    gears = merged_df[(merged_df['entropy'] < avg_entropy) & (merged_df['b_factor'] > avg_b)]
    
    for i, row in gears.iterrows():
        plt.text(row['entropy'] + 0.005, row['b_factor'], str(int(row['res_no'])), fontsize=8, alpha=0.7)
    
    plt.title('HIV-1 Protease: Mapping Mechanical Constraints')
    plt.xlabel('Shannon Entropy (Evolutionary Mutation Rate)')
    plt.ylabel('B-Factor (Physical Flexibility)')
    plt.axvline(x=avg_entropy, color='grey', linestyle='--', alpha=0.5)
    plt.axhline(y=avg_b, color='grey', linestyle='--', alpha=0.5)
    
    plt.savefig(plot_out)
    print(f"✅ Master Analysis complete!")
    print(f"📊 Results: {csv_out}")
    print(f"🖼️ Plot: {plot_out}")
    plt.show()

if __name__ == "__main__":
    if os.path.exists('results/structural_dynamics.csv') and os.path.exists('results/evolutionary_entropy.csv'):
        generate_mechanicity_plot()
    else:
        print("❌ Error: Missing CSV files in results/. Please check your previous analysis steps.")