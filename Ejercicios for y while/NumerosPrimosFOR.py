# Número de primos que queremos
cantidad_primos = 20
primos_encontrados = 0
numero = 2  # Empezamos desde el primer número primo

print("Primeros 20 números primos son:")

for numero in range(2, 10**6):  # Usamos un rango suficientemente grande
    if primos_encontrados >= cantidad_primos:
        break

    # Verificamos si el número es primo
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    # imprime la condicion si es verdadero
    # si es primo lo imprime y suma uno a la variable primos_encontrados
    if es_primo:
        print(numero)
        primos_encontrados += 1