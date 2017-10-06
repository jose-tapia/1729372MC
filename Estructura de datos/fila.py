
class Fila(object):
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


fila=Fila()
fila.meter(4)
fila.meter('a')
fila.meter("hola")
print(fila.longitud)
print(fila.obtener())
print(fila.obtener())
print(fila.obtener())
print(fila.longitud)
# 3
# 4
# a
# hola
# 0
