def divide_elementos_de_lista(lista, divisor):

    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = 5
divisor = 'platzi'

print('123'+'456')