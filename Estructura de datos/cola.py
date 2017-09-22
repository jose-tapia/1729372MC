
class Cola(object):
    def __init__(self):
        self.a=[]
    def obtener(self):
        return self.a.pop(0)
    def meter(self,e):
        self.a.append(e)
        return len(self.a)
    @property
    def longitud(self):
        return len(self.a)


cola=Cola()
cola.meter(4)
cola.meter('a')
cola.meter("hola")
print(cola.longitud)
print(cola.obtener())
print(cola.obtener())
print(cola.obtener())
print(cola.longitud)
