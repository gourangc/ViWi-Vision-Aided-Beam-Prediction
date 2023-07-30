"""
Code for generating train, val, and test splits for multiple source files.
Author: Gouranga Charan
Date: 09/15/2020
"""

import numpy as np
from numpy.random import RandomState
from sklearn.utils import shuffle
import pandas as pd

# List of source files
source_files = ["drone_image_beam_data_BS1.csv", "drone_image_beam_data_BS2.csv"]

# Iterate over each source file
for file in source_files:
    # Read the source file
    df = pd.read_csv(file)
    rng = RandomState(1)
    
    # Perform data splitting
    train, val, test = np.split(df.sample(frac=1, random_state=rng), [int(.7*len(df)), int(.9*len(df))])
    
    # Remove the ".csv" extension from the file name
    file_name = file.split(".")[0]
    
    # Save the splits to separate CSV files
    train.to_csv(f'{file_name}_train.csv', index=False)
    val.to_csv(f'{file_name}_val.csv', index=False)
    test.to_csv(f'{file_name}_test.csv', index=False)
