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
    x=np.linspace(1,50000)
    plt.plot(x,x**(0.5),label="Raíz de n",color="green")
    plt.plot(xs,ys, label=titulo)
    plt.xlabel("Número")
    plt.ylabel("Cantidad de operaciones")
    plt.title(titulo) 
    plt.legend()
    plt.savefig(imagen)
    plt.show()

def graficar1(xs,ys,imagen,titulo):
    x=np.linspace(50001,100000)
    plt.plot(x,x**(0.5),label="Raíz de n",color="green")
    plt.plot(xs,ys, label=titulo)
    plt.xlabel("Número")
    plt.ylabel("Cantidad de operaciones")
    plt.title(titulo) 
    plt.legend()
    plt.savefig(imagen)
    plt.show()

cnt=251



G2xs=range(1,50001,cnt)
G2ys=[esPrimo(x) for x in G2xs]

G3xs=range(50000,100001,cnt)
G3ys=[esPrimo(x) for x in G3xs]


graficar(G2xs,G2ys,"Numeros1al50000.png","Complejidad por número")
graficar1(G3xs,G3ys,"Numeros50000al100000.png","Complejidad por número")