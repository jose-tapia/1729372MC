cantidad = 0

def selectionsort(arr):
    global cantidad
    aux=arr[:]
    for i in range(len(aux)):
        w=aux[i]
        ind=i
        for j in range(i,len(aux)):
            if(aux[j]<w):
                w=aux[j]
                ind=j
                cantidad+=1
        aux[ind]=aux[i]
        aux[i]=w
    return aux

import random
p=random.sample(range(0,100),40)
print(p)
psort=selectionsort(p)
print(cantidad)
print(psort)
