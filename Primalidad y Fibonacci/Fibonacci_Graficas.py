import matplotlib.pyplot as plt

memo={}
cnt=0

def fibonacci(n):
    global memo,cnt
    cnt+=1
    if n==0 or n==1:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n]=fibonacci(n-2)+fibonacci(n-1)
        return memo[n]


def fiborec(n):
    global cnt
    cnt+=1
    if n==0 or n==1:
        return 1
    return fiborec(n-1)+fiborec(n-2)

def fiboiter(n):
    global cnt
    fib=[1,1]
    cnt+=1
    for k in range(2,n+1):
        cnt+=1
        fib.append(fib[k-1]+fib[k-2])
    return fib[n]

def fiboiterativo(n):#Notemos que es la misma cantidad de operaciones que fiboiter(n)
	fib1,fib2=1,1
    global cnt
    cnt+=1
	for k in range(2,n+1):
		cnt+=1
        fib=fib1+fib2
		fib1=fib2
		fib2=fib
	return fib2

#Hasta 50
maximo=50
rango=range(0,maximo)
cntr,cnti,cntm=[],[],[]
for n in rango:
    cnt=0
    a=fiborec(n)
    cntr.append(cnt)
    cnt=0
    b=fiboiter(n)
    cnti.append(cnt)
    memo,cnt={},0
    c=fibonacci(n)
    cntm.append(cnt)


plt.axis([0,50,0,100])
plt.plot(rango,cnti,label="Iterativo")
plt.plot(rango,cntr,label="Recursivo")
plt.plot(rango,cntm,label="Memoria")
plt.xlabel("Número de fibonacci")
plt.ylabel("Cantidad de operaciones")
plt.title("Sucesión de Fibonacci")
plt.legend()
plt.savefig("fibo4.png")
plt.show()
