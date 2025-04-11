def contar_vocales(frase):

    vocales = "aeiouAEIOU"
    
    contador = 0
    
    for caracter in frase:
        if caracter in vocales:
            contador += 1
    
    return contador

frase = input("Ingrese una frase: ")

resultado = contar_vocales(frase)

print(f"El número de vocales en la frase es: {resultado}")