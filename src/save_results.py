#!/usr/bin/python
# coding=utf-8
"""Class to save results in local directory. In prod will want to save to a persistent disk.
:usage:
    After running tfidf analysis save the resulting dataframe.
:authors
    MD at 26/09/20
"""

import os
import pandas as pd


class SaveResults:
    """Save DataFrame in local directory."""

    @staticmethod
    def local_save(df_out: pd.DataFrame, save_folder: str = "./results", save_filename: str = "common-words.csv") -> \
        None:
        """Saves DataFrame at the specified location.

        :param df_out: DataFrame to save
        :param save_folder: folder name. If doesn't exist it will be created.
        :param save_filename: file name. Must include .csv suffix.
        :return: None
        """
        if not os.path.exists(save_folder):
            os.mkdir(save_folder)

        df_out.to_csv(os.path.join(save_folder, save_filename))
