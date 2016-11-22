__author__ = '0138695'
from gensim import corpora

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

stoplist = set("for a of the and to in".split())
texts = [[word for word in document.lower().split() if word not in stoplist]
        for document in documents]

from collections import defaultdict

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token]> 1] for text in texts]

from pprint import pprint
pprint(texts)
dictonary = corpora.Dictionary(texts)
dictonary.save("dee.dict")
print dictonary
print dictonary.token2id
