# Initialize PyIR and set example file for processing
from pyir import PyIR
import pandas as pd

FILE = 'example.fasta'

pyirfiltered = PyIR(query=FILE, args=['--outfmt', 'dict', '--enable_filter'])
result = pyirfiltered.run()

df = pd.DataFrame.from_dict(result)
df.to_excel("trimmed_seq.xlsx", index=False, header=False)

# Prints size of Python returned dictionary
print(len(result))
