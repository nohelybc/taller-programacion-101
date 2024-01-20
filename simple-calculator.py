
def calculator():
    operacion = input("¿Qué operación quieres realizar? (suma, resta, multiplicacion, division): ")
    primer_numero = input("Primer número para la operación: ")
    segundo_numero = input("Segundo número para la operación: ")
    if operacion == "suma":
        return int(primer_numero) + int(segundo_numero)
    elif operacion == "resta":
        return int(primer_numero) - int(segundo_numero)
    elif operacion == "multiplicacion":
        return int(primer_numero) * int(segundo_numero)
    elif operacion == "division":
        return int(primer_numero) / int(segundo_numero)
    else:
        return "Invalid operation"