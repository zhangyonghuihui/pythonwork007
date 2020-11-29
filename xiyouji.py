# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:02:35 2020

@author: 123
"""
import jieba
excludes={"我们","和尚","徒弟","真个","这里","宝贝","不得","一个","那里","怎么","两个","长老","什么","不是","只见","原来","不敢","不曾","这个","闻言","那怪","如何","正是","只是","出来","一声","如今","不知"}
txt=open("西游记.txt","r",encoding='utf-8').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="行者"or word =="大圣"or word=="老孙":
        reword="孙悟空"
    elif word=="师父"or word=="三藏":
        reword="唐僧"
    elif word=="呆子"or word=="八戒":
        reword="猪八戒"
    elif word=="小妖"or word=="妖精":
        reword="妖精"
    else:
        reword= word
    counts[reword]=counts.get(reword,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x [1],reverse=True)
for i in range(8):
    word,count =items[i]
    print("{0:<10}{1:>15}".format(word,count))

