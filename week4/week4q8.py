import pandas as pd
df = pd.read_csv('week4/espeni_raw.csv')

def medianDate(df, cDate, date, l):
    # Check if cDate column exists
    if cDate not in df.columns:
        return None
    
    # Filter rows matching the given date
    filtered = df[df[cDate] == date]
    
    # Compute median for the selected columns
    # filtered[l] = from those rows, keep only the columns listed in l.
    return filtered[l].median()

# Test
l = ['POWER_NGEM_EMBEDDED_WIND_GENERATION_MW', 'POWER_NGEM_IFA_FLOW_MW', 'POWER_ELEXM_WIND_MW']
meds = medianDate(df, 'ELEXM_SETTLEMENT_DATE', '2021-10-02', l)
print(meds.head(3))