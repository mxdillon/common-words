#!/usr/bin/python
# coding=utf-8
"""Test .
:usage:
    To be run with every commit
:authors
    MD at 28/09/20
"""
import os
import shutil
from src.save_results import SaveResults


def test_save_results_nofolder(df_analysis, save_folder, save_file):
    """Check file saves when no folder exists."""

    if os.path.exists(save_folder) and os.path.isdir(save_folder):
        shutil.rmtree(save_folder)

    SaveResults.local_save(save_folder=save_folder, save_filename=save_file, df_out=df_analysis)

    assert os.path.isdir(save_folder), "Error: directory hasn't been created."
    assert os.path.exists(os.path.join(save_folder, save_file)), "Error: .csv hasn't been saved in specified " \
                                                                 "location."

    shutil.rmtree(save_folder)


def test_save_results_folder(df_analysis, save_folder, save_file):
    """Check file saves when folder already present."""

    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    SaveResults.local_save(save_folder=save_folder, save_filename=save_file, df_out=df_analysis)

    assert os.path.isdir(save_folder), "Error: directory hasn't been created."
    assert os.path.exists(os.path.join(save_folder, save_file)), "Error: .csv hasn't been saved in specified " \
                                                                 "location."

    shutil.rmtree(save_folder)
