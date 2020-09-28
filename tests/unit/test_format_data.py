#!/usr/bin/python
# coding=utf-8
"""Test format_data class and its methods.
:usage:
    To be run with every commit
:authors
    MD at 25/09/20
"""


def test_txt_to_df_rows(df_rawtext):
    assert df_rawtext.shape[0] == 5, "Error: dataframe not formatted as expected. Check #rows."


def test_txt_to_df_cols(df_rawtext):
    assert df_rawtext.shape[1] == 2, "Error: dataframe not formatted as expected. Check #cols."


def test_txt_to_df_newlines(df_rawtext):
    assert "Hello This is testfile 1" in df_rawtext["rawtext"].tolist(), \
        "Error: dataframe not formatted as expected. Check conversion of '\n' to ' '."
