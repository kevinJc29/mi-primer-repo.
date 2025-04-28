# Definimos una función para verificar si un número es primo
def es_primo(numero):
    if numero > 1:
        i = 2
        # Verificamos si el número es divisible por algún número menor que él
        # hasta la raíz cuadrada del número
        while i <= int(numero**0.5):
            # Si es divisible no es primo
            # si el numero es divisible por i entonces no es primo
            if numero % i == 0:
                return False
            i += 1
        return True
    return False

contador = 0
numero = 2
# si el contador es menor a 20 entonces entra al bucle
while contador < 20:
    if es_primo(numero):
        print(numero)
        contador += 1
    numero += 1