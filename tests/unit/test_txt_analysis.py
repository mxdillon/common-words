#!/usr/bin/python
# coding=utf-8
"""Test txt_analysis class and its methods.
:usage:
    To be run with every commit
:authors
    MD at 26/09/20
"""

import numpy as np
import pandas as pd
import pytest
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse.csr import csr_matrix


def test_tfidf_output_Xshape(analysis_class):
    """Check shape of tfidf matrix. Ensures stopwords included."""
    assert analysis_class.X.shape == (5, 10), "Error: matrix wrong shape. Check stopwords parameter set to True."


def test_tfidf_output_Xtype(analysis_class):
    assert type(analysis_class.X) == csr_matrix


def test_tfidf_output_vtype(analysis_class):
    assert type(analysis_class.tfidf_vect) == TfidfVectorizer


def test_count_vect_output_shape(analysis_class):
    """Check shape of count matrix. Ensures stopwords included."""
    assert analysis_class.count_matrix.shape == (
        5, 10), "Error: matrix wrong shape. Check stopwords parameter set to True."


@pytest.mark.parametrize("arr,idx,word",
                         [([0, 1, 1, 1, 1], 0, "cheese"),
                          ([0, 1, 0, 0, 1], 2, "ham")],
                         ids=["hamcol", "cheesecol"])
def test_count_vect_tfidf_same_order(arr, idx, word, analysis_class):
    """Check the order of the columns is the same in both count_vector and tfidf matrices.
    This is verified by using the word idx from the tfidf vocab object and the count_matrix from count_vect."""
    np.testing.assert_array_equal(analysis_class.count_matrix[:, idx], arr)
    assert analysis_class.vocab[idx] == word


def test_top_n_words(analysis_class):
    """Check tfidf score indices have been sorted into descending order."""
    np.testing.assert_array_equal(analysis_class.sorted_scores[0, :5], [7, 3, 9, 8, 6])


@pytest.mark.parametrize("d,i,w,s,c,c_all",
                         [(0, 0, "testfile", 0.7071067811865475, 1, 1),
                          (3, 1, "words", 0.0, 0, 1),
                          (2, 0, "words", 0.5490363340004775, 1, 1)],
                         ids=["first", "second", "third"])
def test_collect_results(d, i, w, s, c, c_all, analysis_class):
    """Check the correct results are returned. Need to ensure that the indexing on the arrays is correct."""
    word, score, count, count_all = analysis_class._collect_results(doc=d, term=i)
    assert (word, score, count, count_all) == (w, s, c, c_all)


@pytest.mark.parametrize("data,idx",
                         [(({"filename": "doc1.txt", "word": "testfile", "tfidf_score": 0.7071067811865475,
                             "count_doc": 1, "count_corpus": 1}), 0),
                          (({"filename": "doc5.txt", "word": "cheese", "tfidf_score": 0.4015651234424611,
                             "count_doc": 1, "count_corpus": 4}), 14)],
                         ids=["fisrtrow", "lastrow"])
def test_summary_df_top(data, idx, df_analysis):
    """Check top and bottom rows of df_out are equal to expected. It must be of the format filename; word; tfidf score.
    Checking last row to ensure iteration over both loops is executed correctly."""
    pd.testing.assert_series_equal(df_analysis.iloc[idx], pd.Series(data, name=idx))
