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

valoresMonedas = [2, 1, 0.50, 0.20, 0.10, 0.05]
reservaMonedas = [20, 20, 20, 20, 20]

nombreProductos = ["Agua 💧","Refresco 🥤","Zumo 🥃"]
precioProductos = [0.50, 0.75, 0.95]


def printMenu(nombres, precios):
    if len(nombres) != len(precios):
        return False

    textoMenu = "Bienvenido \n"
    for i in range(len(nombres)):
        textoMenu += f"{i + 1} - {nombres[i]} : {precios[i]}\n"
    textoMenu += f"{len(nombres) + 1} - Salir"
    print(textoMenu)


def elegirProducto(productos):
    opcion = input("Elija una opción => ")
    numerosProductos = []
    for i in range(len(productos)):
        numerosProductos.append(str(i + 1))

    while opcion not in numerosProductos:
        opcion = input("Elija una opcion correcta => ")
    return int(opcion) - 1


def ingresarImporte(opcion):
    precio = precioProductos(opcion)
    importeUsuario = 0
    monedasIntroducidas = []
    while importeUsuario < precio:
        print(f"Le queda {round(precio - importeUsuario, 2)} por ingresar.")
        moneda = ingresarMoneda()
        importeUsuario += moneda
        monedasIntroducidas.append(moneda)
    if importeUsuario > precio:
        resto = importeUsuario - precio

        entregarProducto(nombreProductos[opcion])
        sumarMonedas(monedasIntroducidas)


def entregarProducto(nombre):
    print(f"Aqui tiene su {nombre}")


def sumarMonedas(monedas):
    for moneda in monedas:
        reservaMonedas[valoresMonedas.index(moneda)]


def ingresarMoneda():
    valoresValidos = []


printMenu(nombreProductos, precioProductos)
opcion = elegirProducto(nombreProductos)
if opcion == len(nombreProductos) + 1:
    print("Gracias por venir")
else:
    ingresarImporte(opcion)