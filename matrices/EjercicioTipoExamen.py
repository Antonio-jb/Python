"""

Hacer una matriz cuadrada de longitud >5 y <25

"""

matriz = []

for i in range(5):
    matriz.append([])
    for j in range(5):
        if i % 2 == 0:
            matriz[i].append(0)
        else:
            matriz[i].append(1)

for fila in matriz:
    print(fila)

listaFibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                  144, 233, 377, 610, 987, 1597, 2584, 4181,
                  6765, 10946, 17711, 28657, 46368]

matrizDos = []
print("-----------------------------------------------")

for i in range(8):
    matrizDos.append([])
    for j in range(8):
        if i == j and i < len(listaFibonacci):
            matrizDos[i].append(listaFibonacci[i])
        else:
            matrizDos[i].append(0)

for filaDos in matrizDos:
    print(filaDos)


print("-----------------------------------------------")
matrizInversa = []
print(f"Introduzca el tamaño de la matriz cuadrada: (min: 5 & max: 25)")

def fibonacci(n):
    fibonacciLista = []
    a, b = 0, 1
    while len(fibonacciLista) < n:
        fibonacciLista.append(a)
        a, b = b, a + b
    return fibonacciLista

bucle = True
while bucle:
    try:
        longitud = int(input("Tamaño: "))
        if 5 <= longitud <= 25:
            bucle = False
        else:
            print(f"Por favor introduzca un número válido.")
    except ValueError:
        print("Hubo un error al introducir el tamaño. Por favor, inténtelo de nuevo.")
        print("Recuerda que solo se adimten números -> min: 5 & max: 25")

fibonacciLista = fibonacci(longitud)

for i in range(longitud):
    matrizInversa.append([])
    for j in range(longitud):
        if i + j == longitud - 1:
            matrizInversa[i].append(fibonacciLista[i])
        else:
            matrizInversa[i].append(0)

for filaDos in matrizInversa:
    print(filaDos)
