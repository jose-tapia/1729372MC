import matplotlib.pyplot as plt
import numpy as np 

def esPrimo(n):
    cnt=0
    if n<=1:
        return cnt
    m=2
    while m*m<=n:
        cnt+=1
        if n%m==0:
            return cnt
        m+=1
    return cnt

def itsPrime(n):
    if n<=1:
        return False
    m=2
    while m*m<=n:
        if n%m==0:
            return False
        m+=1
    return True

def graficar(xs,ys,imagen,titulo):
    x=np.linspace(1,100000)
    plt.plot(x,x**(0.5),label="Raíz de n",color="green")
    plt.plot(xs,ys, label=titulo)
    plt.xlabel("Número")
    plt.ylabel("Cantidad de operaciones")
    plt.title(titulo) 
    plt.legend()
    plt.savefig(imagen)
    plt.show()

cnt=251



G5xs=[x for x in range(1,100001,cnt) if x%2==1]
G5ys=[esPrimo(x) for x in G5xs]

graficar(G5xs,G5ys,"NumerosImparesconPrimos.png","Complejidad por número impar")
