import pandas as pd
import os

# starting point
df = pd.read_csv('artwork_data.csv', nrows=5)

# the data has an id column so use that instead of the generated index
df = pd.read_csv('artwork_data.csv', nrows=5, index_col='id') 

# columns of interest
COLS_TO_USE = ['id', 'artist', 'medium', 
               'year','acquisitionYear', 'height',
               'width', 'units']

# read the entire file
df = pd.read_csv('artwork_data.csv',
                 usecols=COLS_TO_USE,
                 index_col='id') 
print(df)

# save for later
df.to_pickle('data_frame.pickle')