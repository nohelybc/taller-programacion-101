# Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression
# Example:
# Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
# Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.
#
# Solution: 
#Don't use classes, just functions

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