def bienvenida():
    nombre = input("¿Cuál es tu nombre? ")
    print(f"¡Hola, {nombre}! Bienvenido al programa de pruebas.")

# funció 2
def calcular_promedio():
    # solicitar notas al usuario
    while True:
        try:
            nota1 = float(input("Ingrese la primera nota: "))
            nota2 = float(input("Ingrese la segunda nota: "))
            nota3 = float(input("Ingrese la tercera nota: "))
            break
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

            #calcular promedio
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

# mostrar el resultado
def mostrar_resultado(promedio):
    print(f"El promedio de las notas es: {promedio:.2f}")

def main():
    bienvenida()
    promedio = calcular_promedio()
    mostrar_resultado(promedio)

if __name__ == "__main__":
    main()
# Ejercicio 1: 