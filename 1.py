# encoding=utf-8
import jieba

result_lcut = jieba.lcut("С��˶ʿ��ҵ���й���ѧԺ�����������ڹ����ѧ����")
print result_lcut
print " ".join(result_lcut)
print " ".join(jieba.lcut_for_search("С��˶ʿ��ҵ���й���ѧԺ�����������ڹ����ѧ����"))

print('/'.join(jieba.cut('����ŵ����ֵ��н�����', HMM=False)))
jieba.suggest_freq(('��', '��'), True)
print('/'.join(jieba.cut('����ŵ����ֵ��н�����', HMM=False)))

import jieba.analyse as analyse
lines = open('NBA.txt').read()
print "  ".join(analyse.extract_tags(lines, topK=20, withWeight=False, allowPOS=()))

print "\n"
import jieba.analyse as analyse
lines = open('NBA.txt').read()
print "  ".join(analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')))
print "---------------------���Ƿָ���----------------"
print "  ".join(analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n')))
