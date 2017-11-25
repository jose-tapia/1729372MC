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

G1xs=range(1,100001,cnt)
G1ys=[esPrimo(x) for x in G1xs]

G2xs=range(1,50001,cnt)
G2ys=[esPrimo(x) for x in G2xs]

G3xs=range(50000,100001,cnt)
G3ys=[esPrimo(x) for x in G3xs]

G4xs=[x for x in range(1,100001,cnt) if x%2==0]
G4ys=[esPrimo(x) for x in G4xs]

G5xs=[x for x in range(1,100001,cnt) if x%2==1 if not itsPrime(x)]
G5ys=[esPrimo(x) for x in G5xs]

G6xs=[x for x in range(1,100001,cnt) if itsPrime(x)]
G6ys=[esPrimo(x) for x in G6xs]

graficar(G1xs,G1ys,"Numeros1al100000.png","Complejidad por número")
graficar(G2xs,G2ys,"Numeros1al50000.png","Complejidad por número")
graficar(G3xs,G3ys,"Numeros50000al100000.png","Complejidad por número")
graficar(G4xs,G4ys,"NumerosPares.png","Complejidad por número par")
graficar(G5xs,G5ys,"NumerosImpares.png","Complejidad por número impar")
graficar(G6xs,G6ys,"NumerosPrimos.png","Complejidad por número primo")
