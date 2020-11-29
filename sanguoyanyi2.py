# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:02:35 2020

@author: 123
"""
import jieba
excludes={"将军","却说","二人","不可","荆州","不能","如此","商议","如何","主公","军士","左右","兵马","引兵","次日","大喜","军马","天下","东吴","于是","今日","魏兵","不敢","陛下","人马","都督","汉中","不知","一人","众将","后主","蜀兵",}
txt=open("三国演义.txt","r",encoding='utf-8').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="诸葛亮"or word =="孔明曰":
        reword="孔明"
    elif word=="关公"or word=="云长":
        reword="关羽"
    elif word=="玄德"or word=="玄德曰":
        reword="刘备"
    elif word=="孟德"or word=="丞相":
        reword="曹操"
    else:
        reword= word
    counts[reword]=counts.get(reword,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x [1],reverse=True)
for i in range(10):
    word,count =items[i]
    print("{0:<10}{1:>15}".format(word,count))
