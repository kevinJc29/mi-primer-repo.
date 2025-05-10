
def es_numero_perfecto(n): # Declara una función que recibe un número entero n y retorna si es perfecto (True o False).
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def main():
    numero = int(input("Ingresa un número: "))
    print(f"{numero} es un número perfecto." #" si es_numero_perfecto(numero)
        # else f"{numero} no es un número perfecto.")
        if es_numero_perfecto(numero) # La función retorna True solo si ambas condiciones se cumplen
        else f"{numero} no es un número perfecto.") # La función retorna Falsa si alguna de las condiciones no se cumple

main()