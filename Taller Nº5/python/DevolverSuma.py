# Función que suma los dígitos de un número entero positivo
def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10 # Tomamos el último dígito y lo sumamos
        n = n // 10    # Eliminamos el último dígito (división entera)
    return suma

# Solicitamos el número al usuario
numero = int(input("Ingresa un número entero positivo: "))

# Verificamos que sea positivo
if numero > 0:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")
else:
    print("El número debe ser entero y positivo.")
