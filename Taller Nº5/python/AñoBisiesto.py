# Pedimos al usuario que introduzca un año
año = int(input("Ingresa un año: "))  # Convertimos la entrada a entero

# Definimos una función que determina si es bisiesto
def es_bisiesto(año):
    # Retorna True si es divisible por 4 y no por 100, o si es divisible por 400
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Usamos la función para comprobar el año
if es_bisiesto(año):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")
