import pandas as pd

df = pd.read_csv('week4part2/espeni_raw.csv')

i = ['POWER_NGEM_EMBEDDED_WIND_GENERATION_MW','POWER_NGEM_IFA_FLOW_MW','POWER_ELEXM_WIND_MW']

drop_row = df[i].dropna()

# convert to numpy
numpy_convert = drop_row.to_numpy()

# display it
print(numpy_convert.shape, numpy_convert[0:5])
