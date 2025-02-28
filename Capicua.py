# Realiza un programa que pida un numero entero positivo de n cifras, y que compruebe
# si el número es capicua
# 12344321

num = input("Ingresa el número: ")
esCapicua = True

for i in range(len(num//2)):
    if num[i] != num[-1 -i]:
        esCapicua = False

if esCapicua:
    print("Es capicua.")
else:
    print("No es capicua.")

# numInvertido = num[::-1]

# if num == numInvertido:
#    print("El número es capicua.")
#else:
#    if num != numInvertido:
#        print("El número no es capicua.")
