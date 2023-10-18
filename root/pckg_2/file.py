
import pandas as pd
from ..pckg_1.file import df as df1
from .pckg_22.file import df as df2

import os

if __name__ == "__main__":
    current_dir = ""
else:
    current_dir = os.path.dirname(__file__)+'\\'
    

df0 = pd.read_csv(current_dir+'3.csv')
df = pd.concat([df1, df0, df2])