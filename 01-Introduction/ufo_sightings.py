

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
#print(ufo.head())
#print(ufo.describe())

# To work with the dates, we will need to convert the YYYYMMDD string to an R Date
# type using the 'strptime' function

# But, something has gone wrong with the data. For now, we'll just ignore the errata
# by removing those entries that have not parsed correctly.  We know that the date 
# strings are always 8 characters long, and any deviation from this would indicate
# a row to ignore.  We will use the 'ifelse' function to construct a vector of
# Booleans indicating the problem rows
ufo['DateOccurred_LENGTH'] =  ufo['DateOccurred'].apply(lambda x : len(str(x)) )
ufo['DateReported_LENGTH'] =  ufo['DateReported'].apply(lambda x : len(str(x)) )

x =  ufo['DateOccurred_LENGTH'] != 8
y =  ufo['DateReported_LENGTH'] != 8
good_rows = x | y
ufo = ufo[good_rows]

# # Now we can convert the strings to Date objects and work with them properly
# pd.to_datetime(ufo['DateOccurred'])
# pd.to_datetime(ufo['DateReported'])
# 
# 
# print ufo['DateReported']