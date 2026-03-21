import subprocess
import sys

# Define steps with clear labels for your progress report
steps = [
    ("Fetching Structures", "python scripts/fetch_data.py"),
    ("Fetching Sequences", "python scripts/fetch_sequences.py"),
    ("Comparative Structural Analysis", "python scripts/analyze_structure.py"),
    ("Evolutionary Entropy Analysis", "python scripts/analyze_evolution.py"),
    ("Mechanicity Mapping", "python scripts/map_mechanicity.py"),
    ("Generating Summary Report", "python scripts/generate_report.py"),
    ("Exporting to PyMOL", "python scripts/export_to_pymol.py")
]

def run_pipeline():
    print("🚀 Starting HIV-1 Protease Mechanicity Pipeline\n" + "="*50)
    
    for label, command in steps:
        print(f"▶️  Running: {label}...")
        try:
            # check=True will raise an error if the script fails
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print(f"✅ {label} Completed Successfully.")
        except subprocess.CalledProcessError as e:
            print(f"\n❌ ERROR in {label}!")
            print(f"Output: {e.stderr}")
            print("\nStopping pipeline to prevent data corruption.")
            sys.exit(1)

    print("="*50 + "\n🎉 Full Pipeline Complete! Check the 'results/' folder.")

if __name__ == "__main__":
    run_pipeline()