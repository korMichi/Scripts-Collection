import numpy as np
import pandas as pd
from Levenshtein import distance as lev

antibodies = {"antibody_name" : "SEQUENCE",
                "antibody_name_2" : "SEQUENCE_2"}

df = pd.read_excel("NAME_OF_EXCEL_FILE.xlsx")

def custom_lev(sequence, ref_sequence):
    return lev(sequence, ref_sequence)

for key in antibodies:
    df[key] = df["CDR3"].apply(custom_lev, ref_sequence=antibodies[key])

df.to_excel("NAME_OF_EXCEL_FILE.xlsx")