# Ejemplo de iteradores en Python

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# obtener el iterador de la lista
iterador = iter(numeros)
# Usar el iterador para recorrer la lista   
print(next(iterador))  # Imprime: 1
print(next(iterador))  # Imprime: 2 
print(next(iterador))  # Imprime: 3
print(next(iterador))  # Imprime: 4
print(next(iterador))  # Imprime: 5
# Intentar obtener el siguiente elemento después de haber recorrido toda la lista
try:
    print(next(iterador))  # Esto generará una excepción StopIteration
except StopIteration:
    print("No hay más elementos en el iterador.")       
# También podemos usar un bucle for para recorrer el iterador
print("Recorriendo la lista con un bucle for:") 
for numero in numeros:
    print(numero)  # Imprime cada número de la lista    
# Crear un iterador personalizado usando una clase  
class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador < self.limite:
            numero = self.contador
            self.contador += 1
            return numero
        else:
            raise StopIteration
# Usar el iterador personalizado
contador = Contador(5)
print("Contando con el iterador personalizado:")
for numero in contador:
    print(numero)  # Imprime los números del 0 al 4
      
