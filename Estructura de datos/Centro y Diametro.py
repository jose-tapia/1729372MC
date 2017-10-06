class Pila(object):
    def __init__(self):
        self.a=[]
    def obtener(self):
        return self.a.pop()
    def meter(self, e):
        self.a.append(e)
        return len(self.a)
    @property
    def longitud(self):
        return len(self.a)
    
class Cola(Pila):
    def obtener(self):
        return self.a.pop(0)
        


class Grafo():
    def __init__(self):
        self.V=set()
        self.E=dict()
        self.vecinos=dict()
        
    def agrega(self,v):
        self.V.add(v)
        if not v in self.vecinos:
            self.vecinos[v]=set()
        
    def conecta(self,v,u,peso=1):
        self.agrega(u)
        self.agrega(v)
        self.E[(u,v)]=self.E[(v,u)]=peso
        self.vecinos[u].add(v)
        self.vecinos[v].add(u)
        
    def complemento(self):
        comp=Grafo()
        for u in self.V:
            for v in self.V:
                if u!=v and (u,v) not in self.E:
                    comp.conecta(u,v,1)
        return comp
        
        
def BFS(graph, ini):
    vis=[ini]
    bsq=Cola()
    bsq.meter(ini)
    while bsq.longitud>0:
        act=bsq.obtener()
        for w in graph.vecinos[act]:
            if w not in vis:
                vis.append(w)
                bsq.meter(w)
    return vis
    
    
def DFS(graph, ini):
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











    
def zip(a,b):
    return [(a[i],b[i]) for i in range(min(len(a),len(b)))]
    
    
    
def superBFS(graph,ini):
    vis =[ini]
    dist=[0]
    bsq=Cola()
    bsq.meter((ini,0))
    while bsq.longitud>0:
        (act,d)=bsq.obtener()
        vecinos=graph.vecinos[act]
        for w in vecinos:
            if w not in vis:
                vis.append(w)
                dist.append(d+1)
                bsq.meter((w,d+1))
    return zip(vis,dist)
    
    
    
    
def diametro(graph):
    maxdist,bestni,bestnf=-1,0,0
    for v in graph.V:
        resbfs=superBFS(graph,v) 
        (fin,dist)=resbfs[-1]
        if dist>maxdist:
            maxdist=dist
            bestni=v
            bestnf=fin
    return [maxdist,bestni,bestnf]
    
    
def centro(graph):
    mindist,bestni,bestnf=100000000,0,0
    for v in graph.V:
        resbfs=superBFS(graph,v) 
        (fin,dist)=resbfs[-1]
        if dist<mindist:
            mindist=dist
            bestni=v
    return [mindist,bestni]
    
    

    
    
    
    
    
    



G=Grafo()
G.conecta(1,2)
G.conecta(2,3)
G.conecta(3,4)
G.conecta(3,6)
G.conecta(4,5)
G.conecta(4,7)
G.conecta(5,8)



print(BFS(G,1))
print(DFS(G,1))
print(diametro(G))
print(centro(G))
