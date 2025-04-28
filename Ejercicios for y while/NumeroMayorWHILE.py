import random  # Generamos números aleatorios

# Definimos cuántos números queremos
cantidad = 10

# Creamos una lista de números aleatorios entre 1 y 500
numeros = [random.randint(1, 500) for _ in range(cantidad)]

print("Lista de números aleatorios:", numeros)

# Inicializamos el mayor con el primer número de la lista
mayor = numeros[0]


i = 0
while i < len(numeros): 
    # Comparamos el número actual con el mayor
    if numeros[i] > mayor:
        mayor = numeros[i] # Si el número actual es mayor, lo asignamos a mayor
    i += 1  # Incrementamos el índice para pasar al siguiente número

print(f"El número mayor es: {mayor}")
