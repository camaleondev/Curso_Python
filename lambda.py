sumar = lambda a, b: a + b
print(sumar(10, 4))

multiplicar = lambda a, b: a * b
print(multiplicar(80, 4))

numeros = list(range(11))
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Cuadrados:", cuadrados)

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", numeros_pares)

