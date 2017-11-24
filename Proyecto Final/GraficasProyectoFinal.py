import matplotlib.pyplot as plt
import numpy as np 

def esPrimo(n):
    cnt=0
    if n<=1:
        return cnt
    m=2
    while m<n:
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
    plt.plot(xs,ys, label=titulo)
    plt.xlabel("Número")
    plt.ylabel("Cantidad de operaciones")
    plt.title(titulo) 
    plt.legend()
    plt.savefig(imagen)
    plt.show()

esprimo=[esPrimo(x) for x in range(100001)]
itsprime=[itsPrime(x) for x in range(100001)]


cnt=251

G1xs=range(1,100001,cnt)
G1ys=[esprimo[x] for x in G1xs]

G2xs=range(1,50001,cnt)
G2ys=[esprimo[x] for x in G2xs]

G3xs=range(50000,100001,cnt)
G3ys=[esprimo[x] for x in G3xs]

G4xs=[x for x in range(1,100001,cnt) if x%2==0]
G4ys=[esprimo[x] for x in G4xs]

G5xs=[x for x in range(1,100001,cnt) if x%2==1 if not itsprime[x]]
G5ys=[esprimo[x] for x in G5xs]

G6xs=[x for x in range(1,100001,cnt) if itsprime[x]]
G6ys=[esprimo[x] for x in G6xs]

graficar(G1xs,G1ys,"1Numeros1al100000.png","Complejidad por número")
graficar(G2xs,G2ys,"1Numeros1al50000.png","Complejidad por número")
graficar(G3xs,G3ys,"1Numeros50000al100000.png","Complejidad por número")
graficar(G4xs,G4ys,"1NumerosPares.png","Complejidad por número par")
graficar(G5xs,G5ys,"1NumerosImpares.png","Complejidad por número impar")
graficar(G6xs,G6ys,"1NumerosPrimos.png","Complejidad por número primo")

cnt=1

G1xs=range(1,100001,cnt)
G1ys=[esprimo[x] for x in G1xs]

G2xs=range(1,50001,cnt)
G2ys=[esprimo[x] for x in G2xs]

G3xs=range(50000,100001,cnt)
G3ys=[esprimo[x] for x in G3xs]

G4xs=[x for x in range(1,100001,cnt) if x%2==0]
G4ys=[esprimo[x] for x in G4xs]

G5xs=[x for x in range(1,100001,cnt) if x%2==1 if not itsprime[x]]
G5ys=[esprimo[x] for x in G5xs]

G6xs=[x for x in range(1,100001,cnt) if itsprime[x]]
G6ys=[esprimo[x] for x in G6xs]

graficar(G1xs,G1ys,"2Numeros1al100000.png","Complejidad por número")
graficar(G2xs,G2ys,"2Numeros1al50000.png","Complejidad por número")
graficar(G3xs,G3ys,"2Numeros50000al100000.png","Complejidad por número")
graficar(G4xs,G4ys,"2NumerosPares.png","Complejidad por número par")
graficar(G5xs,G5ys,"2NumerosImpares.png","Complejidad por número impar")
graficar(G6xs,G6ys,"2NumerosPrimos.png","Complejidad por número primo")
