# Ejercicio 2

def metros_a_kilometros(m):
    return m / 1000

def gramos_a_kilogramos(g):
    return g / 1000

def centigrados_a_fahrenheit(c):
    return (c * 9/5) + 32

print("Conversor de Unidades")

while True:
    print("\nSelecciona una opción:")
    print("1. Metros a Kilómetros")
    print("2. Gramos a Kilogramos")
    print("3. Centígrados a Fahrenheit")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        metros = float(input("Introduce la cantidad en metros: "))
        kilometros = metros_a_kilometros(metros)
        print(f"{metros} metros son {kilometros} kilómetros.")
    elif opcion == "2":
        gramos = float(input("Introduce la cantidad en gramos: "))
        kilogramos = gramos_a_kilogramos(gramos)
        print(f"{gramos} gramos son {kilogramos} kilogramos.")
    elif opcion == "3":
        centigrados = float(input("Introduce la temperatura en grados centígrados: "))
        fahrenheit = centigrados_a_fahrenheit(centigrados)
        print(f"{centigrados} grados centígrados son {fahrenheit} grados Fahrenheit.")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")