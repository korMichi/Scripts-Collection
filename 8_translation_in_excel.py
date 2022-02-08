import pandas as pd
from Bio.Seq import Seq

# Inputs: 
excel_name = input("Provide excel name: ")

# Function

df = pd.read_excel(excel_name, index_col=0)

df["NT_seq"] = df["NT_seq"].apply(Seq)
df["AA_seq"] = df["NT_seq"].apply(Seq.translate)
df.to_excel("translated.xlsx")