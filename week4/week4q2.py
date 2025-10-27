# write a function checkEntry that takes a dataframe df and a string s as input and returns a Boolean. If s is a column name in df then it returns True otherwise False.

# Note - one can access the column names of df using df.columns. dy.columns is an example of an iterator - you can call it directly in a for loop with

# for c in df.columns:

# Check if this works with the above data set.

import pandas as pd

df = pd.read_csv('week4/espeni_raw.csv')

def checkEntry(df, s):
    for c in df.columns:
        if c == s:
            return True
    return False

example = df.columns[5]
result = checkEntry(df, example)

print(example, result)