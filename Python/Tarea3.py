def contar_pares_impares():

    entrada = input("Ingrese una lista de números separados por comas: ")
    numeros = list(map(int, entrada.split(",")))    
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
contar_pares_impares()