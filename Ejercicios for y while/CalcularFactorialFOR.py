# Pedimos al usuario el numero 
n = int(input("Ingrese un número para calcular su factorial: ")) # 

factorial = 1  # le damos el valor a una variable 

# con for iniciamos el ciclo || con range creamos la secuencia de numeros
for i in range(1, n + 1):
    factorial *= i  

# muestra el resultado 
print(f"El factorial es {factorial}") 
