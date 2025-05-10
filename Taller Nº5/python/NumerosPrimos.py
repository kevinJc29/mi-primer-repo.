# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:  # Los números menores que 2 no son primos
        return False
    for i in range(2, int(n**0.5) + 1):  # Verificamos hasta la raíz cuadrada de n
        if n % i == 0:  # Si es divisible por otro número, no es primo
            return False
    return True  # Si no encontramos divisores, es primo

# Función para sumar primos en el rango [a, b]
def suma_primos_en_rango(a, b):
    suma = 0
    for i in range(min(a, b), max(a, b) + 1):  # Recorremos desde el menor hasta el mayor
        if es_primo(i):  # Si el número es primo, lo sumamos
            suma += i
    return suma

# Solicitar al usuario los dos números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

# Calcular e imprimir el resultado
resultado = suma_primos_en_rango(a, b)
print(f"La suma de los números primos entre {a} y {b} es: {resultado}")
