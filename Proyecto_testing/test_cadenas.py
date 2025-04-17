from cadenas import es_palindromo, contar_vocales

def test_es_palindromo():
    assert es_palindromo("Anita lava la tina") is True  
    assert es_palindromo("Hola mundo") is False
   

def test_contar_vocales():
    assert contar_vocales("Hola Mundo") == 4