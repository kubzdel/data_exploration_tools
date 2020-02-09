from sklearn.feature_extraction.text import CountVectorizer

import pandas as pd
import numpy as np


def cos_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


d1 = "John give book Mary"
d2 = "John read book love Mary"
d3 = "John think Mary love?"
d4 = "John think book good gift"
corpus = [d1, d2, d3, d4]

# making one hot vector
wc = CountVectorizer()
x = wc.fit_transform(corpus)
wcX = np.array(x.toarray())

# term frequency
N = wcX.shape[0]
tf = np.array([wcX[i, :] / np.sum(wcX, axis=1)[i] for i in range(N)])

tf = (tf > 0).astype(np.int_)  # for binary representation!

# inverse documents frequency
df = np.count_nonzero(wcX, axis=0)
idf = np.log(N / df)

tfidf = tf * idf

print(pd.DataFrame(tfidf, columns=wc.get_feature_names()).to_string())

# q is tf query
q = [0, 0, 0, 0, 0, 1, 1, 0, 0]

dfq = np.count_nonzero(wcX, axis=0)
idfq = np.log(N / df) * q

doc_num = 0

print(f"Query and {doc_num} document tfidf similarity =  {cos_sim(tfidf[doc_num], idfq)}")
