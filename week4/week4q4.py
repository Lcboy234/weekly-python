# Write a function cleanColumn that takes a data frame df and a string s as input. 
# If s is a column of df then it returns a data frame 
# where all the rows which have NaNs in that column are removed otherwise it returns None.

# Check this for the test data set that you have.

import pandas as pd
dt = pd.read_csv('week4/espeni_raw.csv')

def cleanColumn(df, s):
    if s in df.columns:
        return df.dropna(subset=[s])
    else:
        return None
    
test_df = cleanColumn(dt, "POWER_NGEM_IFA2_FLOW_MW")
print(test_df)