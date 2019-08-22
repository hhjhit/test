# encoding=utf-8
import jieba

result_lcut = jieba.lcut("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")
print result_lcut
print " ".join(result_lcut)
print " ".join(jieba.lcut_for_search("小明硕士毕业于中国科学院计算所，后在哈佛大学深造"))

print('/'.join(jieba.cut('如果放到旧字典中将出错。', HMM=False)))
jieba.suggest_freq(('中', '将'), True)
print('/'.join(jieba.cut('如果放到旧字典中将出错。', HMM=False)))

import jieba.analyse as analyse
lines = open('NBA.txt').read()
print "  ".join(analyse.extract_tags(lines, topK=20, withWeight=False, allowPOS=()))

print "\n"
import jieba.analyse as analyse
lines = open('NBA.txt').read()
print "  ".join(analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')))
print "---------------------我是分割线----------------"
print "  ".join(analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n')))
