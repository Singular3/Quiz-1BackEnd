# Ejercicio 1

#1

import random

numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("Bienvenido al juego de adivinar el número secreto.")
print("He elegido un número entre 1 y 100. ¿Puedes adivinar cuál es?")

#2

while not adivinado:
    intento  = int(input("introduce tu intento: "))
    intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
        adivinado = True