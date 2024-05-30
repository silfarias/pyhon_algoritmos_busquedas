import time
import psutil

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

# ejemplos de listas para las pruebas
listas_prueba = [
    (list(range(100000001)),9999999),
    (sorted([34, 23, 5, 78, 2, 13, 42, 79, 56, 43, 66, 21, 33, 98, 0, 4]), 66) # odenamos la lista
]

def medir_tiempo_recursos():
    for lista, valor in listas_prueba:
        proceso = psutil.Process()  # creamos una instancia de Process una sola vez
        memoria_inicial = proceso.memory_info().rss / (1024 * 1024) # calculamos la memoria inicial en MB antes de la ejecución

        inicio = time.time()
        resultado = busq_binaria(lista, valor)
        fin = time.time()

        memoria_final = proceso.memory_info().rss / (1024 * 1024)

        tiempo = fin - inicio
        uso_memoria = memoria_final - memoria_inicial

        print(f"En la lista de tamaño {len(lista)}: el resultado es {resultado}")
        print(f"Su tiempo de ejecución es de {tiempo} segundos")
        print(f"Uso de memoria: {uso_memoria} MB")

medir_tiempo_recursos()