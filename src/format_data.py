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
    """ """
    data_path: str
    raw_col_name: str

    def txt_to_df(self) -> pd.DataFrame:
        """Load all .txt files in data_path into a pd.DataFrame, with one row per file"""

        files = os.listdir(self.data_path)
        txt_files = [f for f in files if f[4:] == ".txt"]

        df_out = pd.DataFrame(columns=[self.raw_col_name])

        for f in txt_files:
            with open((self.data_path + f), "r") as fi:
                txt = fi.read().replace("\n", " ")
                df_out = df_out.append({self.raw_col_name: txt}, ignore_index=True)
                fi.close()

        return df_out
