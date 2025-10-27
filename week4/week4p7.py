import pandas as pd
data = pd.read_csv('week4/espeni_raw.csv')

def selectRangeColumn(df, c, lo):
    if c in df.columns:
        # df[[c]]
        # df[[c]] selects only column c, but keeps it as a DataFrame (2D), not a Series.
        # df[c] -> Series
        # df[[c]] -> DataFrame with one column.

        # df[[c]][df[c] >= lo]
        # Here, we use the Boolean Series as a filter on the DataFrame.
        # It keeps only the rows where the condition df[c] >= lo is True.
        return df[[c]][df[c] >= lo]
    else:
        return None

test = selectRangeColumn(data, 'POWER_NGEM_EMBEDDED_WIND_GENERATION_MW', 5000)
print(test)