def fbnq():
    ss=[1,1]
    j=1
    k=1
    for i in range (30):
        j+=k
        ss.append(j)
        j,k=k,j
        print(ss)
        
        
        
        
