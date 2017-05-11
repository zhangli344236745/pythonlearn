# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/5/11

import jieba
import  jieba.posseg as pseg
jieba.load_userdict("dict.txt")
words = jieba.cut("他来到了网易杭研大厦")
print "/".join(words)
print type(words)

words2 =jieba.cut("我们中出了一个叛徒",HMM=False)
jieba.suggest_freq(('中出'),True)
print "/".join(words2)

words3 = pseg.cut("我爱北京天安门")
for word , flag in words3:
	print("%s %s" % (word,flag))