# baraja = [2,3,4]
# manoCasa = []
# manoJugador = []
#
# print (baraja)
# carta = baraja.pop()
# print(baraja)
# print(carta)

# Ojetivo: Llegar a 21 sin pasarse
# Juegas contra la casa
# Te puedes plantar siempre que no hayas llegado
# o seguir pidiendo cartas.
# La casa se planta cuando tiene 17 o mas cartas
# A = 1, 11
# J, Q, K = 10
# 2..10 = su valor

from blackjack.Carta import Carta
import random
import time

baraja = []
palos = ["♣️", "♠️", "♥️", "♦️"]
letras = ["J", "Q", "K", "A"]

barajaCasa = []
barajaJugador = []

def baraja_nueva():
    for palo in palos:
        for i in range(2, 11):
            baraja.append(Carta(i, f"{i} de {palo}", palo,))

        for letra in letras:
            baraja.append(Carta(letra, f"{letra} de {palo}", palo,))

def barajear(baraja):
    random.shuffle(baraja)


def valor_cartas(baraja):
    suma_baraja = 0
    for carta in baraja:
        valor_carta = carta.valor

        if valor_carta in ["K", "J", "Q"]:
            valor_carta = 10

        elif valor_carta == "A":
            if suma_baraja + 11 > 21:
                valor_carta = 1
            else:
                valor_carta = 11

        elif isinstance(valor_carta, int):
            valor_carta = carta.valor

        suma_baraja += valor_carta

    return suma_baraja


def repartir_carta(baraja, to_baraja):
    nombre = ""
    if to_baraja == barajaCasa:
        nombre = "cupier"
    if to_baraja == barajaJugador:
        nombre = "jugador"
    print(f"repartiendo carta a {nombre}...")
    print("--------------------------------------------")
    time.sleep(3)
    carta_sacada = baraja.pop()
    to_baraja.append(carta_sacada)
    print(f"LA CARTA ES -> {carta_sacada.nombre}")
    print("-----------------------------------------")
    print(f"La suma de la baraja del {nombre_jugador(to_baraja)} es: {valor_cartas(to_baraja)}")
    print("-----------------------------------------")

def nombre_jugador(baraja):
    nombre = ""
    if baraja == barajaCasa:
        nombre = "cupier"
    if baraja == barajaJugador:
        nombre = "jugador"

    return nombre

def inicio_partida():
    for i in range (0, 2):
        repartir_carta(baraja, barajaJugador)

def comprobar_cartas():
    if valor_cartas(barajaJugador) > 21:
        print("EL CUPIER HA GANADO")
        exit(0)
    if valor_cartas(barajaCasa) > 21:
        print("EL JUGADOR HA GANADO")
        exit(0)
    if valor_cartas(barajaJugador) == 21:
        print("EL JUGADOR HA GANADO")
        exit(0)
    if valor_cartas(barajaCasa) == 21:
        print("EL CUPIER HA GANADO")
        exit(0)

print("--------------------------------------------")
print("Empezando partida...")
print("--------------------------------------------")
baraja_nueva()
barajear(baraja)

inicio_partida()
repartir_carta(baraja, barajaCasa)

plantarse_respuesta = ""
plantarse = False
while valor_cartas(barajaJugador) < 21 and plantarse == False:
    plantarse_respuesta = input("¿Te quieres plantar? (S/N)")
    if plantarse_respuesta.lower() == "n":
        repartir_carta(baraja, barajaJugador)
        comprobar_cartas()
    else:
        plantarse = True
        print("")
        print("--------------------------------------------")
        print("El jugador se ha plantado")
        print("--------------------------------------------")
        print("")
        time.sleep(1)

if valor_cartas(barajaCasa) >= 17:
    print("El cupier se ha plantado")
else:
    while valor_cartas(barajaCasa) < 17 or valor_cartas(barajaJugador) == 21:
        repartir_carta(baraja, barajaCasa)
        comprobar_cartas()
