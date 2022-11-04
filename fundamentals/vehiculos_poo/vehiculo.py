class TPublico:

    def __init__(self, tarifa):
        self.tarifa = tarifa


class Vehiculo:

    def __init__(self, marca, modelo, rend: int):
        # atributos de los objetos
        self.marca = marca
        self.modelo = modelo
        self.rendimiento = rend

    # métodos
    def conducir(self, kms):
        return kms / self.rendimiento
    
    def viajar(self, kms):
        litros = self.conducir(kms)
        print(f"El auto gastó {litros} litros de combustible")

    def peaje(self):
        raise NotImplementedError('No sé cuanto pagar')

