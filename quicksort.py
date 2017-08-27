cantidad = 0

def quicksort(arr):
    global cantidad
    if arr==[] :
        return []
    m=arr[0]
    cnt=0
    left=[]
    right=[]
    for k in arr:
        cantidad+=1
        if k==m:
            cnt+=1
        else:
            if k<m:
                left.append(k)
            else:
                right.append(k)
    return quicksort(left)+([m]*cnt)+quicksort(right)
