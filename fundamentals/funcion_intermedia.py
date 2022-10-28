x = [ [5,2,3], [10,8,9] ] 

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [[ {'x': 10, 'y': [2, 1, 20]} ]]

z[0][0]['y'][2] = 30


# Soluciones
# 1.
x[1][0] = 15
# 2.
estudiantes[0]['last_name'] = 'Bryant'
# 3.
directorio_deportes['fútbol'][0] = 'Andrés'


# PREGUNTA 4
def printInfo(dicc):
    for llave, valores in dicc.items():
        num_valores = len(valores)

        print(f"{num_valores} {llave.upper()}")

        for valor in valores:
            print(valor)
        print('')

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

