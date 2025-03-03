# Crear un array bidimensional 10x15
filas = 10
columnas = 15
array_bidimensional = []

print("Introduce los valores del array 10x15:")
for i in range(filas):
    fila = [int(input(f"Elemento ({i+1}, {j+1}): ")) for j in range(columnas)]
    array_bidimensional.append(fila)

# Crear un array unidimensional con las sumas de las filas
array_sumas = [sum(fila) for fila in array_bidimensional]

# Visualizar resultado
print("\nSuma de cada fila:")
for i, suma in enumerate(array_sumas):
    print(f"Fila {i+1}: {suma}")
