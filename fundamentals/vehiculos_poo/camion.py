from vehiculo import Vehiculo


class Camion(Vehiculo):

    def __init__(self, marca, modelo, rend: int, carga):
        # primero llamo al constructor de la clase madre
        super().__init__(marca, modelo, rend)
        # atributos específicos de la clase hija
        self.carga = carga
    
    # métodos
    def tarar(self, kgs):
        if kgs > self.carga:
            return False
        else:
            return True
    
    def peaje(self):
        return 15


class Acoplado(Camion):
    def __init__(self, marca, modelo, rend: int, carga):
        # primero llamo al constructor de la clase madre
        super().__init__(marca, modelo, rend, carga)

prin = Acoplado('Volvo', 'SuperMax 3600', 1, 20000)