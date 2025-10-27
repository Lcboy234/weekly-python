import pandas as pd
data = pd.read_csv('week4/espeni_raw.csv')

def selectNumericColumns(df):
    # Select columns with numeric dtypes (float64 or int64)
    return df.select_dtypes(include=['float64', 'int64'])

selected = selectNumericColumns(data)
print(selected)