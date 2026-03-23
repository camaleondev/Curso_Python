numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print("aqui el numero es  :", number)

for i in range(3,10):
    print("el numero es :", i)

fruits = ["manzana", "banana", "cereza", "durazno"]    
for fruit in fruits:
    print("aqui la fruta es  :", fruit)
    if fruit == "cereza":
        print("¡Encontré una cereza!")
        break
x = 0
while x < 5:
    print("El valor de x es:", x)
    x += 1

numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    if number == 3:
        continue # Salta el número 3 y continúa con el siguiente
    print("aqui el numero es  :", number)


