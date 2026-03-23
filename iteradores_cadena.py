# iterar en cadenas de texto
# Crear una cadena de texto
texto = "Hola, mundo!"
# Obtener el iterador de la cadena
iterador_texto = iter(texto)
# Usar el iterador para recorrer la cadena
print(next(iterador_texto))  # Imprime: H
print(next(iterador_texto))  # Imprime: o   
print(next(iterador_texto))  # Imprime: l
print(next(iterador_texto))  # Imprime: a
print(next(iterador_texto))  # Imprime: ,
print(next(iterador_texto))  # Imprime:  
print(next(iterador_texto))  # Imprime: m
print(next(iterador_texto))  # Imprime: u
print(next(iterador_texto))  # Imprime: n
print(next(iterador_texto))  # Imprime: d
print(next(iterador_texto))  # Imprime: o
print(next(iterador_texto))  # Imprime: !
# Intentar obtener el siguiente elemento después de haber recorrido toda la cadena


# Crear una cadena de texto
texto = "Hola, mundo!"
# Obtener el iterador de la cadena
iterador_texto = iter(texto)
# Usar el iterador para recorrer la cadena
for caracter in iterador_texto:
    print(caracter)  # Imprime cada caracter de la cadena
# También podemos usar un bucle for directamente sobre la cadena sin necesidad de obtener el iterador       
# Recorrer la cadena directamente con un bucle for
print("Recorriendo la cadena con un bucle for:")
for caracter in texto:
    print(caracter)  # Imprime cada caracter de la cadena 
     