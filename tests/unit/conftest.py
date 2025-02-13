#!/usr/bin/python
# coding=utf-8
"""Fixtures for all tests.
:usage:
    To be run with every commit
:authors
    MD at 25/09/20
"""

import pytest
from src import format_data, txt_analysis


@pytest.fixture(scope="session")
def format_class():
    """Init the formatting class."""
    return format_data.FormatData(data_path="./tests/unit/test-data/", raw_col_name="rawtext")


@pytest.fixture(scope="session")
def df_rawtext(format_class):
    """Return df with rawtext files."""
    return format_class.txt_to_df()


@pytest.fixture(scope="session")
def analysis_class(df_rawtext):
    """Init the analysis class."""
    cl = txt_analysis.MostImportant(raw_data=df_rawtext, raw_col_name="rawtext")
    cl._tfidf()
    cl._count_vectorizer()
    cl._top_n_words()
    return cl


@pytest.fixture(scope="session")
def df_analysis(analysis_class):
    """Return df with tfidf analysis."""
    return analysis_class.summary_df(n=3)


@pytest.fixture(scope="session")
def save_folder():
    return "./results"


@pytest.fixture(scope="session")
def save_file():
    return "common-words.csv¬"
