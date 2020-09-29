#!/usr/bin/python
# coding=utf-8
"""Run analysis over corpus.
:usage:
    Perform TFIDF analysis over the corpus and format the results table.
:authors
    MD at 25/09/20
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from typing import Tuple


class MostImportant:
    """For a given corpus, performs Term Frequency Inverse Document Frequency and returns a DataFrame summarising the
    results."""

    def __init__(self, raw_data: pd.DataFrame, raw_col_name: str):
        """
        :param raw_data: pd.DataFrame with 2 cols: "filename" and another containing the raw text, specified below.
        :param raw_col_name: name of the column containing the raw body text of the documents.
        """
        self.raw_data = raw_data
        self.raw_col_name = raw_col_name
        self.corpus = self.raw_data[self.raw_col_name].tolist()
        self.X = None
        self.tfidf_vect = None
        self.vocab = None
        self.count_vect = None
        self.sorted_scores = None
        self.tfidf_scores = None

    def _tfidf(self) -> None:
        """Fits tfidf vectorizer to corpus."""
        self.tfidf_vect = TfidfVectorizer(stop_words='english')
        self.X = self.tfidf_vect.fit_transform(self.corpus)
        self.vocab = self.tfidf_vect.get_feature_names()

    def _count_vectorizer(self) -> None:
        """Fits count vectorizer to corpus (used in final summary DataFrame)."""
        self.count_vect = CountVectorizer(stop_words="english")
        self.count_matrix = self.count_vect.fit_transform(self.corpus).toarray()

    def _top_n_words(self) -> None:
        """Sorts tfidf scores for each document into descending order and store the indices as self.sorted_scores."""
        self.tfidf_scores = self.X.toarray()
        self.sorted_scores = np.zeros(self.X.shape, dtype=int)

        for i in range(self.X.shape[0]):
            sorted_scores_asc = np.argsort(self.tfidf_scores[i, :])
            self.sorted_scores[i, :] = np.flip(sorted_scores_asc)

    def _collect_results(self, doc: int, term: int) -> Tuple[str, float, int, int]:
        """Retrieves the word, tfidf score, occurrences of the word in the document and occurrences of the word in the
        entire corpus from the data previously calculated.

        :param doc: int representing the document number to index on.
        :param term: int representing the rank of word to index on. Note this is not the index of the word in
        self.vocab: that is calculated within this method and assigned to word_idx.
        :return: tuple containing the word, tfidf score, count in doc and count in corpus.
        """
        word_idx = self.sorted_scores[doc, term]
        w = self.vocab[word_idx]
        s = self.tfidf_scores[doc, self.sorted_scores[doc, term]]

        c = self.count_matrix[doc, word_idx]
        c_all = np.sum(self.count_matrix[:, word_idx])

        return w, s, c, c_all

    def summary_df(self, n: int) -> pd.DataFrame:
        """Creates summary dataframe showing the filename; word; tfidf score; count; and count_corpus for the top n
        words in each doc. Executes all private methods in the class.

        :param n: number of most important terms to return from each document.
        :return: pd.DataFrame summarising the n words from each doc with the highest tfidf score.
        """

        self._tfidf()
        self._count_vectorizer()
        self._top_n_words()

        df_out = pd.DataFrame([])
        cols = ["filename", "word", "tfidf_score", "count_doc", "count_corpus"]

        for i in range(self.X.shape[0]):
            f = self.raw_data["filename"][i]
            for j in range(n):
                w, s, c, c_all = self._collect_results(i, j)
                new_row = pd.DataFrame({cols[0]: f, cols[1]: w, cols[2]: s, cols[3]: c, cols[4]: c_all}, index=[0])
                df_out = df_out.append(new_row, ignore_index=True)

        return df_out
