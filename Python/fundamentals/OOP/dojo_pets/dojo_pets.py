import ninja
import pets

# ========================TESTS=============================================

# Basic Tests

pet1 = pets.Pet("Fido", "dog", ["sit", "stay", "roll over"])
ninja1 = ninja.Ninja("Hayden", "Durand", pet1, "bone", "kibble")

ninja1.walk(pet1).feed(pet1).bathe(pet1)

# Pet Type Tests
pet2 = pets.Cat("Furball")
ninja1.walk(pet2)
pet2.play(ninja1)
pet2.play(ninja1, ninja1.treats)


