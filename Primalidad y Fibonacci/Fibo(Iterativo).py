def fiboiter(n):
    fib=[1,1]
    for k in range(2,n+1):
        fib.append(fib[k-1]+fib[k-2])
    return fib[n]

def fiboiterativo(n):#Notemos que es la misma cantidad de operaciones que fiboiter(n)
    fib1,fib2=1,1
    for k in range(2,n+1):
        ib=fib1+fib2
	      fib1=fib2
	      fib2=fib
    return fib2

print(fiboiter(10))
print(fiboiter(15))
print(fiboiterativo(10))
print(fiboiterativo(15))
