class CifradoCesar:
    

    def __init__(self, desplazamiento):
        
        self.desplazamiento = desplazamiento
        self.alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def cifrar(self, mensaje):
       
        mensaje = mensaje.upper()
        resultado = ""

        for letra in mensaje:
            if letra in self.alfabeto:
                posicion_original = self.alfabeto.index(letra)
                nueva_posicion = (posicion_original + self.desplazamiento) % 26
                resultado += self.alfabeto[nueva_posicion]
            else:
                resultado += letra  

        return resultado

    def descifrar(self, mensaje_cifrado):
      
        mensaje_cifrado = mensaje_cifrado.upper()
        resultado = ""

        for letra in mensaje_cifrado:
            if letra in self.alfabeto:
                posicion_cifrada = self.alfabeto.index(letra)
                posicion_original = (posicion_cifrada - self.desplazamiento) % 26
                resultado += self.alfabeto[posicion_original]
            else:
                resultado += letra

        return resultado




