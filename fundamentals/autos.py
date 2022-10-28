class Auto:
    # atributo de clase
    descr = 'Esto es un auto'

    def __init__(self, marca, modelo, rend: int, asientos=5):
        # atributos de los objetos
        self.marca = marca
        self.modelo = modelo
        self.rendimiento = rend
        self.asientos = asientos
    
    # métodos
    def conducir(self, kms):
        return kms / self.rendimiento
    
    def viajar(self, kms):
        litros = self.conducir(kms)
        print(f"El auto gastó {litros} litros de combustible")
    
    # métodos de clase
    @classmethod
    def presentarse(clase, nueva_descr):
        clase.descr = nueva_descr
        print(clase.descr)

spark = Auto('Chevrolet', 'Spark', 13, 4)
lr = Auto('Landrover', 'Freelander', 6, 5)
auris = Auto('Toyota', 'Auris', 12)

autos = [spark, lr, auris]

print(auris.marca)
print(auris.descr)
print(Auto.descr)

auris.viajar(200)

import pdb; pdb.set_trace()






