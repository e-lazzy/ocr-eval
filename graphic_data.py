import matplotlib.pyplot as plt
import pandas as pd

import sys

if len(sys.argv) < 2:
    print("Usage : python3 graphic_data.py <csv_file>")
    exit(1)
    
filename = sys.argv[1]
if filename.split(".")[1] != "csv":
    print("Usage : python3 graphic_data.py <csv_file>")
    exit(1)
    
nbOut = 0
nbIn = 0
nbFirst = 0


df = pd.read_csv(filename)
for ind in df.index:
    # ImageNumber, ExpectedValue, InOptions, OptionPosition
    if df["InOptions"][ind] == "OUI":
        if df["OptionPosition"][ind] == 0:
            nbFirst += 1
        else:
            nbIn += 1
    else:
        nbOut += 1
        
        
names = ['FIRST', 'IN LIST', 'OUT OF LIST'] # nom des barres
values = [nbFirst, nbIn, nbOut]
plt.bar(names, values); 
plt.savefig('Hist_Data_Full.png')
