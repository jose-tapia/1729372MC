cantidad = 0

def bubblesort(arr):
    aux=arr[:]
    global cantidad
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if(aux[j]>aux[j+1]):
                aux[j],aux[j+1]=aux[j+1],aux[j]
                cantidad+=1
    return aux

import random
p = random.sample(range(0,200),100)
print(p)
psorted=bubblesort(p)
print(cantidad)
print(psorted)
