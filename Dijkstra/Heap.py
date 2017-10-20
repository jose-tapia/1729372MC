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
        
