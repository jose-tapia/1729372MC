def esPrimo(n):
    if n<=1:
        return False
    m=2
    while(m*m<=n):
        if n%m==0:
            return False
        m+=1
    return True
    
    
print(esPrimo(2))
print(esPrimo(3))
print(esPrimo(4))
print(esPrimo(5))
print(esPrimo(6))
