# FizzBuzz 
# for (let i=0; i<=100; i++) { .... }
def fizzbuzz (num1=3, num2=5):

    for i in range(1, 100):

        if i % num1 == 0 and i % num2 == 0:
            print('FizzBuzz')
        
        elif i % num1 == 0:
            print('Fizz')
        
        elif i % num2 == 0:
            print('Buzz')
        
        else:
            print(i)

# fizzbuzz(3, 8)

# declaro una lista
curso = ['Kari', 'Tomas', 'Rafa', 'Dorian']

# imprimo el tipo de dato
print(type(curso))

# imprimo el largo de la lista
# print('La lista "curso" es de largo ' + str(len(curso)) )

# le agrego un elemento a la lista
curso.append('Ricardo')


def invertir (texto):
    return texto.split()


def esPalindrome(texto):
    # retorna True si el texto es palindrome
    # False, en caso contrario. Omitan mayusculas y espacios
    normal = texto.lower().replace(' ', '')
    return normal == normal[::-1]

import random
def saludar(nombre="desconocido", veces=5):
    saludos = ['Buenos dias', 'Hola', 'Hi', 'Buenas Tardes', 'Qué tal']

    for i in range(veces):
        saludo = random.choice(saludos)
        print(f'¡{saludo} {nombre}!')

'''
    Esto genera una pausa. Para salir de ella, escribir "c" en la terminal
'''
import pdb
pdb.set_trace()

print('El programa ha finalizado')

'''
Ojo Rojo
Luz Azul
Anita lava la tina
Arepera
'''
