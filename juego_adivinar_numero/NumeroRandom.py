import random as r

numero = (r.randint(1, 100))
correcto = False

# Juego en el que la maquina cree un número aleatorio de 1 al 100
# y el jugador intente adivinar hasta que lo consigue
# la maquina da pistas (mas alto o mas bajo)

def introNumero():
    return int(input("Ingresa el número que crees que será: "))

adivina = introNumero()

while not correcto:
    if adivina > numero:
        print("El numero es menor")
        print("Intentalo de nuevo.")
        adivina =  introNumero()
    else:
        if adivina < numero:
            print("El numero es mayor")
            print("Intentalo de nuevo.")
            adivina = introNumero()
        else:
            if adivina == numero:
                print("Bien, Has acertado.")
                correcto = True
