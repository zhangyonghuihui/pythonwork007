import random
import string
s=string.ascii_letters+string.digits         #“+”为字符串连接符
ls=[]                  #初始化ls为空列表
ls=list(s)           #将字符串s中的字符存放于列表ls中
def getkey(): 
        key=[]
        print("生成的随机密码为:")              #此行可省略
        for i in range(8):
            k=random.choice(ls)               #choice()函数可从序列类型中随机返回一个元素
            key.append(k)					#将新元素加入到key列表的末尾
        for n in key:                      #遍历key列表
            print(n,end="")              #以一行的格式打印密码
        print("\n")
getkey()
