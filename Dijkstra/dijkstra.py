import random

class Heap(object):
    def __init__(self):
        self.hp=[0]

    def empty(self):
        return len(self.hp)==1

    def top(self):
        if len(self.hp)>1:
            return self.hp[1]
        else:
            return None

    def push(self,x):
        tam=len(self.hp)
        w=tam
        self.hp.append(x)
        while w>0:
            ww=int(w/2)
            if ww>0:
                if self.hp[ww]>self.hp[w]:
                    self.hp[ww],self.hp[w],w=self.hp[w],self.hp[ww],ww
                else:
                    break
            else:
                break

    def pop(self):
        tam=len(self.hp)-1
        self.hp[1],self.hp[tam]=self.hp[tam],self.hp[1]
        tam-=1
        w=1
        while w<=tam:
            i,d=self.hp[w],self.hp[w]
            if 2*w<=tam:
                i=self.hp[2*w]
            if 2*w+1<=tam:
                d=self.hp[2*w+1]
            if self.hp[w]>i or self.hp[w]>d:
                if i<d:
                    self.hp[w],self.hp[2*w]=self.hp[2*w],self.hp[w]
                    w=2*w
                else:
                    self.hp[w],self.hp[2*w+1]=self.hp[2*w+1],self.hp[w]
                    w=2*w+1
            else:
                break
        return self.hp.pop()

def descomponer(w):
    if w==():
        return []
    (x,y)=w
    return descomponer(y)+[x]

class Grafo(object):
    def __init__(self):
        self.vertices=set()
        self.aristas=dict()
        self.vecinos=dict()
    
    def agrega(self,v):
        self.vertices.add(v)
        if not v in self.vecinos:
            self.vecinos[v]=set()
            
    def conecta(self,u,v,peso=1):
        self.agrega(u)
        self.agrega(v)
        self.aristas[(u,v)]=self.aristas[(v,u)]=peso
        self.vecinos[u].add(v)
        self.vecinos[v].add(u)
        
    @property
    def complemento(self):
        comp=Grafo()
        for a in self.vertices:
            for b in self.vertices:
                if a!=b and (a,b) not in self.aristas:
                    comp.conecta(a,b,1)

    def dijkstra(self,ini):
        bsq=Heap()
        bsq.push((0,ini,()))
        visitados=set()
        respuesta=dict()
        while not bsq.empty():
            (dist,nodo,path)=bsq.pop()
            if nodo in visitados:
                continue
            visitados.add(nodo)
            respuesta[nodo]=(dist,descomponer((nodo,path)))
            for w in self.vecinos[nodo]:
                if w in visitados:
                    continue
                d=self.aristas[(nodo,w)]
                bsq.push((d+dist,w,(nodo,path)))
        return respuesta

    def __str__(self):
        nodos="Vertices:\n"
        for w in self.vertices:
            nodos+=" "+str(w)+" "
        vis=set()
        edges="Aristas:\n"
        for w in self.aristas:
            (x,y)=w
            if w in vis:
                continue
            if (y,x) in vis:
                continue
            vis.add(w)
            edges+=" "+str(w)+":\t"+str(self.aristas[w])+"\n"
        return nodos+"\n"+edges


def crearGrafo(n,m):
    G=Grafo()
    for x in range(1,n+1):
        adyacentes=[]
        for k in range(m):
            adyacentes.append((random.randint(x,n),random.randint(1,100)))
        for (u,d) in adyacentes:
            G.conecta(x,u,d)
    return G


def imprimirDijkstra(resultado):
    rans=Heap()
    for w in resultado:
        (dist,path)=resultado[w]
        rans.push((dist,w,path))
    while not rans.empty():
        (dist,w,path)=rans.pop()
        linea=" "+str(w)+":\t"+str(dist)+"\t"+str(path)
        print(linea)
    



G=Grafo()
G.conecta(1,2,7)
G.conecta(1,3,9)
G.conecta(1,6,14)
G.conecta(2,3,10)
G.conecta(2,4,15)
G.conecta(3,4,11)
G.conecta(3,6,2)
G.conecta(4,5,6)
G.conecta(5,6,9)
#print(G)
#imprimirDijkstra(G.dijkstra(1))


G1=Grafo()
G1.conecta(1,4,5)
G1.conecta(1,2,2)
G1.conecta(2,3,14)
G1.conecta(2,4,5)
G1.conecta(2,5,4)
G1.conecta(3,5,34)
G1.conecta(4,5,48)
print(G1)
imprimirDijkstra(G1.dijkstra(1))


G2=Grafo()
G2.conecta('A','B',22)
G2.conecta('A','C',9)
G2.conecta('A','D',12)
G2.conecta('B','C',35)
G2.conecta('B','F',36)
G2.conecta('B','H',34)
G2.conecta('C','D',4)
G2.conecta('C','E',65)
G2.conecta('C','F',42)
G2.conecta('D','I',30)
G2.conecta('E','F',18)
G2.conecta('E','G',23)
G2.conecta('F','G',39)
G2.conecta('F','H',24)
G2.conecta('G','H',25)
G2.conecta('G','I',21)
G2.conecta('H','I',19)
print(G2)
imprimirDijkstra(G2.dijkstra('A'))


G3=Grafo()
G3.conecta('a','b',4)
G3.conecta('a','d',1)
G3.conecta('a','e',2)
G3.conecta('b','c',10)
G3.conecta('b','f',5)
G3.conecta('c','g',8)
G3.conecta('c','k',7)
G3.conecta('d','e',2)
G3.conecta('d','h',14)
G3.conecta('e','f',11)
G3.conecta('e','h',18)
G3.conecta('f','g',6)
G3.conecta('f','i',13)
G3.conecta('g','j',17)
G3.conecta('g','k',9)
G3.conecta('h','i',15)
G3.conecta('i','j',16)
G3.conecta('j','k',12)
print(G3)
imprimirDijkstra(G3.dijkstra('a'))

G4=crearGrafo(15,3)
print(G4)
imprimirDijkstra(G4.dijkstra(1))


G5=crearGrafo(20,3)
print(G5)
imprimirDijkstra(G5.dijkstra(1))

G6=crearGrafo(25,3)
print(G6)
imprimirDijkstra(G6.dijkstra(1))
