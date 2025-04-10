# Diccionario
datos = {
    "producto": "Zapatillas Air Max",
    "talla": 42,
    "color": "Rojo",
    "stock": 20
}

nombres_empleados = ["Juan", "Ana", "Pedro", "María", "Luis"]

def mostrar_menu():
    print("\n--- MENÚ INTEREACTIVO ---")
    print("1. Mostrar mensaje motivacional")
    print("2. Mostrar lista de nombres")
    print("3. Modificar valor en el inventario")
    print("4. Eliminar elemento del inventario")
    print("5. Mostrar inventario actual")
    print("6. Salir")

def mostrar_mensaje_():
     print("\n¡Sigue adelante, cada paso cuenta!")

def mostrar_nombres():
    print("\nLista de nombres de empleados:")
    for nombre in nombres_empleados:
     print(nombre)

def modificar_inventario():
    print("\nModificación de inventario")
    clave = input("Ingrese la clave del producto a modificar: ")
    if clave in datos:
        nuevo_valor = input(f"Ingrese el nuevo valor para {clave}: ")
        datos[clave] = nuevo_valor
        print(f"Valor de {clave} modificado a: {nuevo_valor}")
    else:
        print("Clave no encontrada en el inventario.")

def eliminar_elemento():
    print("\nEliminación de elemento del inventario")
    clave = input("Ingrese la clave del producto a eliminar: ")
    if clave in datos:
        del datos[clave]
        print(f"Elemento {clave} eliminado del inventario.")
    else:
        print("Clave no encontrada en el inventario.")

def mostrar_inventario():
    print("\nInventario actual:")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-6): ")
    
    if opcion == "1":
        mostrar_mensaje_()
    elif opcion == "2":
        mostrar_nombres()
    elif opcion == "3":
        modificar_inventario()
    elif opcion == "4":
        eliminar_elemento()
    elif opcion == "5":
        mostrar_inventario()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")