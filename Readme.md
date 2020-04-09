# Requirements
### System tools
    pigz -> for faster parallel extractions

### Python libs
    pip install wiki_dump_parser
    python -m wiki_dump_parser .\data.xml

# Preparation
First thing is to create the csv file we will use. For that we need to use ```wiki_dump_parser```. After installation and conversion to csv,
the next step is to convert the data into *parquet* for faster processing.
This can be achieved with ```prepare.ipynb``` notebook.