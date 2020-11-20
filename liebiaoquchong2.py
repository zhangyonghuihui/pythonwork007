def panduan2():
    nums = []
    iNumStr = input("请输入数字(回车退出):")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出):")
    print("要判定的列表为:{}".format(nums))
    mo=set(nums)
    print("集合化的列表{}".format(mo))
    if len(mo)!=len(nums):
        print("列表存在重复元素")
    else:
        print("列表不存在重复元素")
  
