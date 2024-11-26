import random

numero_aleatorio = random.randint(1, 100)

intentos = 0

while True:
    intento = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1

    if intento < numero_aleatorio:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_aleatorio:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
