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

