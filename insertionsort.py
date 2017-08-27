cantidad = 0

def insertionsort(arr):
    global cantidad
    arrsort=[]
    for k in arr:
        arrsort.append(k)
        for i in range(len(arrsort)-2,-1,-1):
            if(arrsort[i]>arrsort[i+1]):
                q=arrsort[i]
                arrsort[i]=arrsort[i+1]
                arrsort[i+1]=q
                cantidad+=1
            else:
                break
    return arrsort
