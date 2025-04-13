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

# ejercicio 5:

def redondear_valores(diccionario):
    diccionario_redondeado = {}
    for clave, valor in diccionario.items():
        diccionario_redondeado[clave] = round(valor)
    return diccionario_redondeado

mi_diccionario = {
    "a": 1.5,
    "b": 2.3,
    "c": 3.7
}

mi_diccionario_redondeado = redondear_valores(mi_diccionario)
print(mi_diccionario_redondeado)

# Ejercicio 6:

palabras = ["manzana", "banana", "kiwi", "naranja", "mango"]

logitudes = map(len, palabras)

print("palabras:", palabras)
print("longitufes:", list(logitudes))

# Ejercicio 7:

palabras =["python", "java", "c++", "javascript", "ruby"]

palabras_filtradas = list(filter(lambda x: len(x) > 5, palabras))
print(palabras_filtradas)

# Ejercicio 8:

lista_strings = ["1", "2", "3", "24", "67"]

lista_enteros = list(map(int, lista_strings))
print(lista_strings)
print(lista_enteros)

# Ejercicio 9:

numeros = [-10, -5, 0, 5, 10]

positivos = list(filter(lambda x: x > 0, numeros))
print(positivos)
print(numeros)

# Ejercicio 10:

personas = [("Juan", 25), ("Ana", 30), ("Pedro", 20), ("Maria", 35)]

personas_ordenadas = sorted(personas, key=lambda x: x[1])
print(personas_ordenadas)
print(personas)

# Ejercicio 11:

temperaturas_celsius = [0, 20, 37, 100]

temperaturas_fahrenheit = list(map(lambda x: (x * 9/5) + 32, temperaturas_celsius))
print(temperaturas_fahrenheit)
print(temperaturas_celsius)

# Ejercicio 12:

numeros = [6.7, 8.2, 3.5, 9.1]

numeros_redondeados = list(map(round, numeros))
print(numeros_redondeados)
print(numeros)

# Ejercicio 13:

lista = [5, 3, 5, 2, 3, 1,]

lista_unica_ordenada = sorted(set(lista))
print(lista_unica_ordenada)
print(lista)

