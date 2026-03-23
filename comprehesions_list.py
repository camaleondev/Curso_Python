squares = [x**2 for x in range(1, 11)]  
print("cuadrados:", squares)

celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = [((9/5) * temp + 32) for temp in celsius]
print("Fahrenheit:", fahrenheit)

evens = [x for x in range(1, 21) if x % 2 == 0]
print("Números pares:", evens)  

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Matriz transpuesta:", transposed)

list = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in list]
print("Doblados:", doubled)

words = ["SOL", "mar", "CIELO", "tierra"]
capitalized = [word.upper() for word in words if len(word) > 3]
print("Palabras capitalizadas con más de 3 caracteres:", capitalized)

# Crear un Diccionario con List Comprehension
claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]

diccionario = {clave: valor for clave, valor in zip(claves, valores)}

print(diccionario)

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

resultado = [p["nombre"] for p in personas if p["ciudad"] == "Madrid" and p["edad"] > 30]

print(resultado)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = [n * 2 if n % 2 == 0 else n for n in numeros]

print(resultado)