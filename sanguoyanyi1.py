# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:03:41 2020

@author: 123
"""
import jieba
txt=open("三国演义.txt","r",encoding='utf-8').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x [1],reverse=True)
for i in range(15):
    word,count =items[i]
    print("{0:<10}{1:>15}".format(word,count))