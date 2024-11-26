palabra = input("Introduce una palabra: ")

vocales = "aeiouAEIOU"
contador_vocales = 0

for letra in palabra:
    if letra in vocales:
        contador_vocales += 1

print("La palabra tiene", contador_vocales, "vocales.")
