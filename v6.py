# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/1/3

from gensim import corpora,models,similarities
import jieba
from collections import defaultdict

# 1.导入句子
sentence1 = "我喜欢吃番薯"
sentence2 = "番薯是个好东西"
sentence3 = "利用python进行文本挖掘"

data1 = jieba.cut(sentence1)
data2 = jieba.cut(sentence2)
data3 = jieba.cut(sentence3)

data11 = ""
for item in data1:
    data11 += item+" "
data21 = ""
for item in data2:
    data21 += item+" "
data31=""
for item in data3:
    data31 += item+" "

documents = [data11,data21,data31]
text3 = [[word for word in document.split()]
        for document in documents]

dictionary = corpora.Dictionary(text3)
featureNum = len(dictionary.token2id.keys())
dictionary.save("dictionary.txt")#保存语料库

corpus = [dictionary.doc2bow(text) for text in text3]
tfdif = models.TfidfModel(corpus)

query = "吃东西"
data4 = jieba.cut(query)
data41 = ""
for item in data4:
    data41 += item+" "
new_doc = data41
# 8.将对比句子转换为稀疏向量
new_vec = dictionary.doc2bow(new_doc.split())
index = similarities.SparseMatrixSimilarity(tfdif[corpus],num_features=featureNum)

sim = index[tfdif[new_vec]]
for i in range(len(sim)):
    print("查询与第"+str(i+1)+"句话的相似度为:"+str(sim[i]))