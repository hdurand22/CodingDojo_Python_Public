import pets

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self, pet):
        print(f"{self.first_name} walks {pet.name}")
        return self

    def feed(self, pet):
        print(f"{self.first_name} feeds {pet.name} {self.pet_food}")
        pet.eat(self.pet_food)
        return self

    def bathe(self, pet):
        print(f"{self.first_name} bathes {pet.name}")
        pet.noise()
        return self