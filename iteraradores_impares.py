# crear un iterador para números impares
# limite de números impares
limite = 10

impares =iter(range(1, limite+1,2))

# Usar el iterador para recorrer los números impares
for numero in impares:
    print(numero)  # Imprime los números impares del 1 al 9 