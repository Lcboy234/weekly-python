import pandas as pd
data = pd.read_csv('week4/espeni_raw.csv')

def selectDate(df, c, date):
    if c in df.columns:
        # df[c] == date
        # This compares every value in column c to date.
        # The result is a Boolean Series: True where the value matches, False where it doesn’t.

        # df[ ... ]
        # When you pass a Boolean Series inside df[ ... ], 
        # pandas selects only the rows where the value is True.
        return df[df[c] == date]
    else:
        return None

final = selectDate(data, 'ELEXM_SETTLEMENT_DATE', '2009-01-01')
print(final)