# Busqueda Binaria y Lineal en Python

El objetivo de este trabajo es investigar cómo funcionan los algoritmos de busqueda lineal y busqueda binaria en el contexto de Python y comprender los requisitos previos para la aplicación de cada algoritmo.
Luego de buscar ejemplos de implementaciones de estas busquedas, analizamos el código para entender y probamos con diferentes conjuntos de datos. Además comparamos la eficiencia de ambos scripts, mostrando el tiempo de ejecución de cada uno utilizando el módulo `time` y el espacio de memoria que utilizan con la libreria `psutil`

### Busqueda Lineal
Los algoritmos de búsqueda lineal en Python son métodos sencillos pero eficientes para encontrar un elemento específico dentro de una lista. Funcionan recorriendo la lista secuencialmente, comparando cada elemento con el valor objetivo hasta que se encuentra o se llega al final de la lista.

### Busqueda Binaria

Los algoritmos de búsqueda binaria en Python son métodos eficientes para encontrar un elemento específico dentro de una lista ordenada. A diferencia de la búsqueda lineal, que recorre la lista secuencialmente, la búsqueda binaria aprovecha el orden de la lista para dividirla repetidamente en subconjuntos más pequeños, reduciendo el tiempo de búsqueda.


## Requisitos para su uso
- Python 3x
- Biblioteca psutil (puede instalarse mediante pip)

## Instalación
- Clona este repositorio
- Ejecuta el siguiente comando para instalar la dependencia

```bash
pip install psutil
```

## Ejecución
Para probar el algoritmo de busqueda lineal ejecuta:
```bash
python busq_lineal.py
```

Para el algoritmo de busqueda binaria ejecuta:
```bash
python busq_binaria.py
```





