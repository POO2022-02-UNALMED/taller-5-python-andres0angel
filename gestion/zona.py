from zooAnimales.animal import Animal
class Zona():
    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
    def getNombre(self):
        return self._nombre
    def getZoo(self):
        return self._zoo
    def setNombre(self, name):
        self._nombre = name
    def setZoo(self, nuevoZoologico):
        self._zoo = nuevoZoologico


    def agregarAnimales(self, anim):
        if isinstance(anim, Animal):
            self._animales.append(anim)

    def cantidadAnimales(self):
        return len(self._animales)


