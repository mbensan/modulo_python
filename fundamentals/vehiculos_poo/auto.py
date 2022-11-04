from vehiculo import Vehiculo

# métodos de clase
# @classmethod
# def presentarse(clase, nueva_descr):
#     clase.descr = nueva_descr
#     print(clase.descr)
# atributo de clase
# descr = 'Esto es un vehículo'


class Auto(Vehiculo):

    def __init__(self, marca, modelo, rend: int, asientos=5):
        # primero llamo al constructor de la clase madre
        super().__init__(marca, modelo, rend)
        # super(TPublico, self).__init__(10)
        # atributos específicos de la clase hija
        self.asientos = asientos
    
    def peaje(self):
        return 6

    
# desde acá hacia abajo es para testing
# deseo ejecutarlo sólo si estoy ejecutando directamente ESTE archivo
if __name__ == '__main__':
    spark = Auto('Chevrolet', 'Spark', 13, 4)
    lr = Auto('Landrover', 'Freelander', 6, 5)
    auris = Auto('Toyota', 'Auris', 12)

    print(auris.marca)

    auris.viajar(200)


