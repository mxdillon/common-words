#!/usr/bin/python
# coding=utf-8
"""Test txt_analysis class and its methods.
:usage:
    To be run with every commit
:authors
    MD at 26/09/20
"""

import sklearn

def test_tfidf_output(analysis_class):
    """ """
    assert type(analysis_class.tfidf()) == sklearn.feature_extraction.text.TfidfVectorizer
