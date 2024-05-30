import time

#La busqueda binaria consiste en dividir repetidamente un lista ordenada 
#en subconjuntos mas pequeños, reduciendo asi el tiempo de busqueda
def busq_binaria(lista, valor):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            final = medio - 1
    return -1