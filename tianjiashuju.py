'''def getNum():
    nums = []
    iNumStr=input ("请输入数字（直接输入回车退出）：")
    while iNumStr !="":
        nums.append(eval(iNumStr))
        iNumstr=input("请输入数字（直接输入回车退出）")
    return nums

'''
def getNum():
    nums = []
    iNumStr = input("请输入数字(回车退出):")
    while iNumStr != "":    #死循环判断为空退出，不为空就继续输入并添加到列表里
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出):")
    return nums
getNum()
