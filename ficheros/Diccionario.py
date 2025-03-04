import json

diccionarioConListas = {}

# Cargar el contenido existente del archivo
try:
    with open("diccionario.json", "r") as file:
        diccionarioConListas = json.load(file)
except FileNotFoundError:

    # Si el archivo no existe, se crea un nuevo diccionario
    diccionarioConListas = {}

# Añadir nuevas palabras y sus definiciones
palabraNueva = input("Introduzca una palabra nueva o escriba 'exit'\n").lower()
while palabraNueva != "exit":
    definicion = input("Introduzca su definición:\n")
    if palabraNueva in diccionarioConListas:
        diccionarioConListas[palabraNueva].append(definicion)
    else:
        diccionarioConListas[palabraNueva] = [definicion]
    palabraNueva = input("Introduzca una palabra nueva o escriba 'exit'\n").lower()

# Guardar el diccionario actualizado en el archivo
with open("diccionario.json", "w") as file:
    json.dump(diccionarioConListas, file, indent=4)

# Buscar una palabra en el diccionario
busqueda = input("¿Qué palabra quiere buscar?\n").lower()
if busqueda in diccionarioConListas:
    cont = 1
    for acepcion in diccionarioConListas[busqueda]:
        print(f"{cont}: {acepcion}")
        cont += 1
else:
    print("No está en el diccionario.")
