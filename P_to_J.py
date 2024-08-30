import pandas as pd

df = pd.read_parquet('business.parquet')

json_data = df.to_json(orient='records', lines=True )

with open('business.json', 'w') as json_files:
    json_files.write(json_data)