
import pandas as pd

csv_data = pd.read_csv('data.csv', quotechar ='|', index_col = False)
csv_data.to_parquet('data/input.parquet', engine='pyarrow')