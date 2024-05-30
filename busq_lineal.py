import time
import random

# Implementación de la búsqueda lineal
def busq_lineal(lista, valor):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return f"El valor {valor} se encuentra en la posición {i}"
    return f"El valor {valor} no se encuentra en la lista"

# Función para probar la búsqueda lineal con diferentes conjuntos de datos y valores
def probar_busqueda():
    # Lista de conjuntos de datos y valores a buscar
    datasets = [
        ([5, 23, 67, 12, 65, 48, 96, 5, 31, 56], 5),
        ([4, 23, 67, 12, 65], 12),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
    ]

    resultados = []

    for dataset, valor in datasets:
        inicio = time.time()
        resultado = busq_lineal(dataset, valor)
        fin = time.time()
        tiempo = fin - inicio
        resultados.append((dataset, valor, resultado, tiempo))

    # Mostrar los resultados
    for dataset, valor, resultado, tiempo in resultados:
        print(f"Dataset: {dataset[:10]}... (tamaño: {len(dataset)}), Valor: {valor}, Resultado: {resultado}, Tiempo: {tiempo:.6f} segundos")

# Ejecutar las pruebas
probar_busqueda()