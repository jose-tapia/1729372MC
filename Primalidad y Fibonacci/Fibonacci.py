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
    for k in range(2,n+1):
        cnt+=1
        fib.append(fib[k-1]+fib[k-2])
    return fib[n]


#Hasta 50

archivo = open("datos.txt","w")
archivo.write("Fibo Recursivo Iterativa Memoria\n")
for n in range(0,51):
    cnt=0
    a=fiborec(n)
    cntr,cnt=cnt,0
    b=fiboiter(n)
    cnti,cnt=cnt,0
    memo={}
    c=fibonacci(n)
    cntm,cnt=cnt,0
    archivo.write("%d %d %d %d\n" % (n, cntr, cnti, cntm))
archivo.close()
