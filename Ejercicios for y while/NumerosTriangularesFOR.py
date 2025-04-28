# Número de elementos que queremos imprimir
N = int(input("Valor de N: "))

# mostramos en pantalla
print("Números triangulares usando for:")

# con for iniciamos el ciclo || con range creamos la secuencia de nuemeros
for i in range(1, N + 1):
    triangular = i * (i + 1) // 2     # usamos esta fotmula para calcular el numero triangular
    print(triangular)
