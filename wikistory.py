import time
import dask
import pandas as pd


import dask.dataframe as dd

# import modin.pandas as pd
from dask.distributed import Client

client = Client(n_workers=6, threads_per_worker=2, processes=False, memory_limit='20GB')
client

print("Parsing parquet.")
input_data = dd.read_parquet('data/input.parquet', engine='pyarrow')
print("Adding day columns.")
input_data['timestamp'] = dd.to_datetime(input_data.timestamp,format='%Y/%m/%d %H:%M')
input_data['day'] = input_data.timestamp.dt.date

print(input_data['day'].head())
# input_data['timestamp'] = pd.to_datetime(input_data['timestamp'])
# input_data['day'] = input_data.timestamp.dt.date

# input_data = input_data[input_data.page_title != 'Tartışma:Anasayfa']

# # day_title_grouped = input_data.groupby(['day','page_title']).count()

# day_title_grouped = input_data.groupby(['day','page_title'])['page_title'].apply(len)


print(input_data.head())

input_data.to_parquet('data/with_day.parquet', engine='pyarrow')



# output to static HTML file
# output_file("log_lines.html")

# source = ColumnDataSource(day_title_grouped)

# p = figure()
# # add some renderers
# p.circle(x='x_values', y='y_values', source=source)
# # p.circle(x, x, legend_label="y=x", fill_color="white", size=8)
# # p.line(x, y0, legend_label="y=x^2", line_width=3)
# # p.line(x, y1, legend_label="y=10^x", line_color="red")
# # p.circle(x, y1, legend_label="y=10^x", fill_color="red", line_color="red", size=6)
# # p.line(x, y2, legend_label="y=10^x^2", line_color="orange", line_dash="4 4")

# # show the results
# show(p)
# # for row in group_date_title.iterrows():
# #     print(row[1].page_title)

