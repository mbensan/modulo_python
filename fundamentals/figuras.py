from utiles import Utiles

class Cuadrado:

    def __init__(self, arista):
        self.arista = arista
    
    def hacer_plgm(self, altura):
        volumen = self.area() * altura
        print(f"El volumen de este cubo sería {volumen}")
        
    def perimetro(self):
        return self.arista * 4
    
    def area(self):
        return self.arista ** 2

cuad = Cuadrado(4)
cuad.hacer_plgm(8)

varianza = Utiles.variance([5,6,7,2,33,12,87])
print(f'la varianza es {varianza}')

