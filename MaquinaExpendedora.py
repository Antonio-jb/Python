"""
Maquina de bebidas:
Agua - 0.50€
Refresco - 0.75€
Zumo - 0.95€

El programa emitira un menú que mostrara productos y precios ademas de la opción de salir.
Pedira la opción elegida y pedira monedas al usuario.

La maquina acepta todas las monedas de euro, de 2€ a 5cents.

Al comienzo del día, la maquina dispone de 20 monedas de todas las cantidades necesarias para el cambio.

Se debe dar el cambio correcto con el menor numero posible de monedas.
La maquina mostrara un mensaje de "Introduzca el importe exacto" en caso de no tener dos tipos de monedas cualesquiera
o si una de las ausentes en la pila de 5cts. Sólo aceptará el importe exacto en este caso.

Al final del programa nos debe dar el total del dinero disponible en la maquina. por unidad monetaria.
"""

monedas = [2, 1, 0.50, 0.20, 0.10, 0.05]
cantidadMonedas = [20, 20, 20, 20, 20, 20]

nombreProductos = ["Agua 💧", "Refresco 🥤", "Zumo 🥃"]
precioProductos = [0.50, 0.75, 0.95]


def printMenu(nombres, precios):
    if len(nombres) != len(precios):
        return False

    textoMenu = "¡Bienvenido! Seleccione un producto: \n"
    for i in range(len(nombres)):
        textoMenu += f"{i + 1} - {nombres[i]} : {precios[i]}€\n"
    textoMenu += f"{len(nombres) + 1} - Salir"
    print(textoMenu)

def elegirProducto(productos):
    opcion = input("Elija una opción => ")
    numerosProductos = []
    for i in range(len(productos)):
        numerosProductos.append(str(i + 1))

    numerosProductos.append(str(len(productos) + 1))

    while opcion not in numerosProductos:
        opcion = input("Elija una opcion correcta => ")

    if opcion == str(len(productos) + 1):
        return None

    return int(opcion) - 1

def ingresarMoneda():
    print("Monedas disponibles: 2€, 1€, 0.50€, 0.20€, 0.10€, 0.05€")
    moneda = float(input("Introduce la moneda: "))

    while moneda not in monedas:
        print("Valor no válido. Por favor, introduce una moneda válida.")
        moneda = float(input("Introduce la moneda: "))

    return moneda

def ingresarImporte(opcion):
    precio = precioProductos[opcion]
    importeUsuario = 0
    monedasIntroducidas = []

    while importeUsuario < precio:
        print(f"Le queda {round(precio - importeUsuario, 2)}€ por ingresar.")
        moneda = ingresarMoneda()
        importeUsuario += moneda
        monedasIntroducidas.append(moneda)

    if importeUsuario > precio:
        resto = round(importeUsuario - precio, 2)
        print(f"Su cambio es {resto}€")
        devolverCambio(resto)

    for moneda in monedasIntroducidas:
        cantidadMonedas[monedas.index(moneda)] += 1

    print(f"Aquí tiene su {nombreProductos[opcion]}")


def devolverCambio(cambio):
    print(f"Devolviendo el cambio: {cambio}€")
    for i in range(len(monedas) - 1, -1, -1):
        while cambio >= monedas[i] and cantidadMonedas[i] > 0:
            cantidadMonedas[i] -= 1
            cambio = round(cambio - monedas[i], 2)
            print(f"Se ha devuelto una moneda de {monedas[i]}€")
        if cambio == 0:
            break
    if cambio > 1:
        print("No es posible devolver el cambio exacto con las monedas disponibles.")
        print("Introduzca el importe exacto.")
    else:
        print("Cambio devuelto correctamente.")

def mostrarTotalDinero():
    totalDinero = 0
    print("\nTotal de dinero disponible en la máquina:")
    for i in range(len(monedas)):
        totalDinero += cantidadMonedas[i] * monedas[i]
        print(f"{monedas[i]}€: {cantidadMonedas[i]} monedas")

    print(f"Total en la máquina: {round(totalDinero, 2)}€")

def ejecutarMaquina():
    while True:
        printMenu(nombreProductos, precioProductos)
        opcion = elegirProducto(nombreProductos)

        if opcion is None:
            mostrarTotalDinero()
            print("\n¡Gracias por su visita.!")
            break
        else:
            ingresarImporte(opcion)

ejecutarMaquina()
