def es_nino(edad):
    return edad <13

def es_adolecente(edad):
    return 13 <= edad < 18

def es_adulto(edad):
    return 18 <= edad < 60

def es_adulto_mayor(edad):
    return edad >= 60

# funcion principal

def clasificar_edad(edad):
    if es_nino(edad):
        return "Niño"
    elif es_adolecente(edad):
        return "Adolescente"
    elif es_adulto(edad):
        return "Adulto"
    else:
        return "Adulto Mayor"
    
#solicitar edad al usuario
edad = int(input("Ingrese su edad: "))

resultado = clasificar_edad(edad)
print(f"Usted es: {resultado}")