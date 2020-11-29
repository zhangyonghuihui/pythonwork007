# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:00:36 2020

@author: 123
"""
import time
import random
def sjsc():
    a1=(1976,1,1,0,0,0,0,0,0)             
    a2=(2017,12,31,23,59,59,0,0,0)   
    start=time.mktime(a1)   
    end=time.mktime(a2)     
    #随机生成10个日期字符串
    suijishijianliebiao=[]
    for i in range(23):
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        date=time.strftime("%m-%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
        #print(date)
        suijishijianliebiao.append(date)
        #print(suijishijianliebiao)
        #print(cuonts)
    counts={}
    for word in suijishijianliebiao:
        counts[word] =counts.get(word,0)+1
        if counts[word]>1:
            a=1
            break
        else:
            a=0
    return a
b=0
for i in range(10000):
    sjsc()
   # print(sjsc())
    b+=sjsc()
#print(b)
c=(b/10000)*100
print("进行了10000次随机试验每次生成23个随机生日。")  
print("得到出现相同的生日的次数为{} 概率为{:.2f}%".format(b,c))  
    

    #print(counts)
'''
items =list(counts.items())
items.sort(key=lambda x :x[1],reverse=True)
for i in range (len(counts)):
    #print(i)
    word,count= items[i]
    print("{0:<10}{1:>5}".format(word,count))
'''
