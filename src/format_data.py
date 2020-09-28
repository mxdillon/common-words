#!/usr/bin/python
# coding=utf-8
"""Format data in preparation for analysis.
:usage:
    To be run with every commit
:authors
    MD at 25/09/20
"""

from dataclasses import dataclass
import os
import pandas as pd


@dataclass
class FormatData:
    """Extract data from .txt files and place in DataFrame for analysis."""
    data_path: str
    raw_col_name: str

    def txt_to_df(self) -> pd.DataFrame:
        """Load all .txt files in data_path into a pd.DataFrame, with one row per file.

        :return: DataFrame: Columns show the filename and the raw text contained in the document; one row per doc.
        """

        files = sorted(os.listdir(self.data_path))
        txt_files = [f for f in files if f[4:] == ".txt"]

        f_col = "filename"
        df_out = pd.DataFrame([])

        for f in txt_files:
            with open((self.data_path + f), "r") as fi:
                txt = fi.read().replace("\n", " ")
                df_out = df_out.append(pd.DataFrame({f_col: f, self.raw_col_name: txt}, index=[0]), ignore_index=True)
                fi.close()

        return df_out
