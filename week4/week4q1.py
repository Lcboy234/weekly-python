# Write a short function to read the electrical demand in the UK data set (there is a link to this on moodle) that returns the dataframe. 

# To avoid difficulties in terms of locating the path make sure you store the CSV file in the same directory as your scripts.

import pandas as pd

df = pd.read_csv('week4/espeni_raw.csv')

print(df)