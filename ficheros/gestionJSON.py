import json
import hashlib

def cargarJSON(nombre):
    try:
        with open(nombre, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardarJSON(nombre, datos):
    with open(nombre, "w") as file:
        json.dump(datos, file, cargarJSON())


receta = cargarJSON("receta.json")
receta["dificultad"] = "media"
guardarJSON("receta.json", receta)
print(receta)
