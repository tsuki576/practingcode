import os
import pandas as pd

file_path = (r"C:\Users\simra\OneDrive")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print(df)
else:
    print(f"File not found: {file_path}")

