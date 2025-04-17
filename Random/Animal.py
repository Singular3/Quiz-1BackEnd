class Animal :

    def __init__ (self, name, age, species) :
        self.species = species
        self.name = name
        self.age = age
    
    def moverse(self) :
        print (f"{self.name} is moving")

    def eat(self) :
        print (f"{self.age} is eating")

    def sleep(self) :
        print (f"{self.species} is sleeping")