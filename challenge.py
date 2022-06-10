

import pandas as pd

df = pd.read_excel('SWR.xlsx')
# Check the data type of columns, in order to trim last char from lan ip subnet
# print(df.dtypes)
# convert object to string and trim last char!!!

# df['LAN IP subnet'] = df['LAN IP subnet'].astype("|S")
# print(df.dtypes)

# Replace part the value of one column with the value from a different column

df['udp array'] = df.apply(lambda x:x['udp array'].replace('<<TrainSubnet>>', x['LAN IP subnet']), axis=1)

for index, row in df.iterrows():
     print(index,row['udp array'])  