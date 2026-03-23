# Fibonacci sequence generator
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b 
# Example usage
for number in fibonacci(int(input("ingresa un número limite: "))):
    print(number)