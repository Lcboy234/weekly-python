import pandas as pd
data = pd.read_csv('week4/espeni_raw.csv')

def selectRange(df, c, lo):
    if c in df.columns:
        return df[df[c] >= lo]
    else:
        return None
    
test = selectRange(data, 'POWER_NGEM_EMBEDDED_WIND_GENERATION_MW', 5000)
print(test)