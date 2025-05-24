import pandas as pd


file_path = "data/Test_output.tsv"  
data = pd.read_csv(file_path, sep='\t')


hateful_comments = data[data['Hatefulness'] == 'Hateful']
non_hateful_comments = data[data['Hatefulness'] == 'NotHateful']


sample_hateful_100 = hateful_comments.sample(n=100, random_state=42) 
sample_non_hateful_100 = non_hateful_comments.sample(n=100, random_state=42)  


balanced_data_100_100 = pd.concat([sample_hateful_100, sample_non_hateful_100]).sample(frac=1, random_state=42)  


balanced_output_file_100_100 = "data/test_dataset_100_100.tsv"
balanced_data_100_100.to_csv(balanced_output_file_100_100, sep='\t', index=False)

print(f"Dataset with 100 Hateful and 100 NonHateful comments saved to {balanced_output_file_100_100}.")

counts_100_100 = balanced_data_100_100['Hatefulness'].value_counts()
print("\nCounts for 900 NonHateful and 100 Hateful dataset:")
print("Number of NotHateful entries:", counts_100_100.get("NotHateful", 0))
print("Number of Hateful entries:", counts_100_100.get("Hateful", 0))

