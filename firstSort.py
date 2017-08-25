def minimo(arr):
    k=arr[0]
    for w in arr:
        if(w<k):
            k=w
    return k

def ordenar(arr):
    arrsort=[]
    for k in range(len(arr)):
        w=minimo(arr)
        arr.remove(w)
        arrsort.append(w)
    return arrsort
