"""
Crear una tabla de dos dimensiones, cuyo contenido serán las potencias de 2. La
primera columna de la tabla nos indicara el exponente (positivo o negativo) y la
segunda columna su valor.

El tamaño de la tabla será 20x2.
Se pedirá que el usuario introduzca los valores de las potencias que quiere visualizar
hasta que al introducir la potencia se introduzca un -1000.
"""

# Crear tabla de potencias de 2
tabla = []
print("Introduce exponentes para calcular las potencias de 2 (introduce -1000 para salir):")

while True:
    exponente = int(input("Introduce el exponente: "))
    if exponente == -1000:
        break
    valor = 2 ** exponente
    tabla.append((exponente, valor))

# Mostrar la tabla
print("\nTabla de potencias de 2:")
for exponente, valor in tabla:
    print(f"2^{exponente} = {valor}")

