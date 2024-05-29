import time

# La busqueda lineal consiste en recorrer una lista secuencialmente comparando 
#cada elemento con el valor objetivo hasta encontrarlo o llegar al final de la lista
def busq_lineal(lista, valor):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return f"El valor {valor} se encuentra en la posición {i}"
    return f"El valor {valor} no se encuentra en la lista"
    

lista = [34, 23, 2, 5, 7, 3, 67, 0]
obj = 23
busqueda = busq_lineal(lista, obj)
print(busqueda)


def medir_ejecucion():
    