def huatu():
    lf=list("142573")
    yx=[]
    sx="↑"
    xx="↓"
    a=len(lf)
    for i in range (a-1):
        b=eval(lf[i+1])-eval(lf[i])
        if b>0:
            c=b*sx
            yx.append(c)
        else:
            c=b*(-1)*xx
            yx.append(c)
    print(yx)

