# Ejercicio 1:

def es_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = filter(es_par, numeros)

print(list(pares))

# Ejercicio 2:

def multiplicar_por_dos(x):
    return x * 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = map(multiplicar_por_dos, numeros)

resultado_list = list(resultado)
print(resultado_list)

# Ejercicio 3:

def convertir_mayuscula(x):
    return x.upper()

minusculas = ['a', 'b', 'c', 'd', 'e']

resultado = map(convertir_mayuscula, minusculas)
print(list(resultado))

# Ejercicio 4:

numeros = [67, 89, 90, 1, 78, 34, 100]

numeros_ordenados = sorted(numeros)

print(numeros_ordenados)