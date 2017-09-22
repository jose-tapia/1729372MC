cantidad = 0

def insertionsort(arr):
    global cantidad
    arrsort=arr[:]
    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if(arrsort[j]>arrsort[j+1]):
                arrsort[j],arrsort[j+1]=arrsort[j+1],arrsort[j]
                cantidad+=1
            else:
                break
    return arrsort

import random
p = random.sample(range(0,200),100)
print(p)
psorted=insertionsort(p)
print(cantidad)
print(psorted)
