#!/usr/bin/python
# coding=utf-8
"""Run the data preparation and analysis.
:usage:
    To execute ananlysis of the corpus.
:authors
    MD at 25/09/20
"""

from src import format_data, txt_analysis

if __name__ == "__main__":
    print('test')

formatter = format_data.FormatData(data_path="./data/", raw_col_name="rawdata")
raw_data = formatter.txt_to_df()

