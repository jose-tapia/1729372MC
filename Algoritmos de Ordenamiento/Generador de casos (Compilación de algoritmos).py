import copy
import random

cantidad=0

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

def bubblesort(arr):
    aux=arr[:]
    global cantidad
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if(aux[j]>aux[j+1]):
                aux[j],aux[j+1]=aux[j+1],aux[j]
            cantidad+=1
    return aux

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

def arrayRandom(n):
	arr=[]
	for i in range(n):
		arr.append(random.randint(0,10000))
	return arr

dat=open("datosParaGraficar.txt","w")
dat.write("Lenght Selection Bubble Insertion Quick\n")
for size in range(10,1000,10):
	for repetir in range(15):
		arr=arrayRandom(size)
		cantidad=0
		selectionsort(arr)
		cntS,cantidad=cantidad,0
		bubblesort(arr)
		cntB,cantidad=cantidad,0
		insertionsort(arr)
		cntI,cantidad=cantidad,0
		quicksort(arr)
		cntQ,cantidad=cantidad,0
		dat.write("%d %d %d %d %d\n" % (size,cntS,cntB,cntI,cntQ))
dat.close()
