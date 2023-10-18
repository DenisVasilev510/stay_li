
import pandas as pd
import os

if __name__ == "__main__":
    current_dir = ""
else:
    current_dir = os.path.dirname(__file__)+'\\'
    
df = pd.read_csv(current_dir+'2.csv')