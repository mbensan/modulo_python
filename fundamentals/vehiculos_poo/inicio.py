from auto import Auto
from moto import Moto
from camion import Camion

if __name__ == '__main__':

    licencias = []

    while True:

        respuesta = input('''¿Qué vehículo desea crear?
            1. Auto
            2. Moto
            3. Camión
            0. Salir\n''')
        
        if respuesta == '1':
            new = Auto('Mazda', 'M3', 10)
            licencias.append(new)
        elif respuesta == '2':
            moto = Moto('Honda', 'ZX300', 20)
            licencias.append(moto)

        elif respuesta == '3':
            cam = Camion('Volvo', 'TRD 20', 3, 12000)
            licencias.append(cam)
        
        elif respuesta == '0':
            print('Nos vemos!')
            break
        else:
            print('Esa opción no existe')
    
    for veh in licencias:
        mensaje = f"Por el {veh.__class__.__name__} debe pagar US${veh.peaje()}"
        print(mensaje)

