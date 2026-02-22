# 2a Vad gör följande kod? Fixa eventuella fel.
# class Animal:
#     def make_noise(self):
#         print("Detta djur har vi inget ljud för.")
#
# class Dog(Animal):
#     def make_noise(self):
#     print("Voff!")
#
# class Cat(Animal):
#     def make_noise(shelf):
#         super().make_noise()
#         print("Mjau!")
#
# def sound_off(animal):
#     animal.make_noise()
#
# c = Cat()
# d = Dog()
# h = Rooster()
# sound_off([c, d, h])

class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        # Print funktionen låg i fel rad
        print("Voff!")

class Cat(Animal):
    # Felstavat på shelf istället för self
    def make_noise(self):
        super().make_noise()
        print("Mjau!")
# Ny Class för Rooster skapad
class Rooster(Animal):
    def make_noise(self):
        print("Kuckelikuu!")

class Pig(Animal):
    def make_noise(self):
        print("Nuff Nuff!")

def sound_off(animals):
    # Skapar loop för djuren i listan
    for animal in animals:
        # animal låg i fel rad
        animal.make_noise()

c = Cat()
d = Dog()
# Class Rooster saknas
h = Rooster()
# 2b lägger till ett till djur
p = Pig()
sound_off([c, d, h, p])


# Nu skriver den ut Mjau!, Voff!, Kuckelikuu!, Nuff Nuff!