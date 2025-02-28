from matrices.matrices_utils import printMatrix

"""

Haz una matriz de 10X10 de nombre tabla.
carga la matriz de manera que las filas pares se rellenen con un 1
y las impares con un 0.
Iniciar la matriz y muestra su contenido en pantalla

"""

"""
lista = [1,2,3]
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
"""

tabla = []

for i in range(10):
    tabla.append([])
    for j in range(10):
        if i % 2 == 0:
            tabla[i].append(0)
        else:
            tabla[i].append(1)


for fila in tabla:
    print(fila)

