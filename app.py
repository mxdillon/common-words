#!/usr/bin/python
# coding=utf-8
"""Run the data preparation and analysis. Save results to local directory.
:usage:
    To execute analysis of the corpus.
:authors
    MD at 25/09/20
"""

import logging
import numpy as np
from src import format_data, txt_analysis, save_results

if __name__ == "__main__":
    logging.basicConfig(filename='common-words.log', level=logging.DEBUG)

    # Set seed for any stochastic elements. sklearn uses np.random.
    np.random.seed()

    formatter = format_data.FormatData(data_path="./data/", raw_col_name="rawdata")
    raw_data = formatter.txt_to_df()
    logging.info("COMPLETED: formatting data")

    tfidf_analysis = txt_analysis.MostImportant(raw_data=raw_data, raw_col_name="rawdata")
    results_summary = tfidf_analysis.summary_df(n=3)
    logging.info("COMPLETED: tfidf analysis")

    save_results.SaveResults.local_save(df_out=results_summary, save_folder="./results",
                                        save_filename="common-words.csv")
    logging.info("COMPLETED: saving results")
