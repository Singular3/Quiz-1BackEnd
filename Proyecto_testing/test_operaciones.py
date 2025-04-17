
from operaciones import suma, resta, multiplicar, dividir

def test_suma():
    assert suma(3, 2) == 5
    

def test_resta():
    assert resta(5, 3) == 2
    

def test_multiplicar():
    assert multiplicar(4, 3) == 12
    
def test_dividir():
     assert dividir(10, 2) == 5
   