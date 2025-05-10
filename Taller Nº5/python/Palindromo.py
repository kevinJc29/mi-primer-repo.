def es_palindromo(texto):
    # Convertimos a minúsculas y eliminamos espacios
    texto_limpio = texto.replace(" ", "").lower()
    # Comparamos con el texto invertido
    return texto_limpio == texto_limpio[::-1]

# Solicitamos al usuario que ingrese una frase
entrada = input("Escribe una palabra o frase para verificar si es un palíndromo: ")

# Verificamos y mostramos el resultado
if es_palindromo(entrada):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
