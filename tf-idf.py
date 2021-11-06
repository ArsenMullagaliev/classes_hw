from typing import Iterable, List
from string import punctuation
import math


class CountVectorizer():

    def __init__(self):
        self._features = []
        self._count_matrix = []

    def fit_transform(self, raw_documents: Iterable[str]) -> List[List[int]]:
        self._features = []
        self._count_matrix = []

        for doc in raw_documents:
            doc = doc.lower()
            doc = doc.translate(str.maketrans('', '', punctuation))
            doc_as_list_of_str = doc.split()
            doc_frequencies = dict.fromkeys(self._features, 0)
            for word in doc_as_list_of_str:
                doc_frequencies[word] = doc_frequencies.setdefault(word, 0) + 1
            self._features = list(doc_frequencies.keys())
            self._count_matrix.append(list(doc_frequencies.values()))

        for frequency_list in self._count_matrix:
            frequency_list = frequency_list.extend(
                [0] * (len(self._features) - len(frequency_list))
            )

        return self._count_matrix

    def get_feature_names(self) -> List[str]:
        return self._features


class TfidfTransformer:

    def __init__(self):
        self._tf = []
        self._idf = []
        self._tfidf = []

    def tf_transform(self, count_matrix: List[List[int]]):
        if len(count_matrix) > 0:
            self._tf = []
            for frequency_list in count_matrix:
                new_frequency_list = []
                number_of_words = sum(frequency_list)
                for frequency in frequency_list:
                    new_frequency_list.append(frequency / number_of_words)
                self._tf.append(new_frequency_list)
            return None
        else:
            self._tf = []
            return None

    def idf_transform(self, count_matrix: List[List[int]]):
        if len(count_matrix) > 0:
            self._idf = []
            total_documents = len(count_matrix)
            for ind, _ in enumerate(count_matrix[0]):
                documents_with_feature = 0
                for document_counts in count_matrix:
                    if document_counts[ind] > 0:
                        documents_with_feature += 1
                self._idf.append(math.log((total_documents + 1) / (
                        documents_with_feature + 1)) + 1
                )
            return None
        else:
            self._idf = []
            return None

    def fit_transform(self, count_matrix: List[List[int]]) -> \
            List[List[float]]:
        self.tf_transform(count_matrix)
        self.idf_transform(count_matrix)
        self._tfidf = []
        for row, _ in enumerate(count_matrix):
            document_tfidf = []
            for col, _ in enumerate(count_matrix[0]):
                document_tfidf.append(self._tf[row][col] * self._idf[col])
            self._tfidf.append(document_tfidf)
        return self._tfidf


class TfidfVectorizer(CountVectorizer):

    def __init__(self):
        super().__init__()
        self._tfidftransformer = TfidfTransformer()
        self._tfidf = []

    def fit_transform(self, raw_documents: Iterable[str]):
        self._count_matrix = super().fit_transform(raw_documents)
        self._tfidf = self._tfidftransformer.fit_transform(self._count_matrix)
        return self._tfidf


if __name__ == '__main__':

    corpus = [
     'Crock Pot Pasta Never boil pasta again',
     'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    print('========== CountVectorizer ===========')
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

    print('\n========== TfidfTransformer ===========')
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)

    print('\n========== TfidfVectorizer ===========')
    vectorizer = TfidfVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
