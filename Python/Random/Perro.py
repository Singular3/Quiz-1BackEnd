from Animal import Animal

class Perro(Animal) :

    def __init__ (self, raza, color, name, age, species) :
        super().__init__(name, age, species)
        self.raza = raza
        self.color = color

    def ladrar(self) :
        print (f"{self.name} is barking")

    def moverse(self) :
        print (f"{self.name} is running")

    def eat(self) :
        print (f"{self.name} is eating dog food")

    def sleep(self) :
        print (f"{self.name} is sleeping in the dog house")

    


