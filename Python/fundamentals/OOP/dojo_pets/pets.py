class Pet:
    def __init__(self, name, type, tricks, health=100, energy=100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        print(f"{self.name} is sleeping")
        return self

    def eat(self, food):
        print(f"{self.name} eats {food}")
        return self

    def play(self, owner):
        print(f"{self.name} plays with {owner.first_name}")
        return self

    def noise(self):
        print(f"{self.name} makes a noise")
        return self

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, type="Cat", tricks=None)
        # self.type = "Cat"
        # self.tricks = None
        self.energy = 50
    
    def play(self, owner, treats=""):
        if (treats == ""):
            print(f"{self.name} isn't interested in playing your stupid games, {owner.first_name}")
        else:
            print(f"{self.name} only plays with {owner.first_name} for the treats")
        
        return self

    def noise(self):
        print(f"{self.name} meows")
        return self
