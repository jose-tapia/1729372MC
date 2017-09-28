class Pila(object):
    def __init__(self):
        self.a=[]
    def obtener(self):
        return self.a.pop()
    def meter(self,e):
        self.a.append(e)
        return len(self.a)
    @property
    def longitud(self):
        return len(self.a)

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

def DFS(graph,ini):
    vis=[]
    bsq=Pila()
    bsq.meter(ini)
    while bsq.longitud>0:
        act=bsq.obtener()
        if act in vis:
            continue
        vis.append(act)
        vecinos=graph.vecinos[act]
        for w in vecinos:
            if w not in vis:
                bsq.meter(w)
    return vis

graph=Grafo()
graph.conecta(1,2)
graph.conecta(2,3)
graph.conecta(3,4)
graph.conecta(4,5)
graph.conecta(1,6)
graph.conecta(6,7)
graph.conecta(7,8)
graph.conecta(8,9)
print(DFS(graph,1))
            
