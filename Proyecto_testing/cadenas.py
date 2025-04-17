def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    return palabra == palabra[::-1]

def contar_vocales(texto):
    return sum(1 for char in texto if char in 'aeiouáéíóúü')