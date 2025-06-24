import pandas as pd

df = pd.read_csv('test_FD001.txt', sep=r'\s+', header=None)
print("Shape of the data:", df.shape)
sample_row = df.sample(n=1)
print(sample_row.to_csv(sep='\t'))  