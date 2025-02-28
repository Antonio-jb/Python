"""
Mostrar el siguiente menú para que el usuario decida:
1. Calcular si el número que le pasas es primo.
2. Calcular si el número que le pasas es par.
3. Calcular si el número (año) que le pasas es bisiesto.
"""

seguir = True

def numPrimo():
    numero = int(input(f"Introduzca número deseado: \n"))
    for n in range (2, numero):
        if numero % n == 0:
            print(f"No es primo", n, "Es divisor.\n")
            return False
        print(f"El número {numero} si es primo.\n")
        return True

def numPar():
    numero = int(input(f"Introduzca número deseado: \n"))
    for n in range (2, numero):
        n = 2
        if numero % n > 0:
            print(f"El número {numero} no es par.\n")
            return False
        print(f"El número {numero} si es par.\n")
        return True

def anoBisiesto():
    numero = int(input(f"Introduzca año deseado: \n"))
    if (numero % 4 == 0 and numero % 100 != 0) or (numero % 400 == 0):
        print(f"El año {numero} si es bisiesto.\n")
        return True
    print(f"El año {numero} no es bisiesto.\n")
    return False

while seguir:

    print(f"Escoja una de las opciones de este menu:\n")
    print(f"a) Calcular si el numero es primo.")
    print(f"b) Calcular si el numero es par.")
    print(f"c) Calcular si el numero (año) es bisiesto.")
    print(f"d) Salir.\n")
    opcion = input(f"Introduzca opcion deseada (a/b/c/d): ").lower()

    if opcion == "a":
        numPrimo()
    if opcion == "b":
        numPar()
    if opcion == "c":
        anoBisiesto()
    if opcion == "d":
        seguir = False
        print(f"Operación terminada exitosamente.")
