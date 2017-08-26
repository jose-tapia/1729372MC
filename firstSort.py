cnt=0
def minimo(arr):
    k=arr[0]
    global cnt
    for w in arr:
        cnt+=1
        if(w<k):
            k=w
    return k

def ordenar(arr):
    aux=arr
    arrsort=[]
    for k in range(len(arr)):
        w=minimo(arr)
        arr.remove(w)
        arrsort.append(w)
    arr=aux
    return arrsort

import random
p=random.sample(range(0,100),40)
print(p)
psort=ordenar(p)
print(cnt)
print(psort)
