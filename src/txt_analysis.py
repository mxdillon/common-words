#!/usr/bin/python
# coding=utf-8
"""Run analysis over corpus.
:usage:
    To be run with every commit
:authors
    MD at 25/09/20
"""

from dataclasses import dataclass
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

@dataclass
class MostImportant:
    raw_data: pd.DataFrame
    raw_col_name: str

    def tfidf(self) -> TfidfVectorizer:
        """ """
        corpus = self.raw_data[self.raw_col_name].tolist()
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit(corpus)
        return X


# do tfidf
# select x most important words across all docs
# find occurrences in each doc - return count and 1 example from each