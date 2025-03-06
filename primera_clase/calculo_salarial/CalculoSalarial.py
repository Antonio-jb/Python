""" Vas a capturar el nombre de una persona y el sueldo bruto que va a cobrar. Debes
 calcular el sueldo neto de dicha persona. Se le descuenta como IRPF un 12% y en
 concepto de seguridad social 5,20%. Mostrar un mensaje : El sueldo neto de
 xxxxxxxxxx es xxxxxxx euros. """

# Capturamos el nombre de la persona.
nombre = input("Introduzca nombre: ")
salario = int(input("Introduzca salario: "))


irpf = salario * 0.12
seguridadSocial = salario * 0.052
salarioNeto = salario - irpf - seguridadSocial
print(f"El salario neto es: {salarioNeto}" )


