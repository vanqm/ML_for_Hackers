

import os
import pandas as pd

# This is a tab-delimited file, so we use 'read.delim' and set the separator as a tab character.
# We also have to alter two defaults; first, we want the strings to not be converted to
# factor types; and, this data has does not have header labels in the first row, so
# we want to keep the first row as data.
#
# From the data's description file, we will set the column names accordingly using 
# the 'names' function
names =["DateOccurred", "DateReported","Location", "ShortDescription","Duration", "LongDescription"]
ufo = pd.read_csv(os.path.join("data", "ufo", "ufo_awesome.tsv"), sep="\t",names=names)

# Inspect the data frame
print(ufo.head())
print(ufo.describe())