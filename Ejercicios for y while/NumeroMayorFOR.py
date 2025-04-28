import random  # Generamos números aleatorios

# Definimos cuántos números queremos
cantidad = 10

# Creamos una lista de números aleatorios entre 1 y 500
numeros = [random.randint(1, 501) for _ in range(cantidad)]

print("Lista de números aleatorios:", numeros)

# Inicializamos el mayor con el primer número de la lista
mayor = numeros[0]

# Usamos un bucle for para recorrer la lista de números
# y encontrar el mayor
for numero in numeros:
    if numero > mayor:
        mayor = numero

print(f"El número mayor es: {mayor}")
