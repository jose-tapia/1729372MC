cantidad = 0

def unir(izq,der):
    arr=[]
    while ((izq!=[])and(der!=[])):
        if(izq[0]<der[0]):
            arr.append(izq[0])
            izq.remove(izq[0])
        else:
            arr.append(der[0])
            der.remove(der[0])
        cantidad+=1
    return arr+izq+der

def mergesort(arr):
    if len(arr)<=1:
        return arr
    izq=[]
    for i in range(0,int(len(arr)/2)):
        izq.append(arr[i])
    der=[]
    for i in range(int(len(arr)/2),len(arr)):
        der.append(arr[i])
    izq=mergesort(izq)
    der=mergesort(der)
    return unir(izq,der)
