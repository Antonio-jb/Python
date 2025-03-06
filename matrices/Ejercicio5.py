"""
Diseñar programa Java, que:
a) Crea una tabla bidimensional de longitud 5x5 y nombre 'matriz'.
b) Carga la tabla con valores numéricos enteros.
c) Suma todos los elementos de cada fila y todos los elementos de cada columna
visualizando los resultados en pantalla.
"""

# Crear una matriz 5x5
matriz = []

# Cargar valores en la matriz
print("Introduce los valores de la matriz 5x5 (uno por uno):")
for i in range(5):
    fila = []
    for j in range(5):
        valor = int(input(f"Introduce el valor para la posición ({i+1}, {j+1}): "))
        fila.append(valor)
    matriz.append(fila)

# Imprimir la matriz cargada
print("\nMatriz:")
for fila in matriz:
    print(fila)

# Sumar filas y columnas
print("\nSuma de filas y columnas:")
for i in range(5):
    suma_fila = sum(matriz[i])  # Suma de una fila
    suma_columna = sum(matriz[j][i] for j in range(5))  # Suma de una columna
    print(f"Suma de la fila {i+1}: {suma_fila}")
    print(f"Suma de la columna {i+1}: {suma_columna}")
