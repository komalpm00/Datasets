r'''import pandas as pd

column_names = [
    'unit_number', 'time_in_cycles',
    'op_setting_1', 'op_setting_2', 'op_setting_3'
] + [f'sensor_measurement_{i}' for i in range(1, 22)]
df = pd.read_csv('train_FD001.txt', sep="\s+", header=None, names=column_names)
print("Shape of the data:", df.shape)
print(df.head())'''


import pandas as pd

df = pd.read_csv('train_FD004.txt', sep=r'\s+', header=None)
print("Shape of the data:", df.shape)
sample_row = df.sample(n=1)
print(sample_row.to_csv(sep='\t'))   