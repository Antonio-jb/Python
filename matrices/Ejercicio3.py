"""
Visualizar la matriz transpuesta de la anterior. Si la matriz es cuadrada (tiene igual
número de filas y de columnas) visualice también los elementos de la diagonal
principal.
"""

# Matriz inicial
matriz = [
    [3, 2, 5, 0, 9],
    [9, 10, 2, 3, 1],
    [-3, 2, 3, 43, 1]
]

# Transponer la matriz
transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

print("Matriz Transpuesta:")
for fila in transpuesta:
    print(fila)

# Si es cuadrada, imprimir diagonal principal
if len(matriz) == len(matriz[0]):
    diagonal_principal = [matriz[i][i] for i in range(len(matriz))]
    print("\nDiagonal Principal:", diagonal_principal)
else:
    print("\nLa matriz no es cuadrada.")
