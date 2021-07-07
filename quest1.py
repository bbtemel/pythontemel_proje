
liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

tmp = []
for x in liste:
    if(type(x) != list):
        tmp.append(x)
    else:
        for y in x:
            if(type(y)!= list):
                tmp.append(y)
            else:
                for z in y:
                    if(type(z) != list):
                        tmp.append(z)
                    else:
                        for xz in z:
                            tmp.append(xz)
