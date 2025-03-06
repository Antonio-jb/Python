import json
import os

#Leer el contenido de una carpeta diferenciando entre ficheros y directorios
nombre_carpeta = 'directorio_ejercicio1'

contenido = os.listdir(nombre_carpeta)

for elemento in contenido:
    print(os.path.join(nombre_carpeta, elemento))

def leerFichero(nombre):
    try:
        with open(nombre, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

lectura = leerFichero("receta.json")

print(lectura)

def crearFichero():
    try:
        with open("../directorio_ejercicio1/fichero_ejemplo1.json", "x") as file:
            return json.load(file)
    except FileExistsError:
        with open("../directorio_ejercicio1/fichero_ejemplo1.json", "r") as file:
            return json.load(file)

creacion = crearFichero()
print("Creando fichero nuevo...")

diccionarioConListas = {
    "nobuk": ["m. Piel curtida de vaca con aspecto aterciopelado."],
    "curtido": ["adj. experimentado", "adj. El Salv. renegrido (II de color negruzco)."],
    "legumbre": ["f. Fruto o semilla que se cria ne vainas."]
}
#
# print(diccionario["curtido"][1])

