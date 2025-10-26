# Write a function selectColumns that takes a dataframe df and a list l as input. If all the entries in l are column names in df then it returns a data frame composed of the data from df with those columns, 
# otherwise it returns None.

# For example, if df is data frame with the test data set you are using then

# l = ['POWER_NGEM_EMBEDDED_WIND_GENERATION_MW','POWER_NGEM_IFA_FLOW_MW','POWER_ELEXM_WIND_MW']

# dfs = selectColumns(df,l)

# will create a data frame dfs with the above three columns of data from df.

# Check if this is correct (check the dimensions and compare the entries using the head or tail command).

import pandas as pd

df = pd.read_csv('week4/espeni_raw.csv')

def selectColumns(df, l):
    for column in l:
        if column not in df.columns:
            return None
    return df[l]

l = ['POWER_NGEM_EMBEDDED_WIND_GENERATION_MW','POWER_NGEM_IFA_FLOW_MW','POWER_ELEXM_WIND_MW']
dfs = selectColumns(df,l)
print(dfs)