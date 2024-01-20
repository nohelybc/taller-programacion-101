# if conditional
if 5 > 3:
    print("5 es mayor que 3")

# if else conditional
if 5 < 3:
    print("5 es menor que 3")
else:
    print("5 no es menor que 3")

# ejercicio 1
numero = int(input("Ingresa un número: "))
if numero > 5:
    print("El número es mayor que 5")
elif numero == 5:
    print("El número es igual a 5")
else:
    print("El número es menor que 5")

# ejemplo de for loop
for i in range(5):
    print(i) # i debe de imprimirse 5 veces, el resultado es 0, 1, 2, 3, 4

# ejemplo de while loop
i = 0
while i < 5:
    print(i) # i debe de imprimirse 5 veces, el resultado es 0, 1, 2, 3, 4
    i += 1 # i = i + 1

# ejemplo 2 con for loop
saludo = "Hola mundo"
for letra in saludo:
    print(letra) # letra debe de imprimirse 10 veces, el resultado es "Hola mundo"

# funciones en python
def suma(a, b):
    return a + b

print(suma(5, 5)) # imprime 10
