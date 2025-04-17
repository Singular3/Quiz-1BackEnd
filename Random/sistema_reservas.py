vuelos = [
    {
        "vuelo": "AA123",
        "origen": "LAX",
        "destino": "JFK",
        "fecha": "2023-10-01",
        "hora": "08:00",
        "asientos_disponibles": 50,
        "reservas": []
    },
    {
        "vuelo": "AA456",
        "origen": "JFK",
        "destino": "LAX",
        "fecha": "2023-10-02",
        "hora": "09:00",
        "asientos_disponibles": 30,
        "reservas": []
    }
]

def mostrar_vuelos_disponibles(vuelos):
    print("Vuelos disponibles:")
    for vuelo in vuelos:
        print(f"Vuelo: {vuelo['vuelo']}, Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Fecha: {vuelo['fecha']}, Hora: {vuelo['hora']}, Asientos disponibles: {vuelo['asientos_disponibles']}")

def buscar_vuelo(vuelos, vuelo_id):
    for vuelo in vuelos:
        if vuelo["vuelo"] == vuelo_id:
            return vuelo
    return None

def reservar_vuelo():
    vuelo_id = input("Ingrese el ID del vuelo que desea reservar: ")
    vuelo = buscar_vuelo(vuelos, vuelo_id)
    if vuelo:
        if vuelo["asientos_disponibles"] > 0:
            nombre_pasajero = input("Ingrese el nombre del pasajero: ")
            vuelo["reservas"].append(nombre_pasajero)
            vuelo["asientos_disponibles"] -= 1
            print(f"Reserva exitosa para {nombre_pasajero} en el vuelo {vuelo['vuelo']}")
        else:
            print("Lo siento, no hay asientos disponibles para este vuelo.")
    else:
        print("Vuelo no encontrado.")

def cancelar_reserva():
    vuelo_id = input("Ingrese el ID del vuelo para cancelar la reserva: ")
    vuelo = buscar_vuelo(vuelos, vuelo_id)
    if vuelo:
        nombre_pasajero = input("Ingrese el nombre del pasajero cuya reserva desea cancelar: ")
        if nombre_pasajero in vuelo["reservas"]:
            vuelo["reservas"].remove(nombre_pasajero)
            vuelo["asientos_disponibles"] += 1
            print(f"Reserva cancelada para {nombre_pasajero} en el vuelo {vuelo['vuelo']}")
        else:
            print("No se encontró una reserva a nombre de ese pasajero.")
    else:
        print("Vuelo no encontrado.")

def menu():
    while True:
        print("\nSistema de Reservas de Vuelos")
        print("1. Mostrar vuelos disponibles")
        print("2. Reservar vuelo")
        print("3. Cancelar reserva")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_vuelos_disponibles(vuelos)
        elif opcion == "2":
            reservar_vuelo()
        elif opcion == "3":
            cancelar_reserva()
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()
