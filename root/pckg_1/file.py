
import pandas as pd
from .pckg_11.file import df as df1

import os

if __name__ == "__main__":
    current_dir = ""
else:
    current_dir = os.path.dirname(__file__)+'\\'
    

df0 = pd.read_csv(current_dir+'1.csv')
df = pd.concat([df1, df0])




