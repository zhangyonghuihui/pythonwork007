def getNum():
    nums = []
    iNumStr = input("请输入数字(回车退出):")
    while iNumStr != "":    #死循环判断为空退出，不为空就继续输入并添加到列表里
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出):")
    return nums
def mean (numbers):         
    s = 0.0                  
    for num in numbers:
        s = s +num           
    return s / len(numbers)  
# 计算方差,需要算出平均值
def dev(numbers,mean):             
    sdev = 0.0                     
    for num in numbers:             
        sdev = sdev + (num - mean)**2  
    return pow(sdev / (len(numbers)-1),0.5) 
#计算中位数
def median(numbers):
    numbers.sort()   #进行原列表排序，使用sorted排序必须有返回值numbers = sorted(numbers)
    size = len(numbers)   
    if size % 2 ==0:    #判断为偶数取中间两位数，
        med = (numbers[size//2-1] + numbers[size//2])/2  #//为整除，/为浮点数
    else:              #或为奇数，切片总长度除2，取中间一位
        med = numbers[size//2]
    return med
 
n = getNum()
m = mean(n)
print("平均值:{},方差:{:.2},中位数:{}".format(m,dev(n,m),median(n)))
