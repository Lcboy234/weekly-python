import pandas as pd
data = pd.read_csv('week4/espeni_raw.csv')

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
meds = medianDate(data, 'ELEXM_SETTLEMENT_DATE', '2021-10-02', l)
print(meds.head(3))

import json

def saveMedianAsJson(df, cDate, date, l, filename):
    # Get the median values as a Series
    meds = medianDate(df, cDate, date, l)
    
    # If medianDate returned None (e.g., wrong column), do nothing
    if meds is None:
        return None

    # Convert Series to dictionary
    meds_dict = meds.to_dict()
    
    # Save dictionary as a JSON file
    with open(filename, 'w') as f:
        json.dump(meds_dict, f, indent=4)
    
    return meds_dict

result_dict = saveMedianAsJson(data, 'ELEXM_SETTLEMENT_DATE', '2021-10-02', l, 'medians.json')
print(result_dict)
print(meds.index)