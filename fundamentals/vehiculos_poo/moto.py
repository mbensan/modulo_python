from vehiculo import Vehiculo


class Moto(Vehiculo):

    def __init__(self, marca, modelo, rend: int):
        # primero llamo al constructor de la clase madre
        super().__init__(marca, modelo, rend)
    
    def peaje(self):
        return 3