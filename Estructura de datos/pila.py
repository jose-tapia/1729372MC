
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


pila=Pila()
pila.meter(4)
pila.meter('a')
pila.meter("hola")
print(pila.longitud)
print(pila.obtener())
print(pila.obtener())
print(pila.obtener())
print(pila.longitud)
# 3
# hola
# a
# 4
# 0
