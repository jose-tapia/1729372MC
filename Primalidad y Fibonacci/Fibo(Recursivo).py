def fiborec(n):
    if n==0 or n==1:
        return 1
    return fiborec(n-1)+fiborec(n-2)
    
print(fiborec(10))
print(fiborec(15))
