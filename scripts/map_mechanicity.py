import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_mechanicity_plot():
    # 1. Load the Comparative Data (the winner from multiple PDBs)
    struct_path = "results/comparative_dynamics_report.csv"
    entropy_path = "results/evolutionary_entropy.csv"

    if not os.path.exists(struct_path) or not os.path.exists(entropy_path):
        print("❌ Missing master report or entropy file. Run the previous scripts first!")
        return

    struct_df = pd.read_csv(struct_path)
    evolve_df = pd.read_csv(entropy_path)

    # 2. Merge structural consensus with evolutionary entropy
    # We use 'consensus_flexibility' which is the average Z-score across 1IDB, 1HHP, 1KJF
    merged_df = pd.merge(struct_df, evolve_df, on="res_no")

    # 3. Mechanicity Score Calculation
    # High consensus_flexibility (wiggles everywhere) + Low normalized_entropy (never mutates)
    # We rescale consensus_flexibility to a 0-1 range for the score
    min_f = merged_df["consensus_flexibility"].min()
    max_f = merged_df["consensus_flexibility"].max()
    merged_df["scaled_flex"] = (merged_df["consensus_flexibility"] - min_f) / (max_f - min_f)

    merged_df["mechanicity_score"] = (
        merged_df["scaled_flex"] * (1 - merged_df["normalized_entropy"])
    )

    # 4. Identify the "True Gears" (Top 10% of Mechanicity)
    threshold = merged_df["mechanicity_score"].quantile(0.90)
    gears = merged_df[merged_df["mechanicity_score"] >= threshold].copy()
    gears = gears.sort_values("mechanicity_score", ascending=False)

    # Save results
    os.makedirs("results", exist_ok=True)
    merged_df.to_csv("results/final_mechanicity_analysis.csv", index=False)
    gears.to_csv("results/top_mechanical_residues.csv", index=False)

    # 5. Visualization: The Mechanicity Quadrant
    plt.figure(figsize=(12, 8))
    
    # Scatter plot: Evolution vs. Structural Consensus
    plot = sns.scatterplot(
        data=merged_df,
        x="normalized_entropy",
        y="consensus_flexibility",
        hue="mechanicity_score",
        size="mechanicity_score",
        palette="viridis",
        sizes=(40, 400),
        alpha=0.7
    )

    # Label the top "Gears" (High Flex, Low Mutation)
    for _, row in gears.iterrows():
        plt.text(
            row["normalized_entropy"] + 0.005,
            row["consensus_flexibility"] + 0.05,
            f"Res {int(row['res_no'])}",
            fontsize=9, weight='bold', alpha=0.8
        )

    # Aesthetics
    plt.axvline(0.2, color='red', linestyle='--', alpha=0.3, label="Conservation Cutoff")
    plt.axhline(0, color='black', alpha=0.2) # Mean B-factor line
    
    plt.title("HIV-1 Protease: Universal Mechanical Constraints\n(Consensus across Apo, Holo, and Mutant structures)", fontsize=14)
    plt.xlabel("Evolutionary Entropy (Low = Conserved)", fontsize=12)
    plt.ylabel("Consensus Structural Flexibility (Z-score)", fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    
    plt.savefig("results/mechanicity_quadrant_map.png", dpi=300)
    plt.show()

    print(f"✅ Analysis Complete. Identified {len(gears)} universal gears.")
    print("📊 Check 'results/top_mechanical_residues.csv' for your thesis targets.")

if __name__ == "__main__":
    generate_mechanicity_plot()