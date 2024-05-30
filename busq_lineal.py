import time
import psutil

# Implementación de la búsqueda lineal
def busq_lineal(lista, valor):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            # return f"El valor {valor} se encuentra en la posición {i}"
            return i
    # return f"El valor {valor} no se encuentra en la lista"
    return -1

# Listas para las pruebas
listas_prueba = [
    (list(range(100000001)), 9999999),
    [(34, 23, 5, 78, 2, 13, 42, 79, 56, 43, 66, 21, 33, 98, 0, 4), 66]
]

def medir_tiempo_recursos():
    for lista, valor in listas_prueba:

        # medimos la memoria antes de la ejecución del algoritmo
        memoria_inicial = psutil.Process().memory_info().rss / (1024 * 1024) # devuelve la memoria ocupada ocupada en MB

        inicio = time.time() # tiempo de inicio
        resultado = busq_lineal(lista, valor) # utilizamos la busqueda lineal
        fin = time.time() # tiempo de fin

        # medimos la memoria despues de la ejecución del algoritmo
        memoria_final = psutil.Process().memory_info().rss / (1024 * 1024) # medimos la memoria al finalizar la ejecución

        tiempo = fin - inicio # calculamos el tiempo de ejecución
        uso_memoria = memoria_final - memoria_inicial # calculamos el uso de memoria

        print(f"En la lista de tamaño {len(lista)}: el resultado es {resultado}")
        print(f"Su tiempo de ejecución es de {tiempo} segundos")
        print(f"Uso de memoria: {uso_memoria} MB")


medir_tiempo_recursos()
    
