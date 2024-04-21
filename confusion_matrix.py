import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import sys


def plot_confusion_matrix(df_confusion, title='Confusion matrix for 60k tests', cmap=plt.cm.gray_r):
    plt.matshow(df_confusion, cmap=cmap) # imshow
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(df_confusion.columns))
    plt.xticks(tick_marks, df_confusion.columns, rotation=45)
    plt.yticks(tick_marks, df_confusion.index)
    #plt.tight_layout()
    plt.ylabel(df_confusion.index.name)
    plt.xlabel(df_confusion.columns.name)
    plt.savefig('Confusion_Matrix.png')


if len(sys.argv) < 2:
    print("Usage : python3 confusion_matrix.py <csv_file>")
    exit(1)
    
filename = sys.argv[1]
if filename.split(".")[1] != "csv":
    print("Usage : python3 confusion_matrix.py <csv_file>")
    exit(1)
    

df_read = pd.read_csv(filename)

expected = pd.Series(df_read['EXPECTED'].values.tolist(), name='Expected')
predicted = pd.Series(df_read['FIRST'].values.tolist(), name='Predicted')

df_confusion = pd.crosstab(expected, predicted)
df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")

plot_confusion_matrix(df_conf_norm)
