# Ejercicio 3

inventario = {}

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario:")
        for producto, cantidad in inventario.items():
            print(f"- {producto}: {cantidad} unidades")

def agregar_producto():
    producto = input("Introduce el nombre del producto: ")
    cantidad = int(input("Introduce la cantidad: "))
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    print(f"Producto '{producto}' agregado/actualizado en el inventario.")

def modificar_cantidad():
    producto = input("Introduce el nombre del producto a modificar: ")
    if producto in inventario:
        cantidad = int(input("Introduce la nueva cantidad: "))
        inventario[producto] = cantidad
        print(f"Cantidad de '{producto}' actualizada a {cantidad} unidades.")
    else:
        print(f"El producto '{producto}' no está en el inventario.")

def eliminar_producto():
    producto = input("Introduce el nombre del producto a eliminar: ")
    if producto in inventario:
        del inventario[producto]
        print(f"Producto '{producto}' eliminado del inventario.")
    else:
        print(f"El producto '{producto}' no está en el inventario.")

while True:
    print("\nGestión de Inventario")
    print("1. Mostrar inventario")
    print("2. Agregar/Actualizar producto")
    print("3. Modificar cantidad de producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        modificar_cantidad()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")