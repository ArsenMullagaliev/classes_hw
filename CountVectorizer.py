class CountVectorizer():

    from collections.abc import Iterable

    def __init__(self):
        self._features = list()
        self._tfidf = list()

    def fit_transform(self, raw_documents: Iterable) -> list:
        from string import punctuation
        self._features = list()
        self._tfidf = list()

        for doc in raw_documents:
            if not isinstance(doc, str):
                doc = str(doc)

            doc = doc.lower()
            doc = doc.translate(str.maketrans('', '', punctuation))
            doc = doc.split()

            doc_frequencies = dict.fromkeys(self._features, 0)
            for word in doc:
                doc_frequencies[word] = doc_frequencies.setdefault(word, 0) + 1

            self._features = list(doc_frequencies.keys())
            self._tfidf.append(list(doc_frequencies.values()))

        for frequency_list in self._tfidf:
            frequency_list = frequency_list.extend(
                [0] * (len(self._features) - len(frequency_list))
            )

        return self._tfidf

    def get_feature_names(self) -> list:
        return self._features


if __name__ == '__main__':

    corpus = [
     'Crock Pot Pasta Never boil pasta again',
     'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
