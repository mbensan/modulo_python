def countdown(num):
    if num < 0:
        return []
    arr = []

    for i in range(num, -1, -1):
        arr.append(i)
    
    return arr

'''
print(countdown(-2))
print(countdown(5))
print(countdown(8))
'''

def mayores_segundo(lista):
    if len(lista) < 2:
        return
    
    segundo = lista[1]
    filtrados = []

    for elem in lista:
        if elem > segundo:
            filtrados.append(elem)
    
    print(len(filtrados))

    return filtrados


def mayores_segundo2(lista):
    filtra2 = lista.filter(lambda x: x > lista[1])
    print(len(filtra2))
    return filtra2

