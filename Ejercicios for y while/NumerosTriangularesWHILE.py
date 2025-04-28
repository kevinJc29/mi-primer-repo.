# pedimos al usuario el numero
N = int(input("Ingrese el valor de N: "))

# mostramos en pantalla 
print("Números triangulares usando while:")
i = 1  # le damos el valor 


while i <= N:  # le damos una condicion
    triangular = i * (i + 1) // 2   # usamos esta fotmula para calcular el numero triangular
    print(triangular)
    i += 1  # suma un nunmero al siguiente ciclo
