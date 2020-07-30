def aproximacion(numero):
    objetivo = numero
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    respuesta_completa = ''

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        respuesta_completa = print(f'No se encontro la raiz cuadrada de {respuesta} con el metodo de aproximacion.')

    else:
        respuesta_completa = print(f'La raiz cuadrada de {objetivo} es {respuesta}, con el metodo de aproximacion.')
    

    return respuesta_completa

def busqueda_binaria(numero):
    objetivo = numero
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    respuesta_completa = ''

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2

    respuesta_completa = print(f'La raiz cuadrada de {objetivo} es {respuesta}, con el metodo busqueda binaria.')

    return respuesta_completa

def enumeracion(numero):
    objetivo = numero
    respuesta = 0
    respuesta_completa = ''

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        respuesta_completa = print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        respuesta_completa = print(f'{objetivo} no tiene raiz cuadrada')
    
    return respuesta_completa



def seleccion_metodo(opcion, numero):

    respuesta = ''

    if opcion == 1:
        respuesta = aproximacion(numero)
    elif opcion == 2:
        respuesta = busqueda_binaria(numero)
    elif opcion == 3:
        respuesta = enumeracion(numero)
    else:
        respuesta = f'La opcion {opcion} no es valida.'

    return respuesta

print('Sistema de calculo de raiz cuadrada')
print('Ingresa una opcion: ')
print('1 - Aproximacion.')
print('2 - Busqueda binaria. ')
print('3 - Enumeracion.')
opcion = int(input())
print('Ingresa un numero para buscar: ')
numero = int(input())
print(seleccion_metodo(opcion, numero))