# Pedimos el numero al usuario
n = int(input("Ingrese un número para calcular su factorial: "))

# le damos el valor a una variable 
factorial = 1  
i = 1

# Usar un bucle while
while i <= n:  # le damos la condicion en caso de no cumplirla se acaba el bucle
    # creamos el bucle 
    factorial *= i
    i += 1

# imprime eñ resultado
print(f"El factorial es {factorial}")
