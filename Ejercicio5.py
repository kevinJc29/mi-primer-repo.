# Pedir la nota al usuario
nota = float(input("Ingresa tu nota de (0 a 100:) "))

# Determinar la calificación
if 90 <= nota <= 100:
    print("Calificación: Excelente")
elif 70 <= nota < 90:
    print("Calificación: Aprobado")
elif 0 <= nota < 70:
    print("Calificación: Reprobado")
else:
    print("Error: Nota fuera de rango")