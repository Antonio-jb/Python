import json

import pandas as pd
import openpyxl

animalId = []
animalType = []
animalArrivalDate = []
animalName = []

def loadJSON():
    try:
        with open ("animales.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

animalesCall = loadJSON()
animales = animalesCall["animals"]

cont = 1
for animal in animales:
    animalId.append(cont)
    animalType.append(animal["especie"])
    animalArrivalDate.append(animal["fecha_llegada"])
    animalName.append(animal["nombre"])

df = pd.DataFrame(
    {
        "Número": animalId,
        "Nombre": animalName,
        "Especie": animalType,
        "Fecha de Llegada": animalArrivalDate
    }
)

print(df)
# df.sort_values(by="Especie")
# print(df)

df.to_excel('animalicos.xlsx')
