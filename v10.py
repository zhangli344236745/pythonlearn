# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/3/28
import sys
from operator import add
from pyspark.conf import SparkConf
from pyspark.context import SparkContext



if __name__ == "__main__":
    conf = SparkConf()
    conf.setMaster("local").setAppName("My app")
    sc = SparkContext(conf=conf)
    # lines = sc.textFile('words.txt')
    # count=lines.count()
    # print(count)
    # counts = lines.flatMap(lambda x: x.split(' ')) \
    #               .map(lambda x: (x, 1)) \
    #               .reduceByKey(add)
    # output = counts.collect()
    # for (word, count) in output:
    #     print("%s: %i" % (word, count))
    #
    # sc.stop()