import pandas as pd

# Load your dataset (assume it's a TSV file)
file_path = "data/Test_output.tsv"  # Replace with your dataset file path
data = pd.read_csv(file_path, sep='\t')

# Filter Hateful and NonHateful comments using 'Hatefulness'
hateful_comments = data[data['Hatefulness'] == 'Hateful']
non_hateful_comments = data[data['Hatefulness'] == 'NotHateful']

# --- Create the 100 NonHateful and 100 Hateful dataset ---
# Select 100 Hateful and 100 NonHateful comments
sample_hateful_100 = hateful_comments.sample(n=100, random_state=42)  # Randomly select 100 Hateful comments
sample_non_hateful_100 = non_hateful_comments.sample(n=100, random_state=42)  # Randomly select 900 NonHateful comments

# Combine the samples into a new dataset
balanced_data_100_100 = pd.concat([sample_hateful_100, sample_non_hateful_100]).sample(frac=1, random_state=42)  # Shuffle the rows

# Save to a new file
balanced_output_file_100_100 = "data/test_dataset_100_100.tsv"
balanced_data_100_100.to_csv(balanced_output_file_100_100, sep='\t', index=False)

print(f"Dataset with 100 Hateful and 100 NonHateful comments saved to {balanced_output_file_100_100}.")

# # --- Create the 500 NonHateful and 500 Hateful dataset for stress testing ---
# # Select 500 Hateful and 500 NonHateful comments
# sample_hateful_500 = hateful_comments.sample(n=100, random_state=42)  # Randomly select 500 Hateful comments
# sample_non_hateful_500 = non_hateful_comments.sample(n=100, random_state=42)  # Randomly select 500 NonHateful comments

# # Combine the samples into a new dataset
# balanced_data_500_500 = pd.concat([sample_hateful_500, sample_non_hateful_500]).sample(frac=1, random_state=42)  # Shuffle the rows

# # Save to a new file
# balanced_output_file_500_500 = "src/data/stress_test_dataset_500_500.tsv"
# balanced_data_500_500.to_csv(balanced_output_file_500_500, sep='\t', index=False)

# print(f"Dataset with 500 Hateful and 500 NonHateful comments saved to {balanced_output_file_500_500}.")

# --- Count entries in both datasets ---
# For the 900x100 dataset
counts_100_100 = balanced_data_100_100['Hatefulness'].value_counts()
print("\nCounts for 900 NonHateful and 100 Hateful dataset:")
print("Number of NotHateful entries:", counts_100_100.get("NotHateful", 0))
print("Number of Hateful entries:", counts_100_100.get("Hateful", 0))

# For the 500x500 dataset
# counts_500_500 = balanced_data_500_500['Hatefulness'].value_counts()
# print("\nCounts for 500 NonHateful and 500 Hateful dataset:")
# print("Number of NotHateful entries:", counts_500_500.get("NotHateful", 0))
# print("Number of Hateful entries:", counts_500_500.get("Hateful", 0))