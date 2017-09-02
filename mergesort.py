cantidad = 0

def unir(izq,der):
    arr=[]
    global cantidad
    n,m,i,j=len(izq),len(der),0,0
    while (i!=n) and (j!=m):
        if(izq[i]<der[j]):
            arr.append(izq[i])
            i+=1
        else:
            arr.append(der[j])
            j+=1
        cantidad+=1
    return arr+izq[i:]+der[j:]

def mergesort(arr):
    n=len(arr)
    if n<=1:
        return arr
    izq=arr[:int(n/2)]
    der=arr[int(n/2):]
    izq=mergesort(izq)
    der=mergesort(der)
    return unir(izq,der)

import random
p = random.sample(range(0,200),100)
print(p)
psorted=mergesort(p)
print(cantidad)
print(psorted)
