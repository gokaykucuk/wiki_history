import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_notebook, show
output_notebook()





csv_data = pd.read_csv('data.csv', quotechar ='|', index_col = False)

csv_data['timestamp'] = pd.to_datetime(csv_data['timestamp'])
csv_data['day'] = csv_data.timestamp.dt.date

csv_data = csv_data[csv_data.page_title != 'Tartışma:Anasayfa']

# day_title_grouped = csv_data.groupby(['day','page_title']).count()

day_title_grouped = csv_data.groupby(['day','page_title'])['page_title'].apply(len)



print(day_title_grouped)

day_title_grouped.to_csv('export.csv')

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

