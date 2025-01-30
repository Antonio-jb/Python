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