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

print(G.dijkstra(1))
print(G.dijkstra(2))
print(G.dijkstra(3))
print(G.dijkstra(4))
