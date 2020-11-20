def panduan():
    nums = []
    iNumStr = input("请输入数字(回车退出):")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出):")
    print("要判定的列表为:{}".format(nums))
    nums1=[]
    for i in nums:
        if i not in nums1:
            nums1.append(i)
    if len(nums1)!=len(nums):
        print("列表存在重复元素")
    else:
        print("列表不存在重复元素")
