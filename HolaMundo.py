#print ("Hola Mundo.")
#str()
#int()
#float()
#variable = 3
#otraVariable = "Saludos"
#numeroUsuario = int(input("Mete un número: "))
#print(len(otraVariable))
#lista = [1,2,3,"a",otraVariable,numeroUsuario]

#2 == 2
#2 != 2
#2 >= 2
#2 < 2
#2 == 2 and 1 == 3
#not (2 != 2 or 1 == 1)
#print("a" in "aeiou")
#if "a" not in "aeiou":
#    print("No hay A")

esCierto = False

while not esCierto:
    print("aaa")
    esCierto = True

for i in range(1, 8, 2):
    print(i)

lista = ["Antonio", "Emily", "Adrian", "Javier", "Alvaro"]
for i in range(len(lista)):
    print(lista[i])

lista = ["Antonio", "Emily", "Adrian", "Javier", "Alvaro"]
for alumno in lista:
    for letra in alumno:
     print(letra)

def tieneA(nombre):
    if "a" in nombre.lower():
        return True
    return False

lista = ["Antonio", "Emily", "Adrian", "Javier", "Alvaro"]
for alumno in lista:
    if tieneA(alumno):
     print(f"{alumno.capitalize()} contiene la leta a.")