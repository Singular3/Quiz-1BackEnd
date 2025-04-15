from cifrado_cesar import CifradoCesar

def mostrar_ejemplo(mensaje, clave):
    
    cifrador = CifradoCesar(clave)

    print(f"\nMensaje original: {mensaje}")
    print(f"Clave de desplazamiento: {clave}")

    mensaje_cifrado = cifrador.cifrar(mensaje)
    print(f"Mensaje cifrado: {mensaje_cifrado}")

    mensaje_descifrado = cifrador.descifrar(mensaje_cifrado)
    print(f"Mensaje descifrado: {mensaje_descifrado}")

def main():
   
    print("=== Ejemplos de Cifrado César ===")
   
    mostrar_ejemplo("HOLA MUNDO", 1)
    mostrar_ejemplo("HOLA MUNDO", 10)
    mostrar_ejemplo("HOLA MUNDO", 3)
    mostrar_ejemplo("HOLA MUNDO", 56)

if __name__ == "__main__":
    main()
