import json

def get_socios():
    archivo = open('db.json', 'r')
    datos = json.load(archivo)
    return datos['socios']

def add_socio(nombre, apellido, id):
    # 1. leo  los socios ya existentes
    socios = get_socios()
    # 2. Le agrego un nuevo diccionario a la lista "socios"
    socios.append({
        'nombre': nombre,
        'apellido': apellido,
        'id': id
    })
    # 3. Abro el arcihvo db.json
    archivo = open('db.json', 'w')
    # 4. Creo un string con el array "socios" dentro de él
    socios_json = json.dumps({
        'socios': socios
    })
    # 5. Sobreescribo el contenido del archivo db.json
    archivo.write(socios_json)

