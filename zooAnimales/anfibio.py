from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        self._listado.append(self)
    #SET Y GET
    def getNombre(self):
        return super().getNombre()
    def getEdad(self):
        return super().getEdad()
    def getHabitat(self):
        return super().getHabitat()
    def getColorPiel(self):
        return self._colorPiel
    def isVenenoso(self):
        return self._venenoso
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    @classmethod
    def crearRana(cls, name, age, gen):
        cls.ranas += 1
        return Anfibio(name, age, "selva", gen, "rojo", True)
    @classmethod
    def crearSalamandra(cls, name, age, gen):
        cls.salamandras += 1
        return Anfibio(name, age, "selva", gen, "negro y amarillo", False)
