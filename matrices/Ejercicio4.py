"""
Se captura por teclado los valores de una matriz de 4 x 4. Deseamos saber si es una
matriz identidad. Es aquella que en la diagonal posee el valor 1 y en el resto de las
posiciones tiene el valor 0.
"""

# Función para verificar matriz identidad
def es_identidad(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
                return False
    return True

# Captura de matriz 4x4
matriz = []
print("Introduce los valores de la matriz 4x4:")
for i in range(4):
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    matriz.append(fila)

# Verificar si es identidad
if es_identidad(matriz):
    print("La matriz es identidad.")
else:
    print("La matriz NO es identidad.")
