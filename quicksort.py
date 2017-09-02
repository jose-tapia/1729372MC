cantidad = 0

def quicksort(arr):
    global cantidad
    if arr==[] :
        return []
    m=arr[0]
    left=[]
    right=[]
    for k in arr[1:]:
        if k<m:
            left.append(k)
        else:
            right.append(k)
        cantidad+=1
    return quicksort(left)+[m]+quicksort(right)

import random
p = random.sample(range(0,200),100)
print(p)
psorted=quicksort(p)
print(cantidad)
print(psorted)
